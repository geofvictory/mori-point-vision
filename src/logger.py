import csv
import os
from datetime import datetime


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