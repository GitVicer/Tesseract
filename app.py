from flask import Flask, request
import pytesseract
import urllib.request

app = Flask(__name__)

def isNumber(str):
    
    for char in str:
        print(char.isdigit())
        if char.isdigit() != True and char != '-' and char != '+' and char != " ":
            return False
    return True 

@app.route('/upload_image', methods = ['POST'])
def image_to_text():

    image_url = request.form.get('image_url')

    urllib.request.urlretrieve(image_url, 'uploaded_image')

    text = pytesseract.image_to_string('uploaded_image', lang='eng')
    
    index = text.index('+')
    
    num =  text[index:index+15]
    
    if isNumber(num):
        return num
    else:
        return "This program searches for a valid number on the fact that if there is a '+' followed by digits and '-'"
            





    


