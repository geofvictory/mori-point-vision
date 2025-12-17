
# Mori Point Vision ✅

**Lightweight vision utilities and YOLO-based detection tools for live/recorded streams.**

This repository contains a small set of utilities and an example app to run object detection on video streams or files using OpenCV and Ultralytics (YOLO).

---

## 🔧 Features
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

## 🛠 Configuration

- Edit configuration values or pass CLI flags to control model weights, confidence thresholds, and input source.
- Recommended: store model paths and runtime options in a small YAML or JSON file and load them in `src/main.py` for reproducible runs.

Example CLI flags (implemented in `src/main.py`):

```text
--source    path or stream URL to process
--weights   path/to/weights.pt
--conf      confidence threshold (0.0 - 1.0)
```

---

## 🧪 Development

- Add tests under a `tests/` directory and run with `pytest`.
- Use code formatting and linting tools (e.g., `black`, `ruff`) and add a `requirements-dev.txt` or `pyproject.toml` if needed.
- Consider `pre-commit` hooks for formatting and checks.

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

