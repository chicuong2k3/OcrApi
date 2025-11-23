import easyocr

reader = easyocr.Reader(['en']) 

def run_ocr(image_path: str):
    try:
        results = reader.readtext(image_path)
    except Exception as e:
        print("OCR error:", e)
        return ""

    texts = []
    for _, text, conf in results:
        text = text.strip()
        if text:
            texts.append(text)

    return "\n".join(texts)
