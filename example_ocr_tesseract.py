from PIL import Image
import os
import pytesseract

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
            # IF TRUE; save OCR'd image as pdf variable named 'pdf'
            pdf = pytesseract.image_to_pdf_or_hocr(filename, extension='pdf', lang='nld')
            # define variable 'filename' identical to the previous definition with 'jpg' changed to 'pdf'
            filename = filename.split(sep='.')[0]
            # open empty file with filename 'IMAGE_NAME.pdf'
            with open(f'tesseract/{filename}.pdf', 'w+b') as f:
                # saving the OCR'd image under the empty file
                f.write(pdf)