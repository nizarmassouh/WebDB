import glob
import os
import requests
import sys
import time
import urllib

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from bs4 import BeautifulSoup

os.environ['http_proxy'] = ''
s = requests.session()
s.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"})
URL = "http://www.bing.com/images/async?q="+sys.argv[1]+"&count=150&lostate=r&mmasync=1&dgState=x*1039_y*1099_h*208_c*5_i*36_r*6%22"
images = []
pathf = sys.argv[2]+"/"
pathh = pathf+sys.argv[3]+".bing."+sys.argv[1]+'*'

os.makedirs(sys.argv[2], exist_ok=True)
if len(glob.glob(pathh)) > 0:
    print("Directory exists ... moving on!")
    quit()


def get_images(query, st):
    count = 0
    url = URL+"&first="+str(st)
    request = s.get(url)
    bs = BeautifulSoup(request.text, features="html.parser")
    for img in bs.findAll('img'):
        try:
            ss = img.attrs['src']
            images.append(ss)
        except Exception:
            count += 1
            print(f"{img} doesn't have the src attribute")


for i in range(0, 5):
    get_images(sys.argv[1], 0+(i*160))

print("bing: download of "+str(len(images))+" images has started")
for i, y in enumerate(images):
    fil = str(sys.argv[2])+"/"+str(sys.argv[3])+'.bing.'+str(sys.argv[1])+'.'+str(i)+".jpg"
    try:
        urllib.request.urlretrieve(y, fil)
    except Exception:
        continue
print("bing: Download completed successfully!!")
