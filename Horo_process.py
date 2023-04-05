import requests
from bs4 import BeautifulSoup
from nltk.tokenize import regexp_tokenize
from collections import Counter
import random


def text_saver(text, name, sep='\n'):
    with open(f'{name}.txt', 'a+', encoding='utf-8') as myf:
        myf.write(text + sep)
    return


def links_getter(name):
    with open(name, 'r') as myf:
        links_list = myf.read().split(sep='\n')
    return links_list

def url_getter(url):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, features='lxml')
    a_list = soup.find_all('a')
    a_list.pop()
    links = []
    for a in a_list:
        link = a['href']
        if link[0] == '/':
            link = 'https://astrorok.ru' + link
        if link[0:4] != 'http':
            link = 'https://astrorok.ru/' + link
        links.append(link)
    return links
