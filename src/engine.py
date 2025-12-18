from ultralytics import YOLO
import torch

class MoriVision:
    def __init__(self):
        # Check if Apple Silicon GPU (MPS) is available
        self.device = 'mps' if torch.backends.mps.is_available() else 'cpu'
        print(f"Using device: {self.device}")
        
        # Using yolo11n for maximum inference speed
        self.model = YOLO("yolo11n.pt")
        self.model.to(self.device)  # Move model to GPU/MPS

    def process_frame(self, frame):
        # stream=True optimizes memory for live video
        results = self.model(frame, stream=True, conf=0.4, device=self.device)
        return results