import os

# 1. Update AppServiceProvider.php
asp_path = r'C:\laragon\www\doan_banhngot\app\Providers\AppServiceProvider.php'
with open(asp_path, 'r', encoding='utf-8') as f:
    content = f.read()

if 'Paginator::useBootstrapFive' not in content:
    content = content.replace(
        'use Illuminate\\Support\\ServiceProvider;',
        'use Illuminate\\Support\\ServiceProvider;\nuse Illuminate\\Pagination\\Paginator;'
    )
    content = content.replace(
        'public function boot(): void\n    {',
        'public function boot(): void\n    {\n        Paginator::useBootstrapFive();'
    )
    with open(asp_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('[OK] AppServiceProvider updated with Paginator::useBootstrapFive()')
else:
    print('[SKIP] AppServiceProvider already configured')

# 2. Update ProductController.php
pc_path = r'C:\laragon\www\doan_banhngot\app\Http\Controllers\Client\ProductController.php'
with open(pc_path, 'r', encoding='utf-8') as f:
    pc_content = f.read()

if '$query->get()' in pc_content:
    pc_content = pc_content.replace(
        '$products = $query->get();',
        '$products = $query->paginate(8)->withQueryString();'
    )
    with open(pc_path, 'w', encoding='utf-8') as f:
        f.write(pc_content)
    print('[OK] ProductController updated with paginate(8)')
else:
    print('[SKIP] ProductController already paginated or query->get not found')

# 3. Update products.blade.php
blade_path = r'C:\laragon\www\doan_banhngot\resources\views\client\products.blade.php'
with open(blade_path, 'r', encoding='utf-8') as f:
    blade_content = f.read()

if '{{ $products->links() }}' not in blade_content:
    target = '@endforelse\n    </div>\n</div>'
    replacement = '''@endforelse
    </div>

    {{-- Thanh phân trang Pagination Bootstrap 5 --}}
    @if($products->hasPages())
        <div class="d-flex justify-content-center mt-5 mb-4">
            {{ $products->links() }}
        </div>
    @endif
</div>'''
    if target in blade_content:
        blade_content = blade_content.replace(target, replacement)
    else:
        # try CRLF
        target_crlf = '@endforelse\r\n    </div>\r\n</div>'
        blade_content = blade_content.replace(target_crlf, replacement.replace('\n', '\r\n'))
    with open(blade_path, 'w', encoding='utf-8') as f:
        f.write(blade_content)
    print('[OK] products.blade.php updated with pagination links')
else:
    print('[SKIP] products.blade.php already has pagination links')
