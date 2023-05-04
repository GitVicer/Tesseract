import pandas
import pytesseract
import urllib.request

# Function to check for a valid phone number
def isNumber(str):
    for char in str:
        if char.isdigit() != True and char != '-' and char != '+' and char != " ":
            return False
    return True 

# Function to convert image to to text
def image_to_text(url):

    urllib.request.urlretrieve(url, 'uploaded_image')
    
    text = pytesseract.image_to_string('uploaded_image', lang='eng')
    if text == "":
        return 'Not able to detect text in the image'
    
    for i in range(len(text)):
        if text[i] == '+':
            num = text[i:i+15]
            if isNumber(num):
                return num
            else:
                pass
    return text    

# Manipulating the excel sheet
df = pandas.read_excel('sheet 3.xlsx')

df['screenshot_google_vision_url'] = df['screenshot_google_vision_url'].astype(str)

for index, row in df.iterrows():
    try:
        url = row['screenshot_google_vision_url']
        text = image_to_text(url)
        df.at[index, 'Text'] = text
    except:
        text = 'url not found'  
        df.at[index, 'Text'] = text          

df.to_excel('output.xlsx')  
    
        
    
        
            





    


