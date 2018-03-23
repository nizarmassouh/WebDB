import requests
import glob
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import requests
os.environ['http_proxy']=''
import urllib,urllib2
import sys,time
from bs4 import BeautifulSoup
s = requests.session()
s.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"})
URL = "http://www.bing.com/images/async?q="+sys.argv[1]+"&count=150&lostate=r&mmasync=1&dgState=x*1039_y*1099_h*208_c*5_i*36_r*6%22"
images = []
pathf= sys.argv[2]+"/"
pathh = pathf+sys.argv[3]+".bing."+sys.argv[1]+'*'

if not os.path.exists(sys.argv[2]):
        try:
            os.makedirs(sys.argv[2])
        except OSError as e:
            pass
elif len(glob.glob(pathh))>0:
    print "Directory exists ... moving on!"
    quit()


def get_images(query,st):
    url=URL+"&first="+str(st)
    request = s.get(url)
    bs = BeautifulSoup(request.text)
    for img in bs.findAll('img'):
	try:	
		ss=img.attrs['src']
		images.append(ss)
	except:
		pass


for i in range(0,5):
	get_images(sys.argv[1],0+(i*160))

print "bing: download of "+str(len(images))+" images has started"
for i,y in enumerate(images):
     fil=str(sys.argv[2])+"/"+str(sys.argv[3])+'.bing.'+str(sys.argv[1])+'.'+str(i)+".jpg"
     try:
	     urllib.urlretrieve(y ,fil)
     except:
	     continue
