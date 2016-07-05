from book.models import Page
from django.contrib import admin

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Page, PageAdmin)