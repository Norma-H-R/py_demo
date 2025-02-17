from django.contrib import admin
from .models import Dox


class DoxAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'uploaded_at')
    list_display_links = ('id', 'file')

admin.site.register(Dox)