from django.contrib import admin
from .models import Booklist

class BooklistAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')

admin.site.register(Booklist, BooklistAdmin)
