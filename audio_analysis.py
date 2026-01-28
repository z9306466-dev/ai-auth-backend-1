import cv2
import numpy as np
import random

def analyze_video(path):
    # فتح الفيديو
    cap = cv2.VideoCapture(path)
    frames = 0
    score = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # تحليل الإطار (Frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        score += np.var(gray)
        frames += 1

    cap.release()
    
    # حساب متوسط النتيجة بعد تحليل الفيديو بالكامل
    score /= frames

    # العشوائية في النتيجة
    random_variation = random.randint(-10, 10)
    score += random_variation
    
    if score < 200:
        result = "AI Generated"
        confidence = 85 + random.randint(-5, 5)  # عشوائية في النسبة
    else:
        result = "Real"
        confidence = 78 + random.randint(-5, 5)  # عشوائية في النسبة

    return result, confidence
