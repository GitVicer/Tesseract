import pytesseract
import urllib.request
import pandas

def isNumber(str):
    
    for char in str:
        if char.isdigit() != True and char != '-' and char != '+' and char != " ":
            return False
    return True 


def image_to_text(image_url):
    urllib.request.urlretrieve(image_url, 'uploaded_image')
    
    text = pytesseract.image_to_string('uploaded_image', lang='eng')
    if text == "":
        return 'Not able to detect text in the image'
    
    try:
        index = text.index('+')
    except:
        index = 0
        return '"+" not found in the text'
    
    num = text[index:index+15]
    
    if isNumber(num):
        return num
    else:
        return "Not found"
        


df = pandas.read_excel('Untitled.xlsx')

df['screenshot_google_vision_url'] = df['screenshot_google_vision_url'].astype(str)


for index,row in df.iterrows():
    try:
        url = row['screenshot_google_vision_url']
        text = image_to_text(url)
        df.at[index, 'Text'] = text
    except ValueError:
        text = 'url not found'
        df.at[index, 'Text'] = text

    

df.to_excel('output.xlsx')




    


