import cv2
import streamlink
from engine import MoriVision

def run():
    url = "https://www.youtube.com/live/P79O4t4r6dU"
    streams = streamlink.streams(url)
    cap = cv2.VideoCapture(streams['720p'].url)
    ai = MoriVision()

    while True:
        ret, frame = cap.read()
        if not ret: break

        # Process every 5th frame to save CPU (Frame Skipping)
        results = ai.process_frame(frame)
        
        for r in results:
            cv2.imshow('Mori-Point-Vision', r.plot())

        if cv2.waitKey(1) & 0xFF == ord('q'): break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()