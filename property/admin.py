from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    list_display = ('town', 'address', 'owner', 'price', 'rooms_number', 'active')
    search_fields = ['town', 'address', 'owner']
    list_per_page = 15


admin.site.register(Flat, FlatAdmin)
