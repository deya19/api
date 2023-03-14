from django.contrib import admin
from .models import Author, Book


admin.site.site_header = "My Site Administration"

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)

class BookAdmin(admin.ModelAdmin):
    list_display = ("title","author")

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
