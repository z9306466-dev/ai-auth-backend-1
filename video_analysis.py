import cv2
import numpy as np

def analyze_video(path):
    cap = cv2.VideoCapture(path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frames.append(np.mean(gray))
    cap.release()

    variance = np.var(frames)
    if variance < 200:
        return "AI Generated", 83
    return "Real", 75
