import os
import django


# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scrapper.settings')
django.setup()

import requests
from bs4 import BeautifulSoup
from home.models import *
import uuid
from home.tasks import *





def scrape_imdb_news():
    url = 'https://m.imdb.com/news/movie/'
    headers = { 
        'User-Agent': "Mozlla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url,headers=headers)
    
    soup = BeautifulSoup(response.text,'html.parser')
    articles = []
    news_items = soup.find_all('div',class_='ipc-list-card--border-line')
    
    for item in news_items:
        
        title = item.find('a',class_="ipc-link ipc-link--base sc-dd244256-2 gbQCSG")
        description = item.find('div',class_="ipc-html-content-inner-div")
        image = item.find('img',class_="ipc-image")
        external_link = title['href'] if title else "No external link"
        
        
        title = title.text.strip() if title else "No Title"
        description = description.text.strip() if title else "No Description"
        image = image['src']
        image_path = None

        if image:
            image_name = f"image_{uuid.uuid4()}.jpg"
            image_path = download_image.delay(image, 'downloads/IMDB/',image_name)
        
        # articles.append({
        #     'title':title,
        #     'description':description,
        #     'image':image,
        #     'external_link':external_link
        # })
    
        news = {
            'title': title,
            'description': description,
            'image': image,
            'external_link': external_link
        }
        IMBD_News.objects.create(**news)

    

#ipc-html-content-inner-div
def scrape_toi_news():
    url = "https://timesofindia.indiatimes.com/news"
    
    #For Scrapping Times Of India Page, we actually don't need to use the header. But we are using for godd pracctices
    headers = { 
        'User-Agent': "Mozlla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    resposne = requests.get(url)
    soup = BeautifulSoup(resposne.text,'html.parser')

    news_items = soup.find_all('li')
    News_Lists = []
    for item in news_items:
        title_tag = item.find('p',class_="CRKrj")
        description_tag = item.find('p',class_="W4Hjm")
        image_tag = item.find('img')
        link_tag = item.find('a',href=True)

        if not (link_tag and title_tag and description_tag and image_tag):
            continue
    

        title = title_tag.text.strip() if title_tag else "No Title"
        description = description_tag.text.strip() if title_tag else "No Description"
        # image = image_tag.get('src') or image_tag.get('data-src') or ""
        external_link = link_tag['href'].strip()
        image = None
        if image_tag:
            if image_tag.has_attr('data-src'):
                image = image_tag['data-src']
            elif image_tag.has_attr('src'):
                image = image_tag['src']
            
            # Ensure full image URL
            if image and image.startswith("/"):
                image = "https://static.toiimg.com" + image

        if TOI_News.objects.filter(title=title).exists():
            print("Duplicate found. Skipping:", title)
            continue
        if image:
            image_name = f"image_{uuid.uuid4()}.jpg"
            image_path = download_image.delay(image, 'downloads/TOI/',image_name)

        news= {
            'title':title,
            'description':description,
            'image':image,
            'external_link':external_link        
        }
        TOI_News.objects.create(**news)
        # News_Lists.append({
        #     'title': title,
        #     'description': description,
        #     'image': image,
        #     'external_link': external_link
        # })
   
    

    

