#Required user built imports for data preprocessing to acheive data augmentation.
from black_white import gray_scale
from brightness import brightness_level
from channel_shift import ch_shift
from duplicate import remove_duplicates
from face_extraction import face_extract
from flip_horizontal import flip
from height_width_shift import shift
from laplace import transform
from rename_file import rename
from resize import image_resize
from rotation import rotate
from shear import shear_intensity
from zoom import zoom_in

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

#Used to animate the processing indicator
import threading
import itertools

#check the operating system platform
from sys import platform as operating_sys

#common processes involved
import time
import sys
import os
import numpy as np

# Acts as a process indicator while the process is running
done = False
def animate():
    for c in itertools.cycle(['->', '-->', '--->', '---->','----->','------>','-------->']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDownloading Process Completed!     ')
t = threading.Thread(target=animate)

#prints informations about the program
print('''
Please read.......
This program runs only on windows and linux for mac
System should have Google chrome Version 85.0.4183.121 pre-installed (latest)
For any other version of Google chrome download the required chrome driver version
and replace with existing one with same name depending on os.
url: https://chromedriver.chromium.org/
This project was created with an indention to create data set collection more easier to train
and build deep learning models.
Contact: madewithpy009@gmail.com
\U0001F44D \U0001F44D \U0001F44D \U0001F44D \U0001F44D \U0001F44D
''')

#Getting required inputs from the user
search_Query = str(input('Enter the keyword to be searched => '))
output_Dir_location = str(input('Output directory location => '))
scroll_Value =  1
scroll_Value = int(input('''
Images to be download
Enter 1 to download 100 images (default) (Min Value)
Enter 2 to download 200 images
Enter 3 to download 300 images
Enter 4 to download 400 images
Enter 5 to download 500 images
Enter 6 to download 600 images (Max value)
 *Note more the number of images to be download more the time for the process to complete 
'''))

#checks whether directory exist or not, If not create it 
if(os.path.isdir(output_Dir_location) == False):
    try:
        os.mkdir(output_Dir_location)
    except:
        print('Cannot Create the directory! Parent directory does not exist ')
        sys.exit(0)
        
#checks the scroll_value is in limits or not, if not set it under limits
if (scroll_Value > 6):
    scroll_Value = 6
elif (scroll_Value < 1):
    scroll_Value = 1

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
    
#From here the animation of processes start
t.start()

#Instructuons to navigate to the required page
browser.get('https://www.google.co.in/imghp?hl=en&tab=wi&authuser=0&ogbl')
time.sleep(5)
searchbar = browser.find_element_by_name('q')
searchbar.send_keys(search_Query)
searchbar.send_keys(Keys.ENTER)
time.sleep(10)

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
    index = str(count)
    filename = output_Dir_location + index + '.jpg'
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
#stopping the animation
done=True

#preprocessing the downloaded data
print('''
   Preprocessing Downloaded Images
   User can select select type of preprocessing required according to there need
   This includes programs for data arrangement like
                1. Renaming images files in the output directory (1.jpg,2.jpg....n.jpg)
                2. To remove duplicate images in the directory
                3. Extracting Frontal face from images in output directory and saving the
                   images with same file name as orginal file  else image remains unchanged (limited accuracy)
                4. Getting Laplace tranform of all images in the directory along with multiplication with constant 2
      
    This includes programs for Image Preprocessing like
                1. Image resizing of all image in the output director according to user input (width and height user inputs)
                2. Converting all images to grayscale image in the directory
                3. Data Augmentation techniques to reduce overfitting and So to increase the ability and performance of your model.
                   This includes Rotation, Width Shifting, Height Shifting, Brightness,
                   Shear Intensity, Zoom,Channel Shift, Horizontal Flip.
                   1/4 of total images in the output directory is pass to the above preprocessing fuctions
                   images are taken randomly from the directory
     *NOTE This processes are intended to make preprocessing of data easier. But always recommands to check the data after completion of the process
            and check the integrity of the data manually.
        contact: madewithpy009@gmail.com
''')
files = os.listdir(output_Dir_location)
path = output_Dir_location