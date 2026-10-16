import { Controller, Get, Post } from '@nestjs/common';
import { StreamingService } from './streaming.service';

@Controller('api/streaming')
export class StreamingController {
  constructor(private readonly streamService: StreamingService) {}

  @Get('latest')
  getLatestEvents() {
    return this.streamService.getLatestEvents();
  }

  @Post('simulate')
  generateEvent() {
    return this.streamService.generateSimulatedEvent();
  }
}
