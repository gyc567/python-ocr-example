try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
    tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
    # Example config: '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
    # It's important to include double quotes around the dir path.

    #text=    pytesseract.image_to_string( Image.open(r"D:\tools\OCR\poc\python-ocr-example\images\ocr_example_1.png"), lang='eng', config=tessdata_dir_config)
    text=    pytesseract.image_to_string( Image.open(filename), lang='eng', config=tessdata_dir_config)
   # text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

print(ocr_core('images/ocr_example_1.png'))