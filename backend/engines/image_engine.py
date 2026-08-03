import cv2
import numpy as np
from PIL import Image, ImageChops, ImageEnhance
import io

def process_image_ela(image_bytes: bytes, quality: int = 90) -> tuple[bytes, float]:
    """
    Error Level Analysis (ELA) runs on an image to detect forgery/tampering.
    Returns: (Heatmap image bytes, Authenticity score)
    """
    original = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    
    buffer = io.BytesIO()
    original.save(buffer, 'JPEG', quality=quality)
    buffer.seek(0)
    resaved = Image.open(buffer)
    
    ela_image = ImageChops.difference(original, resaved)
    
    extrema = ela_image.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    if max_diff == 0:
        max_diff = 1
    
    scale = 255.0 / max_diff
    ela_image = ImageEnhance.Brightness(ela_image).enhance(scale)
    
    ela_np = np.array(ela_image)
    mean_diff = np.mean(ela_np)
    
    forgery_risk = min(100.0, float(mean_diff * 4.5))
    authenticity_score = max(0.0, round(100.0 - forgery_risk, 2))
    
    output_buffer = io.BytesIO()
    ela_image.save(output_buffer, format='PNG')
    heatmap_bytes = output_buffer.getvalue()
    
    return heatmap_bytes, authenticity_score