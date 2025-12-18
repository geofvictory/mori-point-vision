from ultralytics import YOLO
import torch
from performance import PerformanceMonitor


class MoriVision:
    def __init__(self):
        # Check if Apple Silicon GPU (MPS) is available
        self.device = 'mps' if torch.backends.mps.is_available() else 'cpu'
        print(f"Using device: {self.device}")
        
        # Using yolo11n for maximum inference speed
        self.model = YOLO("yolo11n.pt")
        self.model.to(self.device)  # Move model to GPU/MPS
        
        # Performance monitoring
        self.monitor = PerformanceMonitor()

    def process_frame(self, frame):
        """Process a frame and return results with latency metrics."""
        self.monitor.start_timer()
        
        # stream=True optimizes memory for live video
        results = self.model(frame, stream=True, conf=0.4, device=self.device)
        
        # Record latency immediately after inference
        latency = self.monitor.stop_timer()
        
        return results, latency