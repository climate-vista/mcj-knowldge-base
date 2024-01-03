from selenium import webdriver
from bs4 import BeautifulSoup
import time
import json


def download_transcript(url):
    # Initialize a browser (in this case, Chrome)
    driver = webdriver.Chrome()

    # Get the webpage
    driver.get(url)
    time.sleep(5)

    # Get the page source and parse it with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")
    transcript = soup.find("div", {"class": "sc-episode-details-body"})
    transcript = transcript.find_all("div")[-1]
    for p in transcript.find_all("p"):
        p.replace_with(p.text + "\n")
    transcript_text = str(transcript.text)

    # Close the browser
    driver.quit()
    return transcript_text


def main():
    # Read in episode links
    with open("episode_links.json", "r") as f:
        episode_links = json.load(f)
    print(f"downloading {len(episode_links)} episodes...")

    # Download and save each transcripts
    for link in episode_links:
        ep_name = link.split("/")[-1]
        transcript = download_transcript(link + "/transcript")
        with open(f"../transcripts/{ep_name}.txt", "w", encoding="utf-8") as f:
            f.write(transcript)
        print(f"saved episode {ep_name}")


if __name__ == "__main__":
    main()
