from django.contrib import admin

from .models import Flat, Complaint


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat',)
    raw_id_fields = ('user', 'flat',)


class FlatAdmin(admin.ModelAdmin):
    list_display = ('town', 'address', 'price', 'construction_year', 'new_building',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    list_per_page = 15
    raw_id_fields = ('liked_by',)
    readonly_fields = ['created_at', ]
    search_fields = ['town', 'address', 'owner', ]


admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Flat, FlatAdmin)
