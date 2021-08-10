# For web automation using selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#For extracting the required data from html code
from bs4 import BeautifulSoup

#For decode base64 data to image
import io
from PIL import Image
import base64

# To make url request to the server
import urllib.request

#check the operating system platform for selecting the right web driver
from sys import platform as operating_sys

#common processes involved
import time
import sys
import os
import numpy as np

def download_image(search_query,output_Dir,scroll_Value):
    #checks whether directory exist or not, If not create it 
    if(os.path.isdir(output_Dir) == False):
        try:
            os.mkdir(output_Dir)
        except:
            print('Cannot Create the directory! Parent directory does not exist ')
            sys.exit(0)
    
    #initialize the webdriver for automation and starts the broswer in background
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    if(operating_sys == 'linux'):
        chrome_Driver_Dir = os.getcwd() + '/linux_chromedriver'
        browser = webdriver.Chrome(chrome_Driver_Dir,options = chrome_options)
    else:
        chrome_Driver_Dir = os.getcwd() + '/windows_chromedriver'
        browser = webdriver.Chrome(chrome_Driver_Dir,options = chrome_options)
        
    #Instructuons to navigate to the required page
    browser.get('https://www.google.co.in/imghp?hl=en&tab=wi&authuser=0&ogbl')
    time.sleep(5)
    searchbar = browser.find_element_by_name('q')
    searchbar.send_keys(search_query)
    searchbar.send_keys(Keys.ENTER)
    time.sleep(5)
    
    #Used to scroll the page depending on images required to download
    iterate_Value = 1
    while(iterate_Value <= scroll_Value):    
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
        iterate_Value = iterate_Value + 1
    
    #extracting the html souce code of webpage and prettify it using beautiful soup
    html_Source = browser.page_source
    html_Code = BeautifulSoup(html_Source,"html.parser")

    #finding the required portion of html source code
    containers = html_Code.findAll("div",{"class":"bRMDJf islir"})
    
    #iterating through each html source code of interest and extracting and saving it
    for count,container in enumerate(containers,start=1):
        index = str(count) + '_downloaded'
        filename = output_Dir + index + '.jpg'
        try:
            data = str(container.img['src'])
            data = data[23:]
            #saving the extracted data in the form of image file
            im = Image.open(io.BytesIO(base64.b64decode(data))).save(filename)
        except:
            try:
                data=str(container.img['data-src'])
                #saving an image from a url using request library
                urllib.request.urlretrieve(data,filename)
            except:
                continue
        