import csv
import os
from datetime import datetime


class MoriLogger:
    """Logger class for tracking detections and performance metrics"""
    
    def __init__(self, detection_file='trail_log.csv', performance_file='performance_metrics.csv'):
        self.detection_file = detection_file
        self.performance_file = performance_file
        
        # Initialize detection file with header if it doesn't exist
        if not os.path.isfile(detection_file):
            with open(detection_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['timestamp', 'label', 'confidence'])
        
        # Initialize performance file with header if it doesn't exist
        if not os.path.isfile(performance_file):
            with open(performance_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['timestamp', 'latency_ms', 'fps', 'device'])
    
    def log_detection(self, label, conf):
        """Log detection events to CSV"""
        with open(self.detection_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now().isoformat(), label, f"{conf:.2f}"])
    
    def log_performance(self, latency, fps, device):
        """Log performance metrics to CSV"""
        with open(self.performance_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                datetime.now().isoformat(),
                f"{latency:.2f}",
                f"{fps:.2f}",
                device
            ])


def log_event(label, conf):
    """Log detection events to trail_log.csv"""
    with open('trail_log.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), label, f"{conf:.2f}"])


def log_performance(latency, fps, device):
    """Log performance metrics to performance_metrics.csv"""
    csv_file = 'performance_metrics.csv'
    
    # Write header if file doesn't exist
    file_exists = os.path.isfile(csv_file)
    
    with open(csv_file, 'a', newline='') as f:
        writer = csv.writer(f)
        
        # Write header on first run
        if not file_exists:
            writer.writerow(['timestamp', 'latency_ms', 'fps', 'device'])
        
        # Write performance data
        writer.writerow([
            datetime.now().isoformat(),
            f"{latency:.2f}",
            f"{fps:.2f}",
            device
        ])