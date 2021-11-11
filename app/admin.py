from django.contrib import admin
from .models import Purchases


class AdminPurchases(admin.ModelAdmin):
    list_display = ('id', 'user', 'money', 'date')
    list_display_links = ('id',)
    search_fields = ('id', 'user', 'money', 'date')
    list_editable = ('user', 'money', 'date')
    list_filter = ('date',)


admin.site.register(Purchases, AdminPurchases)
