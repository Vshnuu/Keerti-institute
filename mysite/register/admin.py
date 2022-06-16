from django.contrib import admin

# Register your models here.
from . models import Product
from . models import Client

admin.site.register(Product)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    ordering = ('name',)
    search_fields = ('name', 'phone')