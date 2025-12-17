from ultralytics import YOLO

class MoriVision:
    def __init__(self):
        # Using yolo11n for maximum inference speed
        self.model = YOLO("yolo11n.pt") 

    def process_frame(self, frame):
        # stream=True optimizes memory for live video
        results = self.model(frame, stream=True, conf=0.4)
        return results