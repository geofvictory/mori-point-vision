"""
Test script to verify connectivity to Mori Point live stream.
Displays raw frames without any YOLO inference for quick diagnostics.
"""

import cv2
import streamlink


def test_connection():
    """Connect to Mori Point stream and display raw frames."""
    # Mori Point Live Stream URL
    url = "https://www.youtube.com/live/P79O4t4r6dU"
    
    print("Connecting to Mori Point...")
    try:
        # 1. Use streamlink to find the actual stream URL
        streams = streamlink.streams(url)
        
        # We'll use 720p to save bandwidth and CPU during testing
        video_url = streams['720p'].url
        print(f"✓ Stream found: {streams.keys()}")
        
        # 2. Open the video capture
        cap = cv2.VideoCapture(video_url)
        
        if not cap.isOpened():
            print("✗ Failed to open video capture.")
            return
        
        print("✓ Connection successful! Press 'q' to close the window.")
        
        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                print("✗ Failed to grab frame.")
                break
            
            frame_count += 1
            
            # 3. Show the frame
            cv2.imshow('Mori Point Connectivity Test', frame)
            
            # Print frame info every 30 frames
            if frame_count % 30 == 0:
                h, w = frame.shape[:2]
                print(f"  Frames received: {frame_count} | Resolution: {w}x{h}")
            
            # Press 'q' to quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print(f"✓ Test completed. Total frames: {frame_count}")
                break
                
        cap.release()
        cv2.destroyAllWindows()
        
    except KeyError:
        print("✗ Error: Stream quality not available. Available streams:", streams.keys())
    except Exception as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    test_connection()
