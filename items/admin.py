from unfold.admin import ModelAdmin
from django.contrib.admin import StackedInline
from django.contrib import admin
from .models import Item, Order, Discount, Tax

@admin.register(Item)
class ItemAdmin(ModelAdmin):
    list_display = ('name', 'price', 'currency', 'description_short')
    list_filter = ('currency',)
    search_fields = ('name', 'description')
    
    def description_short(self, obj):
        if len(obj.description) > 50:
            return f'{obj.description[:50]}...'
        return obj.description
    description_short.short_description = 'Description'

@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = ('id', 'total_price', 'items_count')
    filter_horizontal = ('items',)
    
    def items_count(self, obj):
        return obj.items.count()
    items_count.short_description = 'Number of Items'

class DiscountInline(StackedInline):
    model = Discount
    extra = 0
    max_num = 1

class TaxInline(StackedInline):
    model = Tax
    extra = 0
    max_num = 1

# Добавляем инлайны к OrderAdmin
OrderAdmin.inlines = [DiscountInline, TaxInline]

@admin.register(Discount)
class DiscountAdmin(ModelAdmin):
    list_display = ('order', 'percent_off', 'stripe_coupon_id')
    list_filter = ('percent_off',)

@admin.register(Tax)
class TaxAdmin(ModelAdmin):
    list_display = ('order', 'percentage', 'stripe_tax_id')
    list_filter = ('percentage',)