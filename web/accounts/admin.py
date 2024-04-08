from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Talk ,Photo

# Register your models here.

class TalkAdmin(admin.ModelAdmin):
  list_display = ("topic", "Talk","posted_date",)

class PhotoAdmin(admin.ModelAdmin):
  list_display = ("image","upload_date")
  
admin.site.register(Talk, TalkAdmin)
admin.site.register(Photo,PhotoAdmin)