from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.CharField(max_length=500,blank=True)
    img=models.ImageField(upload_to='categories')
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('medicine_app:products_by_category',args=[self.slug])



class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.CharField(max_length=500, blank=True)
    img = models.ImageField(upload_to='products')
    price=models.DecimalField(decimal_places=3,max_digits=8)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('medicine_app:product_details',args=[self.category.slug,self.slug])

