# # scraper.py

# import requests
# from bs4 import BeautifulSoup

# def scrape_urls(urls):
#     print("🕷 [Scraper] Extracting content from URLs...")
#     contents = []
#     for url in urls:
#         try:
#             response = requests.get(url, timeout=5)
#             soup = BeautifulSoup(response.content, "html.parser")
#             paragraphs = soup.find_all("p")
#             text = "\n".join(p.get_text() for p in paragraphs)
#             contents.append(text[:1000])  # Truncate for simplicity
#         except Exception as e:
#             print(f"❌ Failed to scrape {url}: {e}")
#     return contents

import requests
from bs4 import BeautifulSoup

def scrape_urls(urls):
    contents = []
    headers = {'User-Agent': 'Mozilla/5.0'}

    for url in urls:
        try:
            response = requests.get(url, headers=headers, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            text = ' '.join(p.get_text() for p in paragraphs[:5])
            contents.append(text)
        except Exception as e:
            print(f"❌ Failed to scrape {url}: {e}")
            contents.append("")

    return contents
