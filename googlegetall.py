import requests
from random import randint
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import requests
os.environ['http_proxy']=''
import urllib,urllib2
import sys,glob
from bs4 import BeautifulSoup
import time
s = requests.session()
s.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"})

URL = "https://www.google.com/search"
images = []
pathf= sys.argv[2]+"/"
pathh = pathf+sys.argv[3]+".google."+sys.argv[1]+'*'

#print pathh
if not os.path.exists(sys.argv[2]):
	try:
	    os.makedirs(sys.argv[2])
	except OSError as e:
	    pass
elif len(glob.glob(pathh))>0:
    print "Directory exists ... moving on!"
    quit()
def get_images(query, start):
    screen_width = 1920
    screen_height = 3660
    hdr={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',}
    params = {
        "q": query,
        "sa": "X",
        "biw": screen_width,
        "bih": screen_height,
        "tbm": "isch",
        "ijn": start/100,
	"tbs": "itp:photo",
        "start": start,
		"num" : 1000,
       "ei": "" #- #This seems like a unique ID, you might want to use it to avoid getting banned. But you probably still are.
    }

    #request = s.get(URL, params=params)
    url=URL+"?q="+query.lower()+"&start="+str(start)+"&tbm=isch&sa=X&ijn="+str(start/100)+"&tbs=itp:photo&num=1000"
#    print url

#    req = urllib2.Request(url, headers=hdr)
    request = s.get(url)
    bs = BeautifulSoup(request.text)#urllib2.urlopen(req))
    time.sleep(.5)	    
#    if "traffic" in str(bs):
#	print "Blocked!\n"
#	quit()
#    print bs
    for img in bs.findAll("div", {"class":"rg_bx rg_di rg_el ivg-i"}):
	ss=(img.find('img').attrs['data-src'])
	#print img
        images.append(ss)
    #print len(images)




for x in range(0, 10):
    get_images(sys.argv[1], x*100)
    time.sleep(randint(2,7))
print "google: download of "+str(len(images))+" images has started"
for i,y in enumerate(images):

    urllib.urlretrieve(y , str(sys.argv[2])+"/"+str(sys.argv[3])+'.google.'+str(sys.argv[2])+'.'+str(i)+".jpg")


