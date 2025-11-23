from paddleocr import PaddleOCR

# Load PaddleOCR model
ocr = PaddleOCR(
    use_angle_cls=True,
    lang='en'
)

def run_ocr(image_path: str):
    result = ocr.ocr(image_path)
    texts = []

    for line in result:
        if len(line) >= 2 and len(line[1]) >= 1:
            texts.append(line[1][0])
    return [t.strip() for t in texts if t.strip()]
