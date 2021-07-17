from django.contrib import admin

# Register your models here.
from medicine_app.models import Category, Product

# admin.site.register(Category)
# admin.site.register(Product)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Product,ProductAdmin)