from django.db import models

# Create your models here.

class Page(models.Model):

    page_url     = models.URLField(max_length=400, default='')
    result_ready = models.BooleanField(default=False)

    h1 = models.IntegerField(default=0)
    h2 = models.IntegerField(default=0)
    h3 = models.IntegerField(default=0)
    a  = models.IntegerField(default=0)

    def __str__(self):
        return self.page_url


class Link(models.Model):
    page = models.ForeignKey(Page, related_name='urls', on_delete=models.CASCADE)
    url = models.URLField(max_length=400, default='')

    def __str__(self):
        return self.url