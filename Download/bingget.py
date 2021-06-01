from bs4 import BeautifulSoup

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from common_utils import get_selenium_driver, scroll_down, download_images, check_directory_contains_data, get_url, get_args, click_button

args = get_args()
search_engine = "bing"
file_format = f"{args.index}_{search_engine}_{args.query}"
# check if save_image_dir contains data and exit if data already present.
check_directory_contains_data(args.save_image_dir, file_format)

# prepare the Firefox webdriver
driver = get_selenium_driver(args.run_headless)
images = []


def get_images(query):
    """Scrape the images for bing search engine and append the image url to a python list

    Args:
        query (str): Query for which the images will be downloaded
    """
    count = 0
    url = get_url(args.query, search_engine)
    print(url)
    driver.get(url)

    # scroll till the end.
    scroll_down(driver)
    # click the button "see more images"
    click_button(driver, "a.btn_seemore.cbtn.mBtn")
    # Scroll till end.
    scroll_down(driver)

    request = driver.page_source
    bs = BeautifulSoup(request, features="html.parser")
    tags = bs.findAll("img")
    for img in tags:
        try:
            image_links = img.attrs['src']
            if "http" in image_links:
                images.append(image_links)
        except Exception:
            count += 1
    print(f"Number of img tags without src attribute or http: {count}")


get_images(args.query)
driver.delete_all_cookies()
driver.close()

total_image_links = len(images)
images = set(images)
print(f"Total image links: {total_image_links}")
print(f"Total Duplicate links: {total_image_links - len(images)}")

total_downloaded_images = download_images(images, args.save_image_dir, file_format)
print(f"{search_engine}: {total_downloaded_images} images downloaded successfully!")
