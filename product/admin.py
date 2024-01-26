from django.contrib import admin

# Register your models here.
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display= ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display= ('name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, CategoryAdmin)
