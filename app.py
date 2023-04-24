from flask import Flask, request
import pytesseract
from pytesseract import TesseractError
import urllib.request

app = Flask(__name__)

@app.route('/upload_image', methods = ['POST'])
def image_to_text():

    image_url = request.form.get('image_url')

    print(image_url)
    urllib.request.urlretrieve(image_url, 'uploaded_image')

    # Save the image data to a file and perform OCR
    try:
        text = pytesseract.image_to_string('uploaded_image', lang='eng')
    except TesseractError as error:
        return str(error), 500

    return text


