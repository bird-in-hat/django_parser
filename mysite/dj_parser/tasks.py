from django.db import models
from celery.exceptions import SoftTimeLimitExceeded

from mysite.celery import app
from dj_parser.models import Page, Link

from bs4 import BeautifulSoup
import urllib.request
 

def get_tags(page):
    html_doc = urllib.request.urlopen(page.page_url).read()
    soup = BeautifulSoup(html_doc, "html.parser")
    
    for link in soup.findAll('a'):
        page.a = 1 + page.a # optimize? findAll counld be generator -> inc better then new generator
        page.urls.create(url=link.get('href')) # optimize? all creates it one

    page.h1 = len(soup.findAll('h1'))
    page.h2 = len(soup.findAll('h2'))
    page.h3 = len(soup.findAll('h3'))  

    return page


@app.task(time_limit=15, soft_time_limit=10)
def parse_page(page_id):
    page = Page.objects.get(pk=page_id)
    try:
        page = get_tags(page) 
        page.result_ready = True 
    except SoftTimeLimitExceeded:
        page.result_ready = False

    page.save()

        #? set special field for code HTTP_500_INTERNAL_SERVER_ERROR
