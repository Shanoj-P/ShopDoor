from django.contrib import admin
from .models import Category, Product
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'availability', 'createdDate', 'updatedDate']
    list_editable = ['price', 'stock', 'availability']
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Product, ProductAdmin)
