import requests
import os
import time
from bs4 import BeautifulSoup


titles_and_links = open('titles.txt', 'a', encoding='utf-8')

if os.stat('titles.txt').st_size:
    titles_and_links.truncate(0)

article_list = [1]
URL = 'https://frsah.ro/index.php/page/'

page_number = 1
my_dict = {}

while article_list:

    URL = URL + str(page_number)
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    article_list = soup.find_all(class_='td_module_16 td_module_wrap td-animation-stack')

    print(article_list != [])

    for article in article_list:

        title = article.find('a')['title']
        link = article.find('a')['href']
        my_dict.update({title: link})
        titles_and_links.write(title + "  :  " + link + "\n")

    print(page_number)
    page_number += 1


titles_and_links.close()
