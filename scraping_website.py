from bs4 import BeautifulSoup
import requests
from scraping_category import scraping_all_category


url = 'http://books.toscrape.com/catalogue/category/books_1/index.html'


# Converts a relative category URL into a full URL
def category_url(url_relative):
    base_url_category = 'http://books.toscrape.com/catalogue/category/'
    return base_url_category + url_relative.replace('../', '')


# Scrapes data from all categories on the website
def scraping_website(url):
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        conteneur_ul = soup.find("div", class_="side_categories")
        all_ul = conteneur_ul.find_all("ul")
        ul = all_ul[1]
        categories = ul.find_all("li")

        for category in categories:
            url_relative = category.find("a").get("href")
            scraping_all_category(category_url(url_relative))
    else:
        print('La requête n a pas abouti.')


scraping_website(url)
