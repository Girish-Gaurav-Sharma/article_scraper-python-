import requests, string
from bs4 import BeautifulSoup
import os
url = 'https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&year=2020&page='
i = int(input())
typ = input()
for ll in range(1, i+1):
    os.mkdir(f'Page_{ll}')
    r = requests.get(url+f"{i}")
    soup = BeautifulSoup(r.content, "html.parser")
    article = soup.find_all('article')
    span_list = []
    text = []
    indices = []
    news_article = []
    link = []
    link_ = []
    for art in article:
        span =  art.find('span', {'data-test': "article.type"})
        span_list.append(span)
    for spn in span_list:
        txt = spn.text
        text.append(txt)
    for x in range(len(text)):
        if text[x] == typ:
            indices.append(x)
    for i in indices:
        arti = article[i]
        news_article.append(arti)

    for artii in news_article:
        xx = artii.find('a', {'data-track-action': "view article"})
        link.append(xx)

    for a in link:
        l = 'https://www.nature.com'+a['href']
        link_.append(l)
    for li in link_:
        url = li
        r = requests.get(li)
        sop = BeautifulSoup(r.content, "html.parser")
        title = sop.find('title')
        title = title.text
        title = ''.join(char for char in title if char not in string.punctuation)
        title_ = title.split(' ')
        title = "_".join(z for z in title_)+'.txt'
        body = sop.find('p', {"class": "article__teaser"})
        body = body.text
        body = bytes(body, 'utf-8')
        cwd = os.getcwd()
        relative_dir = f'Page_{ll}/'
        file_name = title
        title = os.path.join(cwd,relative_dir,file_name)
        with open(title, 'wb') as f:
            f.write(body)
