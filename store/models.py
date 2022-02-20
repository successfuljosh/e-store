from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'   # set the plural instead of  Categorys

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)    #cascade=>deletes products when the category is deleted
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')  #stores the link in the db, requires pillow package
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products' 
        ordering = ('-created',)  #sets the ordering based on created attribute in descending order (-)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.slug])
    