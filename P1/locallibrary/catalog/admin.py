from django.contrib import admin
from .models import Book, BookInstance, Language, Genre, Author
#admin.site.register(Book)
#admin.site.register(BookInstance)
admin.site.register(Language)
admin.site.register(Genre)
#admin.site.register(Author)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
admin.site.register(Author, AuthorAdmin)

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass