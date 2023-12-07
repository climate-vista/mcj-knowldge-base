from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json


def get_dynamic_links(url, load_more_button_xpath):
    # Setup Selenium with ChromeDriver
    # Note ChromeDriver is preinstalled
    driver = webdriver.Chrome()
    driver.get(url)

    links = set()

    while True:
        # Wait for the load more button to be clickable
        try:
            load_more_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, load_more_button_xpath))
            )
            load_more_button.click()
            # Wait for the page to load content
            time.sleep(5)
        except Exception as e:
            print("No more 'Load More Episodes' button found or an error occurred:", e)
            break

        # Find all links
        anchor_tags = driver.find_elements(By.TAG_NAME, "a")
        for tag in anchor_tags:
            href = tag.get_attribute("href")
            if href and href.startswith(url):
                links.add(href)

    driver.quit()
    return links


base_url = "https://my-climate-journey.simplecast.com/episodes/"
load_more_button_xpath = '//button[@class="button button-secondary"]'
found_links = get_dynamic_links(base_url, load_more_button_xpath)

# Export to json
with open("episode_links.json", "w") as json_file:
    json.dump(list(found_links), json_file)
