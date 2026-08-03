import librosa
import numpy as np
import io

def process_audio_analysis(audio_bytes: bytes) -> tuple[float, str]:
    audio_buffer = io.BytesIO(audio_bytes)
    y, sr = librosa.load(audio_buffer, sr=None)
    
    spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
    centroid_std = np.std(spectral_centroids)
    
    zero_crossings = librosa.zero_crossings(y, pad=False)
    zcr_mean = np.mean(zero_crossings)
    
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfcc_var = np.var(mfcc)
    
    anomaly_score = 0
    if centroid_std < 500:
        anomaly_score += 40
    if zcr_mean < 0.02 or zcr_mean > 0.2:
        anomaly_score += 30
    if mfcc_var < 50:
        anomaly_score += 30
        
    authenticity_score = max(0.0, round(100.0 - anomaly_score, 2))
    
    if authenticity_score > 70:
        status = "Human Voice"
    else:
        status = "AI Cloned / Synthetic Audio"
        
    return authenticity_score, status