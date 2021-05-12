import os
import time
from random import randint
from urllib.request import urlretrieve

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36")

MAP_URLS = {
    "bing": "https://www.bing.com/images/search",
    "google": "https://www.google.com/search",
    "yahoo": "https://images.search.yahoo.com/search/images"
}


def get_selenium_driver(headless):
    browser_options = Options()
    if headless:
        browser_options.add_argument("--headless")
    # browser_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36")

    # create webdriver Firefox instance
    driver = webdriver.Firefox(options=browser_options, firefox_profile=profile)
    return driver


def scroll_till_element_is_found(element, driver):
    """ Scroll till element is found. Method work only for google search """
    while not element.is_displayed():
        time.sleep(randint(2, 7))
        driver.find_element_by_tag_name('body').send_keys(Keys.END)


def scroll_down(driver):
    # code from https://stackoverflow.com/questions/48850974/selenium-scroll-to-end-of-page-in-dynamically-loading-webpage
    """A method for scrolling the page."""

    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page.
        time.sleep(randint(2, 7))

        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break
        last_height = new_height


def download_images(list_of_images, image_dir, file_format):
    print("Downloading images..")
    count = 0
    for index, image_url in enumerate(list_of_images):
        image_file = os.path.join(image_dir, f"{file_format}_{str(index)}.jpg")
        try:
            urlretrieve(image_url, image_file)
            time.sleep(0.5)
        except Exception as e:
            print(e)
            count += 1
    print(f"Failed to retrieve {count} images")
    return index


def check_directory_contains_data(image_dir):
    # Exit if directory contains data.
    os.makedirs(image_dir, exist_ok=True)
    if len(os.listdir(image_dir)) > 0:
        print("Directory contains data...Exiting.")
        sys.exit()


def get_url(query, engine):
    url = MAP_URLS[engine] + "?q=" + query
    if "google" in engine:
        url = url + "&tbm=isch"  # this is required to display image page.
    return url
