// ==========================================================================
// BIGDATA LAB - HR EMPLOYEE ATTRITION SYSTEM CLIENT LOGIC
// Sinh viên: Vũ Lê Anh Đức - MSSV: 2001230191
// ==========================================================================

document.addEventListener("DOMContentLoaded", () => {
    // Stage metadata
    const stageDetails = {
        "hdfs_prepare": {
            num: "1. Chuẩn bị HDFS Data Lake",
            desc: "Tạo cấu trúc thư mục phân cấp Data Lake HDFS (/raw, /processed, /output) tương thích Apache Hadoop trên máy và phân vùng lưu trữ chịu lỗi.",
            cmd: "run-stage hdfs_prepare"
        },
        "upload_data": {
            num: "2. Ingest Dữ Liệu Nguồn",
            desc: "Nạp và kiểm tra tập dữ liệu nhân sự WA_Fn-UseC_-HR-Employee-Attrition.csv (1,470 dòng, 35 thuộc tính) vào tầng lưu trữ raw/ của Data Lake.",
            cmd: "run-stage upload_data"
        },
        "spark_read": {
            num: "3. Đọc Bằng Apache Spark",
            desc: "Khởi tạo Apache Spark / PySpark In-Memory DataFrame, đọc trực tiếp dữ liệu CSV từ HDFS và tự động suy luận Schema (InferSchema).",
            cmd: "run-stage spark_read"
        },
        "spark_clean": {
            num: "4. Feature Engineering & Parquet",
            desc: "Loại bỏ cột hằng số vô nghĩa (EmployeeCount, StandardHours, Over18), trích xuất 5 đặc trưng mới và tối ưu hóa ghi ra định dạng nén cột Snappy Parquet.",
            cmd: "run-stage spark_clean"
        },
        "spark_sql": {
            num: "5. Spark SQL Đa Chiều (6 Queries)",
            desc: "Tạo bảng tạm SQL, thực thi 6 truy vấn sâu: Làm thêm giờ (OverTime), Mức lương phòng ban, Chức vụ và Cân bằng cuộc sống.",
            cmd: "run-stage spark_sql"
        },
        "ml_predict": {
            num: "6. MLlib Random Forest & K-Means",
            desc: "Huấn luyện Random Forest & Logistic Regression xử lý lệch lớp, phân cụm K=4, đánh giá ROC-AUC 0.81 và vượt qua 6/6 test suites.",
            cmd: "run-stage ml_predict"
        },
        "save_results": {
            num: "7. Xuất HDFS & Cảnh Báo 3 Cấp",
            desc: "Chấm điểm rủi ro nghỉ việc (Risk Score %), phân loại 3 cấp độ (Xanh/Vàng/Đỏ), lọc 172 nhân viên nguy cơ cao và lưu trữ HDFS Output.",
            cmd: "run-stage save_results"
        },
        "kafka_stream": {
            num: "8. Kafka Ingest & AI Suy Luận",
            desc: "Mô phỏng Producer phát sự kiện streaming (check-in muộn, OT đêm) vào Topic 'hr-employee-events' và Consumer AI chấm điểm tức thời.",
            cmd: "run-stage kafka_stream"
        },
        "airflow_dag": {
            num: "9. Điều Phối Apache Airflow DAG",
            desc: "Thiết lập đồ thị điều phối có hướng DAG (Orchestration), lên lịch chạy tự động @daily và cấu hình dependency từ Bước 1 đến Bước 8.",
            cmd: "run-stage airflow_dag"
        }
    };

    let currentStage = "hdfs_prepare";
    let isStreamingActive = false;
    let streamInterval = null;
    let chartInstances = {};

    // DOM Elements
    const terminalOutput = document.getElementById("terminal-output");
    const termInput = document.getElementById("term-input");
    const btnTermRun = document.getElementById("btn-term-run");
    const btnClearTerm = document.getElementById("btn-clear-term");
    const btnRunCurrentStage = document.getElementById("btn-run-current-stage");
    const btnRunAll = document.getElementById("btn-run-all-pipeline");
    const selectedTitle = document.getElementById("selected-title");
    const selectedDesc = document.getElementById("selected-desc");
    const btnUpload = document.getElementById("btn-upload-dataset");
    const fileInput = document.getElementById("csv-file-input");

    // =========================================================================
    // 1. NAVIGATION TAB SWITCHING
    // =========================================================================
    document.querySelectorAll(".nav-tab-btn").forEach(btn => {
        btn.addEventListener("click", () => {
            document.querySelectorAll(".nav-tab-btn").forEach(b => b.classList.remove("active"));
            document.querySelectorAll(".tab-pane").forEach(p => p.classList.remove("active"));

            btn.classList.add("active");
            const targetPaneId = btn.getAttribute("data-tab").replace("tab-", "pane-");
            const targetPane = document.getElementById(targetPaneId);
            if (targetPane) {
                targetPane.classList.add("active");
            }

            // Lazy load charts when tabs open
            if (btn.getAttribute("data-tab") === "tab-spark-sql") {
                loadSparkSqlData();
            } else if (btn.getAttribute("data-tab") === "tab-ml-kmeans") {
                loadMlKmeansData();
            } else if (btn.getAttribute("data-tab") === "tab-streaming") {
                loadStreamingData();
            }
        });
    });

    // =========================================================================
    // 2. TERMINAL LOGGING & COMMANDS
    // =========================================================================
    function printTerm(text, className = "") {
        const line = document.createElement("div");
        line.className = `t-line ${className}`;
        line.textContent = text;
        terminalOutput.appendChild(line);
        terminalOutput.scrollTop = terminalOutput.scrollHeight;
    }

    async function executeStage(stageKey) {
        printTerm(`$ run-stage ${stageKey}`, "t-cmd");
        try {
            const res = await fetch(`/api/run-stage/${stageKey}`, { method: "POST" });
            const data = await res.json();
            if (data.output) {
                printTerm(data.output, data.success ? "t-green" : "t-red");
            }
            await refreshStatus();
        } catch (err) {
            printTerm(`[ERROR] Không thể kết nối đến server: ${err.message}`, "t-red");
        }
    }

    async function executeAll() {
        printTerm(`$ run-all (Bắt đầu chu trình tự động hóa 9 bước Pipeline)`, "t-cmd");
        try {
            const res = await fetch(`/api/run-all`, { method: "POST" });
            const data = await res.json();
            if (data.output) {
                printTerm(data.output, data.success ? "t-green" : "t-red");
            }
            await refreshStatus();
        } catch (err) {
            printTerm(`[ERROR] Lỗi thực thi pipeline: ${err.message}`, "t-red");
        }
    }

    function handleCommand(cmd) {
        cmd = cmd.trim();
        if (!cmd) return;

        if (cmd === "clear") {
            terminalOutput.innerHTML = "";
            return;
        }

        if (cmd === "help") {
            printTerm("$ help", "t-cmd");
            printTerm("--- DANH SÁCH LỆNH BIGDATA LAB TERMINAL ---", "t-cyan");
            printTerm(" run-stage hdfs_prepare   : Bước 1: Chuẩn bị HDFS Data Lake");
            printTerm(" run-stage upload_data    : Bước 2: Ingest dữ liệu thô vào raw");
            printTerm(" run-stage spark_read     : Bước 3: Đọc dữ liệu PySpark");
            printTerm(" run-stage spark_clean    : Bước 4: Feature engineering & Parquet");
            printTerm(" run-stage spark_sql      : Bước 5: Spark SQL 6 queries phân tích");
            printTerm(" run-stage ml_predict     : Bước 6: Random Forest & K-Means MLlib");
            printTerm(" run-stage save_results   : Bước 7: Xuất HDFS & Cảnh báo 3 cấp");
            printTerm(" run-stage kafka_stream   : Bước 8: Kafka streaming simulation");
            printTerm(" run-stage airflow_dag    : Bước 9: Airflow DAG Orchestration");
            printTerm(" run-all                  : Chạy liên hoàn toàn bộ 9 bước");
            printTerm(" clear                    : Xóa màn hình Terminal");
            return;
        }

        if (cmd === "run-all") {
            executeAll();
            return;
        }

        if (cmd.startsWith("run-stage ")) {
            const stageName = cmd.replace("run-stage ", "").trim();
            executeStage(stageName);
            return;
        }

        if (/^[1-9]$/.test(cmd)) {
            const numMap = {
                "1": "hdfs_prepare", "2": "upload_data", "3": "spark_read",
                "4": "spark_clean", "5": "spark_sql", "6": "ml_predict",
                "7": "save_results", "8": "kafka_stream", "9": "airflow_dag"
            };
            executeStage(numMap[cmd]);
            return;
        }

        printTerm(`$ ${cmd}`, "t-cmd");
        printTerm(`[ERROR] Lệnh '${cmd}' không được hỗ trợ. Gõ 'help' để xem danh sách.`, "t-red");
    }

    // Select Stage Card
    function selectStage(stageKey) {
        currentStage = stageKey;
        document.querySelectorAll(".pipeline-card").forEach(c => c.classList.remove("selected"));
        const card = document.getElementById(`card-${stageKey}`);
        if (card) card.classList.add("selected");

        const info = stageDetails[stageKey];
        if (info) {
            selectedTitle.textContent = info.num;
            selectedDesc.textContent = info.desc;
            termInput.value = info.cmd;
        }
    }

    document.querySelectorAll(".pipeline-card").forEach(card => {
        card.addEventListener("click", () => {
            const stage = card.getAttribute("data-stage");
            selectStage(stage);
        });
    });

    btnRunCurrentStage.addEventListener("click", () => executeStage(currentStage));
    btnRunAll.addEventListener("click", () => executeAll());
    btnTermRun.addEventListener("click", () => {
        const cmd = termInput.value;
        termInput.value = "";
        handleCommand(cmd);
    });

    termInput.addEventListener("keydown", (e) => {
        if (e.key === "Enter") {
            const cmd = termInput.value;
            termInput.value = "";
            handleCommand(cmd);
        }
    });

    btnClearTerm.addEventListener("click", () => {
        terminalOutput.innerHTML = "";
        printTerm("[SYSTEM] Màn hình đã được xóa sạch.", "t-cyan");
    });

    // Upload Dataset
    btnUpload.addEventListener("click", () => fileInput.click());
    fileInput.addEventListener("change", async () => {
        if (!fileInput.files || fileInput.files.length === 0) return;
        const file = fileInput.files[0];
        const formData = new FormData();
        formData.append("file", file);

        printTerm(`[UPLOADING] Đang nạp tệp '${file.name}' lên HDFS Data Lake...`, "t-cyan");
        try {
            const res = await fetch("/api/upload", { method: "POST", body: formData });
            const data = await res.json();
            printTerm(`[UPLOAD OK] ${data.message}`, "t-green");
            await refreshStatus();
        } catch (e) {
            printTerm(`[UPLOAD ERROR] ${e.message}`, "t-red");
        }
    });

    // Refresh status
    async function refreshStatus() {
        try {
            const res = await fetch("/api/status");
            const data = await res.json();

            for (const [stage, isDone] of Object.entries(data.steps || {})) {
                const checkEl = document.getElementById(`check-${stage}`);
                if (checkEl) {
                    if (isDone) checkEl.classList.add("completed");
                    else checkEl.classList.remove("completed");
                }
            }

            if (data.folders) {
                document.getElementById("badge-raw").textContent = `${data.folders.raw.count} file (${data.folders.raw.size_kb} KB)`;
                document.getElementById("badge-processed").textContent = `${data.folders.processed.count} file (${data.folders.processed.size_kb} KB)`;
                document.getElementById("badge-output").textContent = `${data.folders.output.count} files`;
            }
        } catch (e) {
            console.error("Lỗi cập nhật status:", e);
        }
    }

    // =========================================================================
    // 3. SPARK SQL 6 INTERACTIVE CHARTS
    // =========================================================================
    async function loadSparkSqlData() {
        try {
            const res = await fetch("/api/spark-sql/overview");
            const data = await res.json();

            if (data.kpis) {
                document.getElementById("kpi-total-employees").textContent = data.kpis.total_employees.toLocaleString();
                document.getElementById("kpi-attrition-rate").textContent = `${data.kpis.attrition_rate_percent}%`;
                document.getElementById("kpi-attrition-count").textContent = `${data.kpis.total_attrition} nhân viên đã rời đi`;
                document.getElementById("kpi-avg-income").textContent = `$${Math.round(data.kpis.avg_monthly_income_usd).toLocaleString()}`;
                document.getElementById("kpi-avg-age").textContent = `${data.kpis.avg_age} tuổi`;
                document.getElementById("kpi-avg-tenure").textContent = `${data.kpis.avg_years_at_company} năm`;
            }

            const q = data.queries || {};

            // Chart 1: OverTime (Doughnut)
            if (q.query_1 && q.query_1.data) {
                renderOverTimeChart(q.query_1.data);
            }

            // Chart 2: Department (Combined Bar + Line)
            if (q.query_2 && q.query_2.data) {
                renderDepartmentChart(q.query_2.data);
            }

            // Chart 3: JobRole (Horizontal Bar)
            if (q.query_3 && q.query_3.data) {
                renderJobRoleChart(q.query_3.data);
            }

            // Chart 4: WorkLifeBalance (Bar)
            if (q.query_4 && q.query_4.data) {
                renderWorkLifeChart(q.query_4.data);
            }

            // Chart 5: Tenure Buckets (Bar)
            if (q.query_5 && q.query_5.data) {
                renderTenureChart(q.query_5.data);
            }

            // Chart 6: Environment Satisfaction (Bar)
            if (q.query_6 && q.query_6.data) {
                renderEnvSatisfactionChart(q.query_6.data);
            }
        } catch (err) {
            console.error("Lỗi tải dữ liệu Spark SQL:", err);
        }
    }

    function createOrUpdateChart(canvasId, config) {
        if (chartInstances[canvasId]) {
            chartInstances[canvasId].destroy();
        }
        const ctx = document.getElementById(canvasId).getContext("2d");
        chartInstances[canvasId] = new Chart(ctx, config);
    }

    function renderOverTimeChart(data) {
        createOrUpdateChart("chart-overtime", {
            type: "doughnut",
            data: {
                labels: data.map(d => d.OverTime_Status),
                datasets: [{
                    data: data.map(d => d.Attrition_Rate_Percent),
                    backgroundColor: ["#ef4444", "#3b82f6"],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { position: "bottom", labels: { color: "#94a3b8", font: { family: "Outfit" } } },
                    tooltip: {
                        callbacks: {
                            label: (ctx) => ` Tỷ lệ nghỉ việc: ${ctx.raw}%`
                        }
                    }
                }
            }
        });
    }

    function renderDepartmentChart(data) {
        createOrUpdateChart("chart-department", {
            type: "bar",
            data: {
                labels: data.map(d => d.Department),
                datasets: [
                    {
                        label: "Tỷ lệ nghỉ việc (%)",
                        data: data.map(d => d.Attrition_Rate_Percent),
                        backgroundColor: "#8b5cf6",
                        borderRadius: 6,
                        yAxisID: "y"
                    },
                    {
                        label: "Thu nhập TB ($)",
                        data: data.map(d => d.Avg_Monthly_Income_USD),
                        type: "line",
                        borderColor: "#06b6d4",
                        borderWidth: 3,
                        pointBackgroundColor: "#06b6d4",
                        yAxisID: "y1"
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: { ticks: { color: "#94a3b8" }, grid: { display: false } },
                    y: { position: "left", ticks: { color: "#94a3b8" }, grid: { color: "rgba(255,255,255,0.05)" } },
                    y1: { position: "right", ticks: { color: "#06b6d4" }, grid: { display: false } }
                },
                plugins: {
                    legend: { labels: { color: "#94a3b8" } }
                }
            }
        });
    }

    function renderJobRoleChart(data) {
        createOrUpdateChart("chart-jobrole", {
            type: "bar",
            data: {
                labels: data.map(d => d.JobRole),
                datasets: [{
                    label: "Tỷ lệ nghỉ việc (%)",
                    data: data.map(d => d.Attrition_Rate_Percent),
                    backgroundColor: ["#ef4444", "#f97316", "#f59e0b", "#6366f1", "#3b82f6"],
                    borderRadius: 6
                }]
            },
            options: {
                indexAxis: "y",
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: { ticks: { color: "#94a3b8" }, grid: { color: "rgba(255,255,255,0.05)" } },
                    y: { ticks: { color: "#cbd5e1" }, grid: { display: false } }
                },
                plugins: { legend: { display: false } }
            }
        });
    }

    function renderWorkLifeChart(data) {
        createOrUpdateChart("chart-worklife", {
            type: "bar",
            data: {
                labels: data.map(d => d.WorkLifeBalance_Level),
                datasets: [{
                    label: "Tỷ lệ nghỉ việc (%)",
                    data: data.map(d => d.Attrition_Rate_Percent),
                    backgroundColor: ["#ef4444", "#f59e0b", "#3b82f6", "#10b981"],
                    borderRadius: 6
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: { ticks: { color: "#94a3b8" }, grid: { display: false } },
                    y: { ticks: { color: "#94a3b8" }, grid: { color: "rgba(255,255,255,0.05)" } }
                },
                plugins: { legend: { display: false } }
            }
        });
    }

    function renderTenureChart(data) {
        createOrUpdateChart("chart-tenure", {
            type: "bar",
            data: {
                labels: data.map(d => d.Tenure_Group),
                datasets: [{
                    label: "Tỷ lệ nghỉ việc (%)",
                    data: data.map(d => d.Attrition_Rate_Percent),
                    backgroundColor: "#ec4899",
                    borderRadius: 6
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: { ticks: { color: "#94a3b8" }, grid: { display: false } },
                    y: { ticks: { color: "#94a3b8" }, grid: { color: "rgba(255,255,255,0.05)" } }
                },
                plugins: { legend: { display: false } }
            }
        });
    }

    function renderEnvSatisfactionChart(data) {
        createOrUpdateChart("chart-env-satisfaction", {
            type: "bar",
            data: {
                labels: data.map(d => d.Env_Satisfaction_Level),
                datasets: [{
                    label: "Tỷ lệ nghỉ việc (%)",
                    data: data.map(d => d.Attrition_Rate_Percent),
                    backgroundColor: "#14b8a6",
                    borderRadius: 6
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: { ticks: { color: "#94a3b8" }, grid: { display: false } },
                    y: { ticks: { color: "#94a3b8" }, grid: { color: "rgba(255,255,255,0.05)" } }
                },
                plugins: { legend: { display: false } }
            }
        });
    }

    document.getElementById("btn-refresh-sql")?.addEventListener("click", () => {
        loadSparkSqlData();
    });

    // =========================================================================
    // 4. ML & K-MEANS DATA
    // =========================================================================
    async function loadMlKmeansData() {
        try {
            const res = await fetch("/api/ml/metrics");
            const data = await res.json();

            if (data.feature_importances) {
                createOrUpdateChart("chart-feature-importance", {
                    type: "bar",
                    data: {
                        labels: data.feature_importances.map(f => f.feature),
                        datasets: [{
                            label: "Mức độ ảnh hưởng (%)",
                            data: data.feature_importances.map(f => f.importance_percent),
                            backgroundColor: "#6366f1",
                            borderRadius: 6
                        }]
                    },
                    options: {
                        indexAxis: "y",
                        responsive: true,
                        maintainAspectRatio: false,
                        scales: {
                            x: { ticks: { color: "#94a3b8" }, grid: { color: "rgba(255,255,255,0.05)" } },
                            y: { ticks: { color: "#cbd5e1" }, grid: { display: false } }
                        },
                        plugins: { legend: { display: false } }
                    }
                });
            }
        } catch (e) {
            console.error("Lỗi tải ML Data:", e);
        }
    }

    // =========================================================================
    // 5. KAFKA LIVE STREAMING
    // =========================================================================
    const tickerList = document.getElementById("streaming-ticker-list");
    const streamCounter = document.getElementById("stream-event-counter");
    const btnStreamToggle = document.getElementById("btn-stream-toggle");
    const streamToggleText = document.getElementById("stream-toggle-text");
    const btnStreamSingle = document.getElementById("btn-stream-single");
    const highRiskTableBody = document.getElementById("high-risk-table-body");

    function renderStreamItem(item, prepend = true) {
        const div = document.createElement("div");
        div.className = "stream-event-item";
        div.innerHTML = `
            <div class="sei-left">
                <div class="sei-meta">${item.timestamp} • <strong>${item.employee_id}</strong> (${item.department})</div>
                <div class="sei-title">${item.event_type} - <span class="sei-desc">${item.description}</span></div>
            </div>
            <div class="sei-right">
                <div class="sei-risk-val" style="color: ${item.badge_color}">${item.current_risk_score}%</div>
                <div class="sei-tier-tag" style="background: ${item.badge_color}22; color: ${item.badge_color}">${item.alert_level}</div>
            </div>
        `;
        if (prepend && tickerList.firstChild) {
            tickerList.insertBefore(div, tickerList.firstChild);
        } else {
            tickerList.appendChild(div);
        }
    }

    async function pushSingleSimulatedEvent() {
        try {
            const res = await fetch("/api/streaming/simulate", { method: "POST" });
            const item = await res.json();
            renderStreamItem(item, true);
            const currentCount = tickerList.children.length;
            streamCounter.textContent = `${currentCount} events`;
        } catch (e) {
            console.error("Lỗi phát event:", e);
        }
    }

    async function loadStreamingData() {
        try {
            const res = await fetch("/api/streaming/latest");
            const events = await res.json();
            tickerList.innerHTML = "";
            events.forEach(item => renderStreamItem(item, false));
            streamCounter.textContent = `${events.length} events`;

            // Load high risk table
            const resHr = await fetch("/api/ml/high-risk-employees");
            const highRiskList = await resHr.json();
            highRiskTableBody.innerHTML = "";
            highRiskList.slice(0, 15).forEach(emp => {
                const tr = document.createElement("tr");
                tr.innerHTML = `
                    <td><strong>${emp.Employee_ID}</strong></td>
                    <td>${emp.Department}</td>
                    <td>${emp.JobRole}</td>
                    <td>$${Number(emp.MonthlyIncome).toLocaleString()}</td>
                    <td><span class="badge-pill" style="color: ${emp.OverTime === 'Yes' ? '#ef4444' : '#10b981'}">${emp.OverTime}</span></td>
                    <td><strong style="color: #ef4444">${emp.Risk_Score_Percent}%</strong></td>
                    <td><button class="btn-alert-hr" onclick="alert('Đã phát tín hiệu cảnh báo khẩn cấp tới Phòng Nhân sự (HR) cho nhân viên ${emp.Employee_ID}!')">Cảnh báo HR</button></td>
                `;
                highRiskTableBody.appendChild(tr);
            });
        } catch (e) {
            console.error("Lỗi tải dữ liệu streaming:", e);
        }
    }

    btnStreamSingle?.addEventListener("click", pushSingleSimulatedEvent);

    btnStreamToggle?.addEventListener("click", () => {
        isStreamingActive = !isStreamingActive;
        if (isStreamingActive) {
            streamToggleText.textContent = "Tạm dừng Streaming";
            btnStreamToggle.classList.add("danger");
            streamInterval = setInterval(pushSingleSimulatedEvent, 1200);
        } else {
            streamToggleText.textContent = "Bắt đầu Streaming";
            btnStreamToggle.classList.remove("danger");
            clearInterval(streamInterval);
        }
    });

    // =========================================================================
    // 6. AI RISK SIMULATOR
    // =========================================================================
    const inputAge = document.getElementById("input-age");
    const valAge = document.getElementById("val-age");
    const inputIncome = document.getElementById("input-income");
    const valIncome = document.getElementById("val-income");
    const btnOtYes = document.getElementById("btn-ot-yes");
    const btnOtNo = document.getElementById("btn-ot-no");
    const valOvertime = document.getElementById("val-overtime");
    const inputWlb = document.getElementById("input-wlb");
    const valWlb = document.getElementById("val-wlb");
    const inputYears = document.getElementById("input-years");
    const valYears = document.getElementById("val-years");
    const inputTotalYears = document.getElementById("input-total-years");
    const valTotalYears = document.getElementById("val-total-years");
    const btnRunSim = document.getElementById("btn-run-simulation");

    let currentOtValue = "Yes";

    inputAge?.addEventListener("input", () => valAge.textContent = `${inputAge.value} tuổi`);
    inputIncome?.addEventListener("input", () => valIncome.textContent = `$${Number(inputIncome.value).toLocaleString()}`);
    inputYears?.addEventListener("input", () => valYears.textContent = `${inputYears.value} năm`);
    inputTotalYears?.addEventListener("input", () => valTotalYears.textContent = `${inputTotalYears.value} năm`);
    inputWlb?.addEventListener("change", () => valWlb.textContent = inputWlb.options[inputWlb.selectedIndex].text);

    btnOtYes?.addEventListener("click", () => {
        currentOtValue = "Yes";
        btnOtYes.classList.add("active");
        btnOtNo.classList.remove("active");
        valOvertime.textContent = "CÓ (Yes)";
        valOvertime.className = "val-display text-amber";
    });

    btnOtNo?.addEventListener("click", () => {
        currentOtValue = "No";
        btnOtNo.classList.add("active");
        btnOtYes.classList.remove("active");
        valOvertime.textContent = "KHÔNG (No)";
        valOvertime.className = "val-display text-emerald";
    });

    async function runSimulatorInference() {
        const payload = {
            age: inputAge ? inputAge.value : 32,
            monthlyIncome: inputIncome ? inputIncome.value : 3500,
            overTime: currentOtValue,
            workLifeBalance: inputWlb ? inputWlb.value : 1,
            yearsAtCompany: inputYears ? inputYears.value : 1,
            totalWorkingYears: inputTotalYears ? inputTotalYears.value : 4
        };

        try {
            const res = await fetch("/api/ml/predict-risk", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload)
            });
            const data = await res.json();

            const scoreDisplay = document.getElementById("sim-score-display");
            const tierBadge = document.getElementById("sim-tier-badge");
            const recList = document.getElementById("sim-recommendations-list");

            if (scoreDisplay) {
                scoreDisplay.textContent = `${data.riskScorePercent}%`;
                scoreDisplay.style.color = data.badgeColor;
            }

            if (tierBadge) {
                tierBadge.textContent = data.alertTier;
                tierBadge.style.color = data.badgeColor;
                tierBadge.style.borderColor = data.badgeColor;
                tierBadge.style.backgroundColor = `${data.badgeColor}22`;
            }

            if (recList && data.recommendations) {
                recList.innerHTML = "";
                data.recommendations.forEach(r => {
                    const li = document.createElement("li");
                    li.textContent = r;
                    recList.appendChild(li);
                });
            }
        } catch (e) {
            console.error("Lỗi chạy simulator:", e);
        }
    }

    btnRunSim?.addEventListener("click", runSimulatorInference);

    // Initial status setup
    selectStage("hdfs_prepare");
    refreshStatus();
});
