from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='media/category', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)


class CarServices(models.Model):
    owner = models.ForeignKey(User, related_name='user_car_sevices', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='service_category', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    contact = models.IntegerField()
    email = models.EmailField()
    image = models.ImageField(upload_to='images', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    lat = models.FloatField()
    lon = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(CarServices, self).save(*args, **kwargs)