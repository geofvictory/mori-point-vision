
# Mori Point Vision ✅

**Lightweight vision utilities and YOLO-based detection tools for live/recorded streams.**

This repository contains a small set of utilities and an example app to run object detection on video streams or files using OpenCV and Ultralytics (YOLO).

---

## 🔧 Features
- **GPU-accelerated inference**: Auto-detects Apple Silicon (MPS) or CUDA; falls back to CPU
- **Frame skipping**: Process every Nth frame to reduce CPU load while maintaining smooth playback
- **Performance monitoring**: Track latency and FPS in real-time with rolling averages
- **CSV metrics export**: Log inference times and device info to `performance_metrics.csv`
- **Detection logging**: Log each detected object (class, confidence, timestamp) to `trail_log.csv`
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

3. Run the example app:

```bash
python src/main.py
```

Press `q` to quit. The app processes the Mori Point live stream (hardcoded in `main.py`). To use a different stream, edit the `url` variable in `src/main.py`.

### Quick Connectivity Check

Before running the full pipeline, test if your stream connection works:

```bash
python test_connection.py
```

This displays raw frames without inference overhead — useful for diagnosing stream issues.

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

### Detection Logging
Detections are automatically logged to `trail_log.csv` with the following columns:
- `timestamp`: ISO format datetime when detection occurred
- `label`: Class name of detected object
- `confidence`: Detection confidence score (0.00–1.00)

The logger is initialized in `main.py` and automatically logs each detection:
```python
from src.logger import MoriLogger

logger = MoriLogger()  # Creates trail_log.csv
logger.log_detection(class_name, confidence_score)  # Log each detection
```

### Customization
Edit `src/main.py` to adjust:
- **Stream URL**: Change `url` variable to point to your stream
- **Model weights**: Use different YOLO models (yolo11s.pt, yolo11m.pt, etc.)
- **Confidence threshold**: Adjust `conf` parameter in `engine.py`
- **Frame skip rate**: Tune `process_every_n_frames`

## 📁 Project Structure

```
src/
  main.py           → App entry point; stream/file processing
  engine.py         → MoriVision class; YOLO inference + metrics
  performance.py    → PerformanceMonitor; latency tracking
  logger.py         → MoriLogger class; CSV logging for detections and performance metrics
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

## 🧪 Development & Testing

### Running the Full Pipeline

```bash
python src/main.py
```

Monitor performance in real-time:
- **Display overlay**: Latency (ms) and FPS shown on each frame
- **Metrics export**: Check `performance_metrics.csv` after running for historical analysis

### Testing & Diagnostics

**Stream connectivity test** (no inference):
```bash
python test_connection.py
```

**Performance analysis**:
```python
from src.performance import PerformanceMonitor
from src.engine import MoriVision

ai = MoriVision()
stats = ai.get_performance_stats()
print(stats)  # View avg latency, FPS, sample count
```

### Code Quality

- Add tests under a `tests/` directory and run with `pytest`
- Use code formatting: `black src/`
- Use linting: `ruff check src/`
- Consider `pre-commit` hooks for automated checks

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

