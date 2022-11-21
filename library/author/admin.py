from django.contrib import admin
from django.contrib.admin import StackedInline
from author.models import Author


class BookInline(StackedInline):
    model = Author.books.through
    extra = 3


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'patronymic', 'get_books')
    list_filter = ['name', 'books']
    search_fields = ['name', 'surname']
    inlines = [
        BookInline,
    ]
    exclude = ('books',)

    @staticmethod
    def get_books(obj):
        return '\n'.join([b.name for b in obj.books.all()])


admin.site.register(Author, AuthorAdmin)
