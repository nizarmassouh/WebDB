import argparse
import glob
import os
import sys
import time
from random import randint
from urllib.request import urlretrieve

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")

MAP_URLS = {
    "bing": "https://www.bing.com/images/search",
    "google": "https://www.google.com/search",
    "yahoo": "https://images.search.yahoo.com/search/images"
}


def get_args():
    """Parse arguments passed into the file.

    Returns:
        Namespace: args name space containing individual arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, help='query for which images are searched and downloaded')
    parser.add_argument("--save_image_dir", type=str, help='path to save the downloaded images')
    parser.add_argument("--run_headless", action='store_true', help='Runs the script on browser without displaying the browser in GUI.')
    parser.add_argument("--index", type=int, help='Index number that is iterated for each search query when script is launched from download.py')
    args = parser.parse_args()
    return args


def get_selenium_driver(headless):
    """prepare the firefox selenium driver

    Args:
        headless (bool): When the flag is True scripts runs without invoking the browser

    Returns:
       Webdriver : A webdriver object used crawl webpages.
    """
    browser_options = Options()
    if headless:
        browser_options.add_argument("--headless")

    # create webdriver Firefox instance
    driver = webdriver.Firefox(options=browser_options, firefox_profile=profile)
    return driver


def scroll_down(driver):
    # code from https://stackoverflow.com/questions/48850974/selenium-scroll-to-end-of-page-in-dynamically-loading-webpage
    """A method for scrolling the page."""

    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page.
        time.sleep(randint(3, 7))

        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break
        last_height = new_height


def download_images(list_of_images, image_dir, file_format):
    """Function downloads the images from the list of URL provided.

    Args:
        list_of_images (List): List of image urls
        image_dir (str): Path where the images will be saved
        file_format (str): Used to derive the file naming convention

    Returns:
        str: The total number of images that are downloaded
    """
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
    return str(index + 1)  # + 1 as index starts from 0.


def check_directory_contains_data(image_dir, file_format):
    """Checks if the query used already contains images and terminates the program if present.

    Args:
        image_dir (str): Path where the images will be saved
        file_format (str): Used to derive the file naming convention
    """
    # Exit if directory contains data.
    os.makedirs(image_dir, exist_ok=True)
    file_path = os.path.join(image_dir, file_format) + "*"
    print(file_path)
    if len(glob.glob(file_path)) > 0:
        print("Directory contains data...Exiting.")
        sys.exit()


def get_url(query, engine):
    """Retrieves the respective url for the search engine provided and formats the search query.

    Args:
        query (str): Query for which the images will be downloaded
        engine (str): Search engine 'bing' or 'yahoo' or 'bing'

    Returns:
        str: formatted url for scraping the images
    """
    url = MAP_URLS[engine] + "?q=" + query
    if "google" in engine:
        url = url + "&tbm=isch"  # this is required to display image page.
    return url


def click_button(driver, locator):
    """function tries to find the locator passed and clicks on it

    Args:
        driver (WebDriver): Selenium webdriver object
        locator (str): locator tag that uniquely identifies an element in the DOM
    """
    try:
        button = driver.find_element_by_css_selector(locator)
        button.click()
    except NoSuchElementException:
        print(f"Element with locator {locator} not found!")
