# Django-Scraping

This is a project where I have integrated Django and scrapy together.I have used scrapy for crawling 2 websites namely Snapdeal.com and paytmmall.com.
I have used 2 spiders for crawling the data and then django is used for displaying the results.


### Prerequisites

* Python3
* Scrapy
* Scrapyd
* JSONField (Django)

## Deployment

To deploy locally,
* python3 manage.py makemigrations
* python3 manage.py migrate
* simultaneously run scrapyd
* python3 manage.py runserver
