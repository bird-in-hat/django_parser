from django.db import models

# Create your models here.

class Page(models.Model):

    page_url     = models.CharField(max_length=400, default='')
    result_ready = models.BooleanField(default=False)

    h1 = models.IntegerField(default=0)
    h2 = models.IntegerField(default=0)
    h3 = models.IntegerField(default=0)
    a  = models.IntegerField(default=0)

    def __str__(self):
        return self.page_url

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        to_celery()


class Link(models.Model):
    page = models.ForeignKey(Page, related_name='urls', on_delete=models.CASCADE)
    url = models.CharField(max_length=400, default='')

    def __str__(self):
        return self.url