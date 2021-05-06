import glob
import os
import requests
import sys
import time
import urllib

from urllib.request import urlopen
from random import randint
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument("--headless")
# os.environ['http_proxy'] = ''
driver = webdriver.Chrome(options=chrome_options)
s = requests.session()
s.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"})
URL = "https://www.google.com/search"
images = []
pathf = sys.argv[2] + "/"
pathh = pathf + sys.argv[3] + ".google." + sys.argv[1] + '*'

os.makedirs(sys.argv[2], exist_ok=True)
if len(glob.glob(pathh)) > 0:
    print("Directory exists ... moving on!")
    quit()


def get_images(query, start):
    count = 0
    url = URL + "?q=" + query.lower() + "&start=" + str(start) + "&tbm=isch&sa=X&ijn=" + str(start / 100) + "&tbs=itp:photo&num=10000"
    driver.get(url)
    request = driver.page_source
    bs = BeautifulSoup(request, features="html.parser")
    # time.sleep(.5)
    tags = bs.findAll("div")
    for img in tags:
        try:
            ss = (img.find('img').attrs['data-src'])
            images.append(ss)
        except Exception:
            count += 1
    print(f"number div tags with no image src is {count}")


for x in range(0, 10):
    get_images(sys.argv[1], x * 100)
    time.sleep(randint(2, 7))

print("google: download of " + str(len(images)) + " images has started")
for i, y in enumerate(images):
    urllib.request.urlretrieve(y, str(sys.argv[2]) + "/" + str(sys.argv[3]) + '.google.' + str(sys.argv[2]) + '.' + str(i) + ".jpg")
print("google: download completed successfully!!")
