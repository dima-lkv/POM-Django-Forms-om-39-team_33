from django.contrib import admin
from django.contrib.admin import StackedInline, TabularInline
from author.models import Author
from book.models import Book


class BookInline(StackedInline):
    model = Author.books.through
    extra = 3
    # fields = ['name']
    # fields = ['book_name']
    # readonly_fields = ['name']

    # @staticmethod
    # def name(instance):
    #     return instance.book.name


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
        return '\n'.join([a.name for a in obj.books.all()])


admin.site.register(Author, AuthorAdmin)
