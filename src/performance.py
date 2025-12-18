import time
import numpy as np


class PerformanceMonitor:
    """Tracks inference latency and FPS metrics in real-time."""
    
    def __init__(self):
        self.inference_times = []
        self.start_time = None

    def start_timer(self):
        """Start the performance timer."""
        self.start_time = time.perf_counter()

    def stop_timer(self):
        """Stop the timer and record latency (in ms)."""
        if self.start_time:
            latency = (time.perf_counter() - self.start_time) * 1000  # Convert to ms
            self.inference_times.append(latency)
            # Keep only the last 100 readings for a rolling average
            if len(self.inference_times) > 100:
                self.inference_times.pop(0)
            return latency
        return 0

    def get_avg_latency(self):
        """Return average inference latency (ms) over recent samples."""
        return np.mean(self.inference_times) if self.inference_times else 0

    def get_fps(self, latency_ms):
        """Calculate FPS from latency in milliseconds."""
        return 1000 / latency_ms if latency_ms > 0 else 0

    def get_stats(self):
        """Return a dict with current performance stats."""
        avg_latency = self.get_avg_latency()
        return {
            "avg_latency_ms": avg_latency,
            "fps": self.get_fps(avg_latency),
            "samples": len(self.inference_times),
        }
