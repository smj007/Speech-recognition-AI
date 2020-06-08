# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 14:05:33 2020

@author: saimi
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 11:50:06 2020

@author: saimi
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By #checks if an element is present
from selenium.webdriver.support.ui import WebDriverWait #waits for a response
from selenium.webdriver.support import expected_conditions as EC #defines what the required return conditions are
from selenium.common.exceptions import TimeoutException #if no response after sometime, issue an error throw
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys

class Fetcher:
    def __init__(self, url):
        driver_options = Options()
        driver_options.headless = True
        driver = webdriver.Chrome(options=driver_options, executable_path="resources/chromedriver.exe")
        driver.wait = WebDriverWait(driver, 5)
 
        # save instance variables
        self.driver = driver
        self.url = url
 
        # call lookup method
        self.lookup()
        
    def lookup(self):
        self.driver.get(self.url)
        try:
            ip = self.driver.wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "gsfi")
            ))
            soup = BeautifulSoup(self.driver.page_source, "html.parser")
            answer = soup.find_all(class_="Wnoohf")
            print(answers.get_text())
        except:
            print("Failed to get element in time")
            
            
     