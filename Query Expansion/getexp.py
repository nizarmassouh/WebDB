import sys
import time

from bs4 import BeautifulSoup
from selenium import webdriver
# argument is query

URL = "http://mykeyworder.com/keywords?tags="
expansions = []


def get_exp(query):
    keys = open('Keys.txt', 'a')
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    base_url = str(URL + str(sys.argv[1]))
    driver.get(base_url)
    try:
        time.sleep(1)
        bs = BeautifulSoup(driver.page_source, features="html.parser")
        exp = str(bs.findAll("div", {"class": "col-md-2"})[1]).split("\n")
        for x in exp:
            try:
                ss = str(x.split("<input checked=\"\" name=\"keywordselect[]\" onclick=\"countCheckboxes()\" type=\"checkbox\" value=\"")[1]).split("\"/>")[0]
                if ss not in query:
                    expansions.append(query + " " + ss)
                    keys.write(ss + ' ')
            except Exception as e:
                print(f"exception while getting checkboxes: {e}")
        keys.write("\n")
    except Exception as e:
        print(f"exception while parsing html: {e}")
    driver.close()


get_exp(str(sys.argv[1]).rstrip())
print(', '.join(expansions))
