from django.db import models
from jsonfield import JSONField
# Create your models here.

class ScrapyItem(models.Model):
    unique_id = models.CharField(max_length=100, null=True)
    snapdeal_data = JSONField() # this stands for our crawled data
    paytm_data = JSONField() # this stands for our crawled data
