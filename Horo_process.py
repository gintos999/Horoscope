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