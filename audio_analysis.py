import librosa
import numpy as np

def analyze_audio(path):
    y, sr = librosa.load(path, sr=None)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    score = np.var(mfcc)

    if score < 60:
        return "AI Generated", 85
    return "Real", 78
