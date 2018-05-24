from django.contrib import admin
from . import models
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

@admin.register(models.Book) #does the same thing as admin.site.register
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')


admin.site.register(models.Author, AuthorAdmin)
# admin.site.register(models.Book)
# admin.site.register(models.BookInstance)
admin.site.register(models.Genre)
