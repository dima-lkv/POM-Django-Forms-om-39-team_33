from django.contrib import admin
from book.models import Book
from django.contrib.admin import StackedInline, TabularInline



class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'count']
    list_filter = ['authors', 'count']
    search_fields = ['name', 'description']


admin.site.register(Book, BookAdmin)
