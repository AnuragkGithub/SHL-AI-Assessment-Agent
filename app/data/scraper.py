import requests
from bs4 import BeautifulSoup

URL = "https://www.shl.com/solutions/products/product-catalog/"

def scrape():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    print("Scraping completed")

if __name__ == "__main__":
    scrape()