from django.contrib import admin
from .models import product


@admin.register(product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'price', 'status', 'created_at')
	list_filter = ('status', 'created_at')
	search_fields = ('name', 'description')
