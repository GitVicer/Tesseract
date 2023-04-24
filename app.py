from flask import Flask, request
import pytesseract
import urllib.request

app = Flask(__name__)

@app.route('/upload_image', methods = ['POST'])
def image_to_text():

    image_url = request.form.get('image_url')

    urllib.request.urlretrieve(image_url, 'uploaded_image')

    text = pytesseract.image_to_string('uploaded_image', lang='eng')

    return text


