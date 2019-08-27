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
* DB used is MYSQL and it should be configured and password for the database in picked via environment variable $DB_PASSWORD
* python3 manage.py makemigrations
* python3 manage.py migrate
* ON a new tab in terminal change directory to /django-scraping/scraping_project/web_scraper and then run scrapyd (please note scrapyd should be ran on a new tab in terminal alongside django server)
* python3 manage.py runserver
