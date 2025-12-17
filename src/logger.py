import csv
from datetime import datetime

def log_event(label, conf):
    with open('trail_log.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), label, f"{conf:.2f}"])