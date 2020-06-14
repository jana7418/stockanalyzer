from django.contrib import admin
from .models import Stock, Index

# Register your models here.

class StockAdmin(admin.ModelAdmin):
    pass

class IndexAdmin(admin.ModelAdmin):
    pass

admin.site.register(Stock, StockAdmin)
admin.site.register(Index, IndexAdmin)