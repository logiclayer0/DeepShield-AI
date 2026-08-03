# 🛡️ DeepShield AI — Multi-Modal Cyber Forensics & Deepfake Detection Engine

**DeepShield AI** is a state-of-the-art cyber forensics platform built to detect AI-generated synthetic media, voice clones, and deepfake manipulations. It leverages specialized algorithmic pipelines (Error Level Analysis, Spectral Acoustic Extraction, and Temporal Optical Flow) to provide detailed authenticity scores and real-time forensic reports.

---

## 🚀 Key Forensic Capabilities

### 🖼️ Image Error Level Analysis (ELA) Engine
* Detects image manipulation by re-compressing the frame and highlighting statistical visual variance.
* Identifies local high-frequency anomalies caused by generative AI tools, copy-move forgery, or pixel splicing.

### 🎙️ Acoustic Voice Clone Detector
* Extracts **Mel-Frequency Cepstral Coefficients (MFCCs)**, spectral centroid, and zero-crossing rates.
* Identifies synthetic speech characteristics and TTS (Text-to-Speech) generative voice clones with high precision.

### 🎥 Video Temporal Anomaly Detection Engine
* Analyzes frame-by-frame structural differences to track artificial facial motion and unnatural blinking frequencies.
* Identifies video deepfakes generated through frame-stitching and AI face-swapping algorithms.

---

## 🛠️ System Architecture & Tech Stack

| Layer | Technologies Used |
| :--- | :--- |
| **Frontend UI** | Next.js 14, React 18, Tailwind CSS, Lucide Icons |
| **Backend API** | Python 3.11+, FastAPI, Uvicorn, CORS Middleware |
| **Forensic Engines** | OpenCV, Librosa, NumPy, SciPy, Pillow, Matplotlib |

---

## 💻 Local Setup & Installation

### 1. Backend API Service
```bash
# Navigate to backend directory
cd backend

# Install dependencies
pip install -r requirements.txt

# Launch FastAPI Server
uvicorn main:app --reload