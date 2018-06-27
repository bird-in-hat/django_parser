from django.db import models

# Create your models here.

class Page(models.Model):

    page_url = models.CharField(max_length=400,  default='')

    h1_count = models.IntegerField(default=0)
    h2_count = models.IntegerField(default=0)
    h3_count = models.IntegerField(default=0)

    def __str__(self):
        return self.page_url


class Link(models.Model):
    page = models.ForeignKey(Page, related_name='links', on_delete=models.CASCADE)
    a_url = models.CharField(max_length=400,  default='')

    def __str__(self):
        return self.a_url

