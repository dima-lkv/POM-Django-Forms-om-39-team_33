from django.contrib import admin
from book.models import Book
from django.contrib.admin import StackedInline, TabularInline


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'issueYear', 'get_authors']
    list_filter = ['authors', 'issueYear']
    search_fields = ['name', 'description', 'issueYear']
    readonly_fields = ['issueYear',]

    fieldsets = (
        ('Read only', {
            'fields': ('issueYear',)
        }),
        ('Edit', {
            'fields': ('name', 'publicationYear', 'description'),
        }),
    )

    def get_authors(self, obj):
        return ' '.join([a.__str__() for a in obj.authors.all()])


admin.site.register(Book, BookAdmin)
