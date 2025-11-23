from paddleocr import PaddleOCR

# Load PaddleOCR lite model
ocr = PaddleOCR(
    use_angle_cls=True, 
    lang='en'  
)

def run_ocr(image_path: str):
    result = ocr.ocr(image_path)
    texts = [line[1][0] for line in result]  
    return [t.strip() for t in texts if t.strip()]
