from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    list_display = ('town', 'address', 'price', 'construction_year', 'new_building',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony', )
    list_per_page = 15
    readonly_fields = ['created_at', ]
    search_fields = ['town', 'address', 'owner']


admin.site.register(Flat, FlatAdmin)
