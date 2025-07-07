from PIL import Image
import os
import pytesseract
import easyocr
import fitz
# Path to pytesseract executable
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# --- Loop over all images within folder ---

# get directory name as string
directory = os.getcwd()

# loop over all files within directory, saving the filenames as a string under variable 'filename'
for root, dirs, files in os.walk("."):
    for filename in files:
        # check whether extension of the file is 'jpg' or 'jpeg'
        if filename.split(sep='.')[1] == 'jpg' or filename.split(sep='.')[1] == 'jpeg':
            image = Image.open(filename).convert("RGB")
            width, height = image.size
            reader = easyocr.Reader(['nl'])
            result = reader.readtext(filename)

            doc = fitz.open()
            page = doc.new_page(width = width, height = height)

            img_rect = fitz.Rect(0, 0, width, height)
            page.insert_image(img_rect, filename=filename)

            # Overlay the OCR'd text (transparent)
            for (bbox, text, conf) in result:
                if conf < 0.1:  # Skip low-confidence text
                    continue
                # Get rectangle from bbox
                rect = fitz.Rect(*bbox[0], *bbox[2])
                page.insert_textbox(rect, text, fontsize=10, color=(0, 0, 0), overlay=True, render_mode=0)  # render_mode=3 = invisible text

            filename = filename.split(sep='.')[0]
            filename = f'easyOCR/{filename}.pdf'
            doc.save(filename)
            print(f'finished processing {filename}')
            doc.close()
        
