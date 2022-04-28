from django.contrib import admin

# Register your models here.
from .models import Shoe, Release, Accessory

# Register your models here
admin.site.register(Shoe)
admin.site.register(Release)
admin.site.register(Accessory)