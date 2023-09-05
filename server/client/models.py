from django.db import models

# Create your models here.


class WhyUsModel(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
