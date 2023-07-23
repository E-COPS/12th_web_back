import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
import django
django.setup()
from activities.models import News
from datetime import datetime

def extract_year(date_string):
    date_obj = datetime.strptime(date_string, '%Y.%m.%d')
    return date_obj.year


def crawl_news():
    req = requests.get('https://e-cops.tistory.com/')
    html = req.content.decode('utf-8', 'replace')
    soup = BeautifulSoup(html, 'html.parser')
    news_elements = soup.select('main > div > div > article')
    
    news_list = []

    for news_element in news_elements:
        title = news_element.select_one('div > a > strong').text.strip()
        #author = news_element.select_one('div > a > span > b').text.strip()
        year_string = news_element.select_one('div > div > span').text.strip()
        year = extract_year(year_string)
        link = news_element.select_one('div > a')['href']
        
        img_element = news_element.select_one('a > p > img')
        img = img_element['src'] if img_element else ''

        news = {
            "title": title,
           # "author" : author,
            "year": year,
            "link" : link,
            "img" : img,
        }
        news_list.append(news)

    return news_list

if __name__ == '__main__':
    News.objects.all().delete()
    news_list = crawl_news() 
    for news_data in news_list: #db 저장
        a = News(title = news_data["title"], 
                  #author = news_data["author"], 
                  year = news_data["year"],
                  link = news_data["link"],
                  img = news_data["img"])
        a.save()

        for news in News.objects.all():
            print(f"Title: {news.title}")
            print(f"Year: {news.year}")
            print(f"Link: {news.link}")
            print(f"Image: {news.img}")
            print("-----------------------------")