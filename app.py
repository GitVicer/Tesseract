from flask import Flask, request
import pytesseract

app = Flask(__name__)

@app.route('/upload-image', methods = ['POST'])
def image_to_text():
    file = request.files['image']
    file.save('uploaded-image')
    text = pytesseract.image_to_string('uploaded-image',lang='eng')
    return (text)


