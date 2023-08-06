from django.contrib import admin
from . models import *
# Register your models here.

# we created this class for displaying the name which are we needed in admin
class categoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image' , 'description')


admin.site.register(Category, categoryAdmin)
admin.site.register(Product)