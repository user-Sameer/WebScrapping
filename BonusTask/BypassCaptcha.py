from PIL import Image
from selenium import webdriver
from PIL import Image, ImageFilter
import pytesseract 
from selenium.webdriver.common.by import By

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

#defing the chromedriver
PATH="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
#loading the url
driver.get("https://www.amazon.com/errors/validateCaptcha")




# function to get the captcha
def get_captcha(driver, element, path):
     
    size = element.size    
    # saves screenshot of entire page
    driver.save_screenshot(path)
    # uses PIL library to open image in memory
    image = Image.open(path)
    left = 450
    top = 302+67
    right = 410 + size['width'] + 200
    bottom = 302 + size['height'] + 90
    image = image.crop((left, top, right, bottom))  # defines crop points
    image.save(path, 'png')  # saves new cropped image

    captcha = pytesseract.image_to_string(image) 
    
    print(captcha)
    return captcha

   


img = driver.find_element(By.XPATH, "//div[@class='a-row a-text-center']/img")
captcha=get_captcha(driver, img, "captcha.png")
#sending the extracted text to the captcha webpage
fillcaptcha=driver.find_element(By.XPATH, "//input[@id='captchacharacters']")
fillcaptcha.send_keys(captcha)

driver.quit()