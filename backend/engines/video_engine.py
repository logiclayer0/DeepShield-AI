import cv2
import numpy as np
import tempfile
import os

def process_video_analysis(video_bytes: bytes) -> tuple[float, str]:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
        temp_video.write(video_bytes)
        temp_path = temp_video.name

    cap = cv2.VideoCapture(temp_path)
    frame_count = 0
    frame_diffs = []
    prev_frame = None

    while cap.isOpened() and frame_count < 100:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, (320, 240))

        if prev_frame is not None:
            diff = cv2.absdiff(prev_frame, gray)
            frame_diffs.append(np.mean(diff))

        prev_frame = gray
        frame_count += 1

    cap.release()
    os.remove(temp_path)

    if not frame_diffs:
        return 50.0, "Inconclusive Video Data"

    diff_std = np.std(frame_diffs)
    
    if diff_std < 1.5:
        anomaly_score = 45.0
    elif diff_std > 25.0:
        anomaly_score = 35.0
    else:
        anomaly_score = 10.0

    authenticity_score = max(0.0, round(100.0 - anomaly_score, 2))
    status = "Authentic Video" if authenticity_score > 70 else "Deepfake / Manipulated Video"

    return authenticity_score, status