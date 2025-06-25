# Face Anonymizer

This project is a **Level 1** implementation: a simple, Dockerized Python tool that reads a video file, detects faces using OpenCV’s Haar Cascade, applies a blur to anonymize them, and displays the result in real-time.

---

## 🔧 Build the Docker Image

```bash
docker build -t face-anonymizer .
```

---

## ▶️ Run the Anonymizer

```bash
docker run --rm -it \
  -v "$(pwd)":/app \
  face-anonymizer input.mp4
```

* **`-v "$(pwd)":/app`** mounts your current directory (containing the input video) into the container.
* Replace `input.mp4` with the path to your video file.
* Press **`q`** in the display window to stop playback and exit.

---

## 🧩 Project Structure

```
face_anonymizer/
├── Dockerfile
├── entrypoint.sh
├── requirements.txt
├── anonymize.py
└── README.md
```

---

## ⚙️ How It Works

1. **Reads video** – via OpenCV (`cv2.VideoCapture`).
2. **Detects faces** – using Haar Cascade (`cv2.CascadeClassifier`).
3. **Blurs faces** – through `cv2.GaussianBlur`.
4. **Displays output** – real-time feed with blurred faces.
