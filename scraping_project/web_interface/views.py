from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,Http404,JsonResponse
from django.template import loader
from django.utils import timezone
from django.http import HttpResponse,HttpResponseRedirect,Http404,JsonResponse
from django.urls import reverse
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from uuid import uuid4
from urllib.parse import urlparse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_POST, require_http_methods
from django.views.decorators.csrf import csrf_exempt
from scrapyd_api import ScrapydAPI
from scrapy import signals
from scrapy.crawler import Crawler, CrawlerProcess,CrawlerRunner
from web_scraper.web_scraper.spiders.paytm_crawler import PaytmCrawlerSpider
from twisted.internet import reactor
from web_interface.models import ScrapyItem
import scrapy,time
# Create your views here.

scrapyd = ScrapydAPI('http://localhost:6800')

def searchdata(request):
    if 'q' in request.GET:
        querystring = request.GET.get('q').strip()
        if len(querystring) == 0:
            return redirect('/search/')

        results= []
        url = request.GET.get('q', None)
        #page = request.GET.get('page')
        unique_id = str(uuid4())
        settings = {
            'unique_id': unique_id
        }
        #if url!=None and page==None:
        task = scrapyd.schedule('default','paytm_crawler',
                                settings=settings, search_data=querystring)
        task1 = scrapyd.schedule('default','snapdeal_crawler',
                                 settings=settings, search_data=querystring)
        time.sleep(20)
        status = scrapyd.job_status('default', task)
        status1 = scrapyd.job_status('default', task1)
        obj=ScrapyItem.objects.get(unique_id=unique_id)
        for i in obj.paytm_data.values():
            results.append(i)
        for i in obj.snapdeal_data.values():
            results.append(i)
        print(results[0])
        # paginator = Paginator(results, 5)
        # products = paginator.get_page(page)
        return render (request, 'web_interface/results.html', {
            'querystring': querystring,
            'results': results,
        })

    else:
        return render(request, 'web_interface/search.html', {})

def viewdata(request):
    if request.method =='GET':
        all_objs=[]
        paginator = Paginator(all_objs, 5)
        page = request.GET.get('page')
        profiles = paginator.get_page(page)
        return render(request,'web_interface/results.html',{'results' : profiles})
