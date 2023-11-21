import requests
import json
import selenium
from selenium import webdriver
import time



    
    
    
def check():
    r = requests.get('https://kith.com/collections/mens-footwear/products.json')
    products = json.loads(r.text)['products']

    for product in products:
        productname = product['title']
        if productname == 'Nike Air Jordan 4 SE Craft - Medium Olive / Pale Vanilla / Khaki / Black-Sail':
            producturl = 'https://kith.com/collections/mens-footwear/products/' + product['handle']
            print('Item Found!')
            return producturl

    return False


def buyProduct(url):
  chrome_options = webdriver.ChromeOptions()
  chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' 
  print('Opening Chrome')
  
  #Access product
  driver = webdriver.Chrome(executable_path='/Users/Desktop/chromedriver', options=chrome_options)
  driver.get(str(url))
  print('Accessing product page')
  time.sleep(3)
  
  #Size Selection
  driver.find_element_by_xpath('//div[@option value="10"]').click()
  time.sleep(1)
  print('Getting Size')

  #Add to Cart
  driver.find_element_by_xpath('//button[@class="btn product-form__add-to-cart"]').click()
  time.sleep(1)
  print('Adding to Cart')

  #check out
  driver.find_element_by_xpath('//button[@name="checkout"]').click()
  time.sleep(.1)
  print('Going to Checkout')

  #enter email
  driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys('example@gmail.com')
  time.sleep(.1)

  #Enter first name 
  driver.find_element_by_xpath('//input[@placeholder="First name"]').send_keys('Example')
  time.sleep(.1)

  #Enter Last Name
  driver.find_element_by_xpath('//input[@placeholder="Last name"]').send_keys('Example_Last')
  time.sleep(.1)

  #Enter Street
  driver.find_element_by_xpath('//input[@placeholder="Address"]').send_keys('1234 May Street')
  time.sleep(.1)

  #Enter City
  driver.find_element_by_xpath('//input[@placeholder="City"]').send_keys('City')
  time.sleep(.1)

  #Enter Zip Code
  driver.find_element_by_xpath('//input[@placeholder="ZIP code"]').send_keys('12345')
  time.sleep(.1)

  #Phone Number
  driver.find_element_by_xpath('//input[@placeholder="Phone"]').send_keys('1234567890' + u'\ue007')
  print('Shipping Info Submitted')

while True:
    myUrl = check()
    if myUrl != False:
        buyProduct(myUrl)
    else:
        print('Not Possible')
