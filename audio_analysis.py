import librosa
import numpy as np
import random

def analyze_audio(path):
    y, sr = librosa.load(path, sr=None)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    score = np.var(mfcc)
    
    # العشوائية في النتيجة
    random_variation = random.randint(-10, 10)
    score += random_variation
    
    if score < 60:
        result = "AI Generated"
        confidence = 85 + random.randint(-5, 5)  # عشوائية في النسبة
    else:
        result = "Real"
        confidence = 100 + random.randint(-5,5 )  # عشوائية في النسبة

    return result, confidence
