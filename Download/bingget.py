import argparse

from bs4 import BeautifulSoup

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from common_utils import get_selenium_driver, scroll_till_element_is_found, scroll_down, download_images, check_directory_contains_data, get_url

parser = argparse.ArgumentParser()
parser.add_argument("--query", type=str, help='query for which images are searched and downloaded')
parser.add_argument("--save_image_dir", type=str, help='path to save the downloaded images')
parser.add_argument("--run_headless", action='store_true', help='Runs the script on browser without displaying the browser in GUI.')
parser.add_argument("--index", type=int, help='Index number that is iterated for each search query when script is launched from download.py')
args = parser.parse_args()

search_engine = "bing"
file_format = f"{args.index}_{search_engine}_{args.query}"
# check if save_image_dir contains data and exit if data already present.
check_directory_contains_data(args.save_image_dir, file_format)

# prepare the Firefox webdriver
driver = get_selenium_driver(args.run_headless)
images = []


def get_images(query):
    count = 0
    url = get_url(args.query, search_engine)
    print(url)
    driver.get(url)

    scroll_down(driver)
    more_results_button = driver.find_element_by_css_selector(".btn_seemore.cbtn.mBtn")

    try:
        more_results_button.click()
        scroll_down(driver)
    except NoSuchElementException:
        print("Element not found.")

    request = driver.page_source
    bs = BeautifulSoup(request, features="html.parser")
    tags = bs.findAll("img")
    for img in tags:
        try:
            image_links = img.attrs['src']
            images.append(image_links)
        except Exception:
            count += 1
    print(f"Number of img tags without src attribute is {count}")


get_images(args.query)
driver.close()

total_image_links = len(images)
images = set(images)
print(f"Total image links: {total_image_links}")
print(f"Total Duplicate links: {total_image_links - len(images)}")

download_images(images, args.save_image_dir, file_format)
print(f"{search_engine}: Download completed successfully!!")
