from django.urls import path

from . import views

app_name = 'web_interface'
urlpatterns = [
    path('',views.viewdata,name='viewdata'),
    path('search/',views.searchdata,name='searchdata'),
    path('crawl/',views.crawl,name='crawldata'),
]
