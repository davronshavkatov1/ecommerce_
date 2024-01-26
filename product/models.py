from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="photoes/categories",blank=True)
    slug = models.SlugField(max_length=50, unique=True) 
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])
    
    def __str__(self) -> str:
        return self.name


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'photoes/products')
    stock = models.IntegerField(default=100)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
