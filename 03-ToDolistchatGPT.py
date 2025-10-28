import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error fetching the page:", e)
    exit()

soup = BeautifulSoup(response.content, "html.parser")
books = soup.findAll("article")

rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Rating"])

    for book in books:
        title = book.h3.a["title"]
        rating_text = book.p["class"][1]
        rating = rating_map.get(rating_text, 0)
        price = book.find("p", class_="price_color").text

        print(f"📚 '{title}' — {rating} stars")
        writer.writerow([title, rating])
