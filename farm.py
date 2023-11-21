import requests
import json
import selenium
from selenium import webdriver
import time
import subprocess


def farm():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' 
    print('Opening Chrome')
    
    #Opening youtube
    driver = webdriver.Chrome(executable_path='/Users/danteschrantz/Desktop/chromedriver', options=chrome_options)
    driver.get('https://www.youtube.com/watch?v=TET2gPb7ye0')
    

while True:
    farm()
    


