
# Mori Point Vision ✅

**Lightweight vision utilities and YOLO-based detection tools for live/recorded streams.**

This repository contains a small set of utilities and an example app to run object detection on video streams or files using OpenCV and Ultralytics (YOLO).

---

## 🔧 Features
- **GPU-accelerated inference**: Auto-detects Apple Silicon (MPS) or CUDA; falls back to CPU
- **Frame skipping**: Process every Nth frame to reduce CPU load while maintaining smooth playback
- **Performance monitoring**: Track latency and FPS in real-time with rolling averages
- **CSV metrics export**: Log inference times and device info to `performance_metrics.csv`
- Run YOLO detection on camera / file / stream inputs
- Stream handling via `streamlink` and `ffmpeg` integration
- Simple logging and engine components under `src/` for easy extension

---

## ⚡ Quickstart

1. Clone the repo:

```bash
git clone https://github.com/geofvictory/mori-point-vision.git
cd mori-point-vision
```

2. Install runtime dependencies:

```bash
python -m pip install -r requirements.txt
```

3. Run the example app (uses `src/main.py`):

```bash
python -m src.main --source 0              # run on default webcam
python -m src.main --source path/to/video.mp4
python -m src.main --source "rtsp://..."  # run on RTSP stream
```

Check `src/main.py` and `src/engine.py` to see how the inputs are handled and how detections are produced and logged.

---

## 🛠 Configuration & Performance Tuning

### GPU Acceleration
The engine automatically detects and uses:
- **Apple Silicon (M1/M2/M3)**: Metal Performance Shaders (MPS) for 5–10x faster inference
- **NVIDIA GPU**: CUDA (if PyTorch is built with CUDA support)
- **CPU**: Fallback if no GPU detected

### Frame Skipping
Reduce CPU usage by processing every Nth frame. Edit `src/main.py`:

```python
process_every_n_frames = 5    # Process every 5th frame (default)
# or
process_every_n_frames = 10   # For 50% lower CPU usage
```

### Performance Metrics
Metrics are logged to `performance_metrics.csv` with the following columns:
- `timestamp`: ISO format datetime
- `latency_ms`: Inference time in milliseconds
- `fps`: Estimated frames per second
- `device`: Hardware used (mps, cuda, cpu)

View live stats:
```python
from src.performance import PerformanceMonitor
stats = perf_monitor.get_stats()
print(f"Avg Latency: {stats['avg_latency_ms']:.2f}ms")
print(f"FPS: {stats['fps']:.1f}")
```

### CLI Configuration
Edit `src/main.py` to adjust model, confidence, and input source.

Example configuration:
```text
--source    path or stream URL to process
--weights   path/to/weights.pt (e.g., yolo11n.pt, yolo11m.pt)
--conf      confidence threshold (0.0 - 1.0)
```

## 📁 Project Structure

```
src/
  main.py           → App entry point; stream/file processing
  engine.py         → MoriVision class; YOLO inference + metrics
  performance.py    → PerformanceMonitor; latency tracking
  logger.py         → CSV logging for events and metrics
requirements.txt    → Runtime dependencies
README.md           → This file
```

---

## 🏗 Architecture Highlights

### Decoupled Telemetry Module
A standalone `performance.py` module provides **high-resolution performance profiling** (Inference Latency & Throughput) without injecting overhead into the core vision engine. This architecture enables:
- Clean separation of concerns: inference logic isolated from metrics collection
- Zero impact on detection speed: performance tracking runs independently
- Real-time metrics export: CSV logging of latency, FPS, and hardware device
- Extensibility: Easy to add custom metrics or swap logging backends

---

## 🧪 Development

---

## 📦 Requirements

See `requirements.txt` for runtime dependencies. If you need GPU-enabled PyTorch, install the correct `torch` wheel for your CUDA version from https://pytorch.org.

---

## 🤝 Contributing

Contributions are welcome — open an issue or submit a PR. Please include small, focused changes and a short description of the reasoning.

---

## 📜 License

Add a `LICENSE` file to declare the project license (e.g., MIT). For now this repository is unlicensed.

---

## Contact

Maintainer: geofreyvictory (GitHub)

---

Feel free to tell me any details you'd like added (examples, badges, model weights, example outputs) and I can update the README accordingly. ✨

