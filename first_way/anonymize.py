import cv2
import sys


def anonymize(input_path):
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml",
    )
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print("Error: couldn't open video.")
        sys.exit(1)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))
        for x, y, w, h in faces:
            roi = frame[y : y + h, x : x + w]
            frame[y : y + h, x : x + w] = cv2.GaussianBlur(roi, (23, 23), 30)
        cv2.imshow("Blurred Faces", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    video = sys.argv[1] if len(sys.argv) > 1 else "input.mp4"
    anonymize(video)
