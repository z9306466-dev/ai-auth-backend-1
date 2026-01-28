import librosa
import numpy as np
import random

def analyze_audio(path):
    y, sr = librosa.load(path, sr=None)
    
    # استخراج الميزات الصوتية المختلفة
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    spectral_contrast = librosa.feature.spectral_contrast(y=y, sr=sr)
    
    # حساب تباين الميزات الصوتية المختلفة
    mfcc_var = np.var(mfcc)
    chroma_var = np.var(chroma)
    spectral_contrast_var = np.var(spectral_contrast)
    
    # حساب مجموع تباين الميزات
    score = mfcc_var + chroma_var + spectral_contrast_var
    
    # زيادة العشوائية في النتيجة
    random_variation = random.randint(-50, 50)
    score += random_variation
    
    # تعديل النتيجة بناءً على العشوائية
    if score < 120:  # عشوائية كبيرة هنا
        result = "AI Generated"
        confidence = 90 + random.randint(-30, 30)  # عشوائية قوية في الثقة
    else:
        result = "Real"
        confidence = 80 + random.randint(-30, 30)  # عشوائية كبيرة ولكن دقة بسيطة
    
    return result, confidence
