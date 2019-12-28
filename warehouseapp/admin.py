from django.contrib import admin
from .models import Product, Transaction

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'price', 'quantity']

class TransactionAdmin(admin.ModelAdmin):
	list_display = ['product', 'operation','timestamp','object_id']
	list_filter = ('product','timestamp',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Transaction, TransactionAdmin)
