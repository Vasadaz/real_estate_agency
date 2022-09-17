from django.contrib import admin

from .models import Flat, Complaint, Owner


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat',)
    raw_id_fields = ('user', 'flat',)


class OwnerInstanceInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ('owner',)


class FlatAdmin(admin.ModelAdmin):
    inlines = [OwnerInstanceInline]
    list_display = (
        'town',
        'address',
        'price',
        'construction_year',
        'new_building',
    )
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    list_per_page = 15
    raw_id_fields = ('liked_by',)
    readonly_fields = ['created_at', ]
    search_fields = ['town', 'address', ]


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)


admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Flat, FlatAdmin)
admin.site.register(Owner, OwnerAdmin)
