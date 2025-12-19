import cv2
import streamlink
from .engine import MoriVision
from .logger import MoriLogger
from .performance import PerformanceMonitor

def run():
    url = "https://www.youtube.com/live/P79O4t4r6dU"
    streams = streamlink.streams(url)
    cap = cv2.VideoCapture(streams['720p'].url)
    ai = MoriVision()
    logger = MoriLogger()
    perf = PerformanceMonitor()

    # Frame skipping configuration
    frame_count = 0
    process_every_n_frames = 5  # Process every 5th frame; increase to 10 for lower CPU
    last_annotated_frame = None

    while True:
        ret, frame = cap.read()
        if not ret: 
            break

        frame_count += 1
        
        # Run inference on designated frames only
        if frame_count % process_every_n_frames == 0:
            perf.start_timer()
            results, latency = ai.process_frame(frame)
            latency = perf.stop_timer()
            print(f"FPS: {perf.get_fps(latency):.1f}")
            
            for r in results:
                last_annotated_frame = r.plot()
                if results:
                    for box in r.boxes:
                        logger.log_detection(r.names[int(box.cls[0])], float(box.conf[0]))
        
        # Display the most recent annotated frame (or raw frame if no inference yet)
        display_frame = last_annotated_frame if last_annotated_frame is not None else frame
        cv2.imshow('Mori-Point-Vision', display_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()