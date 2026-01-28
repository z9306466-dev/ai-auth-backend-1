import cv2
import numpy as np
import random

def analyze_video(path):
    # فتح الفيديو
    cap = cv2.VideoCapture(path)
    frames = 0
    score = 0
    frame_diffs = []  # لحفظ التباين بين الإطارات
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # تحويل الإطار إلى صورة رمادية
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # إضافة التباين بين الإطارات
        if frames > 0:
            diff = np.var(gray - prev_gray)  # حساب التباين بين الإطار الحالي والإطار السابق
            frame_diffs.append(diff)
        
        prev_gray = gray
        frames += 1
    
    cap.release()
    
    # حساب متوسط التباين بين الإطارات
    avg_diff = np.mean(frame_diffs) if frame_diffs else 0
    score = avg_diff
    
    # زيادة العشوائية في النتيجة
    random_variation = random.randint(-50, 50)
    score += random_variation
    
    # تعديل النتيجة بناءً على العشوائية
    if score < 100:  # عشوائية قوية هنا
        result = "AI Generated"
        confidence = 90 + random.randint(-40, 40)  # عشوائية قوية للثقة
    else:
        result = "Real"
        confidence = 80 + random.randint(-40, 40)  # عشوائية عالية ولكن مع بعض الدقة
    
    return result, confidence
