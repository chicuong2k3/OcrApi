from paddleocr import PaddleOCR

# Load PaddleOCR lite model
ocr = PaddleOCR(
    use_angle_cls=True, 
    lang='en'  
)

def run_ocr(image_path: str):
    result = ocr.ocr(image_path, cls=True)

    lines = []
    for block in result:
        for line in block:
            text = line[1][0].strip()
            if text:
                lines.append(text)

    return lines
