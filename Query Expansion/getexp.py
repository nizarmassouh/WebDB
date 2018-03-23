import requests 
import os 
import unicodedata
import glob
import sys 
from bs4 import BeautifulSoup 
import httplib 
import unittest, time, re 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException 
from selenium.common.exceptions import NoAlertPresentException 
#argument is query
URL ="http://mykeyworder.com/keywords?tags=" 
expansions = [] 


def get_exp(query):
    Keys=open('Keys.txt','a')
    driver = webdriver.PhantomJS()
    driver.maximize_window()
    driver.implicitly_wait(30)
    base_url = str(URL+str(sys.argv[1]))
    verificationErrors = []
    accept_next_alert = True
    driver.get(base_url )
    try:
        
	    time.sleep(1)
            bs = BeautifulSoup(driver.page_source)
	    exp=str(bs.findAll("div",{"class":"col-md-2"})[1]).split("\n")

	    for x in exp:
		
		try:
	    		ss=str(x.split("<input checked=\"\" name=\"keywordselect[]\" onclick=\"countCheckboxes()\" type=\"checkbox\" value=\"")[1]).split("\"/>")[0]
			if ss not in query:
				expansions.append(query+" "+ss)
				Keys.write(ss+' ')

        	except:
			pass   
	
	    Keys.write("\n")
    except:
        pass




get_exp(str(sys.argv[1]).rstrip()) 
print ', '.join(expansions)
