# Parser 100 баллов дз
from bs4 import BeautifulSoup 
import requests
import csv
import pprint
# Необходимые инструменты:
# 1)bs4
# 2)requests
# 3)csv
# 4)lxml
# 5)selenium webdriver

# Техническое задание

# Необходимо вытянуть данные с сайта
url = 'https://global.wildberries.ru/catalog?category=9492'
def parsing_dat(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    container = soup.find('div', class_='card-cell')
    print(container)
parsing_dat(url)
# Парсинг сайтов – это новый метод ввода данных, который не требует повторного
# ввода или копипастинга. Такого рода программное обеспечение ищет информацию под
# контролем пользователя или автоматически, выбирая новые или обновленные данные
# и сохраняя их в таком виде, чтобы у пользователя был к ним быстрый доступ.
# Что нужно сделать?
# 1) Спарсить наименование товара;
# 2) Спарсить цену товара;
# 4) Спарсить линк картинки этого товара

# Полезные ссылки:

# 1) https://google.com/
# 2) https://youtube.com/
# 3) https://leftjoin.ru/all/parsim-dannye-kataloga-sayta-ispolzuya-beautiful-soup-i-selenium/
# 4) https://www.dataquest.io/blog/web-scraping-tutorial-python/
# 5) https://devman.org/encyclopedia/modules/bs4-tutorial/
# 6) https://www.crummy.com/software/BeautifulSoup/bs4/doc.ru/bs4ru.html
# 7) https://www.youtube.com/watch?v=ykjBVT57r68
# 8) https://www.youtube.com/watch?v=3hgkiDAaSQs
# 9) https://habr.com/ru/companies/selectel/articles/754674/