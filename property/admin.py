from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    list_display = ('town', 'address', 'owner', 'price', 'rooms_number', 'active')
    list_per_page = 15
    readonly_fields = ['created_at', ]
    search_fields = ['town', 'address', 'owner']


admin.site.register(Flat, FlatAdmin)
