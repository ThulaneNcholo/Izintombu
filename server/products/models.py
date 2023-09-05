from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class ProductsModel(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True)
    detailed_description = RichTextField(blank=True, null=True)
    main_image = models.ImageField(
        null=True, blank=True, upload_to='static/images')
    image1 = models.ImageField(
        null=True, blank=True, upload_to='static/images')
    imag2 = models.ImageField(
        null=True, blank=True, upload_to='static/images')
    image3 = models.ImageField(
        null=True, blank=True, upload_to='static/images')
    price = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
