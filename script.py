import time
import unittest
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

url = 'https://en.wikipedia.org/wiki/'
randomUrl = 'https://en.wikipedia.org/wiki/Special:Random'
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)

driver.get(randomUrl)

firstHeading = driver.find_element_by_id('firstHeading')
class Novel(unittest.TestCase):
    
        def test_11(self):
            print('<h2>' + firstHeading.text + '</h2>')
            for x in range(10):
                time.sleep(2)
                paragraph = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/p[1]')
                sentence = paragraph.text.split('.')[0]
                word = sentence.split(' ')[-1]
                word = re.sub('[^A-Za-z0-9]+', '', word)
                if sentence!='':
                    print(sentence + '. ')
                if word != '':
                    driver.get(url + word)
                elif word == 'to':
                    driver.get(randomUrl)
                elif word == 'to:':
                    driver.get(randomUrl)    
                else:
                    driver.get(randomUrl)
                time.sleep(2)
            driver.close()


@classmethod
def tearDownClass(class_name):
        driver.quit()
unittest.main()