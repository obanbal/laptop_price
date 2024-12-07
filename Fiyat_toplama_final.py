from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import pandas as pd
from openpyxl.workbook import Workbook

url = "https://www.hepsiburada.com/laptop-notebook-dizustu-bilgisayarlar-c-98"
driver = webdriver.Chrome()
respons = driver.get(url)
response = driver.page_source
soup = BeautifulSoup(response, "lxml")

# Laptop listelerini bul
laptops = soup.find_all("div", attrs={"data-test-id": "product-info-wrapper"})

liste = []
for laptop in laptops:
    # Ürün adı
    name = laptop.find("h3", attrs={"data-test-id": "product-card-name"}).get_text(strip=True)
    # Fiyat
    price = laptop.find("div", attrs={"data-test-id": "price-current-price"}).get_text(strip=True)
    print(f'Özellik :',name, '--->', 'Fiyat : ', price)
    liste.append([name])
    liste.append([price])

veritabani = pd.DataFrame(liste)
veritabani.columns=["Özellikler-Fiyat"]
'''veritabani.columns=["Fiyat"]'''
veritabani.to_excel("laptoplar.xlsx")