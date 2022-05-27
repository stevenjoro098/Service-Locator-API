from django.contrib import admin
from .models import CarServices, Category


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(CarServices)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner','category', 'contact', 'email', 'created']
    prepopulated_fields = {'slug': ('name',)}
