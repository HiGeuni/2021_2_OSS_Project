from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request
import time
import socket
from io import BytesIO
from PIL import Image
import argparse
import numpy as np
import tensorflow as tf
import cv2

socket.setdefaulttimeout(10)

# Declare ArgumentParser
parser = argparse.ArgumentParser()
parser.add_argument("--keyword",nargs='+')
parser.add_argument("--txt", help="Using txt file, Set Keyword")
parser.add_argument("--comb", nargs='+', help="Set This Argument When You Want to Crawling word combination with keyword")
parser.add_argument("--noPaint", type=bool, default=False, help= "Set This Argument When You Want to Only Real Images")
parser.add_argument("--limitSize",type=int, default=800, help = "To prevent Too small Image")
parser.add_argument("--type", default="jpg")
parser.add_argument("--dst", help="Set Save Folder", required=True)
args = parser.parse_args()

IMG_SIZE =(224,224)

if args.noPaint:
    print(2)
    model = tf.keras.models.load_model('./model/model.h5')

def checkPaint(img):
    img = np.array(img)
    img = cv2.resize(img, dsize=IMG_SIZE, interpolation=cv2.INTER_CUBIC)
    img = np.reshape(img, (1, 224, 224, 3))
    img = tf.keras.applications.vgg16.preprocess_input(img)
    prediction = model.predict(img)
    return round(prediction,1)

# Crawling Function
def crawling(keyWord):
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.google.co.kr/imghp?hl=ko&authuser=0&ogbl")
    time.sleep(2)
    elem = driver.find_element_by_name("q")
    elem.send_keys(keyWord)
    elem.send_keys(Keys.RETURN)
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(1.5)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height

    cnt=1
    ls = driver.find_elements_by_css_selector("img.rg_i.Q4LuWd")
    print("Number of Images : ", len(ls))
    address = args.dst+"/"
    for img in ls:
        print(cnt)
        try:
            ActionChains(driver).click(img).perform()
            time.sleep(1)
            imgurl = driver.find_element_by_xpath(
                '/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img').get_attribute(
                "src")
            imageInfo = urllib.request.urlopen(imgurl).read()
            image = Image.open(BytesIO(imageInfo))
            flag = True
            if args.noPaint:
                flag = checkPaint(image)
            if flag and max(image.size) >= args.limitSize:
                cnt += 1
                print(address + str(keyWord.replace(" ", "_").rstrip()) + str(cnt) + "." + args.type)
                image.save(address + str(keyWord.replace(" ", "_").rstrip()) + str(cnt) + "."+args.type, "JPEG", quality=95,
                           optimize=True, progressive=True)
            #urllib.request.urlretrieve(imgurl,address+str(keyWord.replace(" ", "_").rstrip())+str(i)+".jpg")
            image.close()
        except:
            pass
    driver.close()

if __name__ == "__main__":
    if args.keyword:
        if args.comb:
            for i in args.keyword:
                for j in args.comb:
                    crawling(i+" "+j)
        else:
            for i in args.keyword:
                crawling(i)

    elif args.txt:
        f = open(args.txt)
        print(args.txt)
        for keyword in f.readlines():
            print(keyword)
            crawling(keyword)

    else:
        print("Unvalid Argument, You Should Set Argument keyword or txt")
        exit(0)