from squirrely_feed.celery import app
import requests
from bs4 import BeautifulSoup
from .models import Article
from .data_queues import toi_queue, MAX_LEN
from traceback import print_exc
import re

def toi_scrapper():
    base_url = 'https://timesofindia.indiatimes.com'
    html_content = requests.get(base_url).content
    soup = BeautifulSoup(html_content, 'html.parser')
    news_lists = soup.findAll('div', {'class':'list8'})
    links = soup.findAll('a', href=re.compile('^/.*.cms$'), title=re.compile('.*'))
   
    url_presence_mapper = set()

    for link in links:
        try:
            url = base_url+link['href']
            if url not in url_presence_mapper:
                article = Article(title=link['title'], source=base_url, url=url)
                article.save()
                url_presence_mapper.add(url)
                if len(toi_queue) == MAX_LEN:
                    toi_queue.pop(0)
                toi_queue.append(article)
        except Exception as ex:
           print("internal server error ", ex)

@app.task()
def aggregate_news():
    print("starting news aggregation")
    toi_scrapper()

