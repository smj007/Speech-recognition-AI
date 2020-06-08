# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 09:56:23 2020

@author: saimi
"""

import subprocess
import os
import requests
from bs4 import BeautifulSoup
from get_answer import Fetcher


class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "si", "sure", "do it", "yeah", "confirm"]
        self.cancel = ["no", "negative", "negative soldier", "don't", "wait", "cancel"]
        
    def discover(self, text):
        if "what" in text and "your name" in text:
            if "my" in text:
                self.respond("You have not told me your name yet")
                   

        else:
            f = Fetcher("https://www.google.com/search?q=")
            answer = f.lookup()
            self.respond(answer)
            
                
# =============================================================================
#         elif "open" in text or "launch" in text:
#             app = text.split(" ", 1)[-1]
#             self.respond("Opening " + app)
#             #os.chdir("C:\Program Files (x86)\Google\Chrome\Application") - Do not use, use only for testing
#             os.system("start " + app + ".exe")
# =============================================================================
                
       
                
    def respond(self, response):
        print(response)
        subprocess.call("say " + response, shell = True)            