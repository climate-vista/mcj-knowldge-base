from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = "https://my-climate-journey.simplecast.com/episodes/lumen/transcript"

# Initialize a browser (in this case, Chrome)
driver = webdriver.Chrome()

# Get the webpage
driver.get(url)
time.sleep(5)

# Get the page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
transcript = soup.find('div', {'class': 'sc-episode-details-body'})
transcript = transcript.find_all('div')[-1]

for p in transcript.find_all('p'):
    p.replace_with(p.text + '\n')

with open('transcript.txt', 'w', encoding='utf-8') as f:
    f.write(str(transcript.text))

# Close the browser
driver.quit()