from django.contrib import admin
from .models import Product, Order
from django.contrib.auth.models import Group



admin.site.site_header = "Inventory Management"
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'category')
    search_fields = ('category',)
    list_filter = ('name',)
    ordering = ('-created_at',)
    list_per_page = 10
    #list_editable = ('quantity',)

# Register your models here.
admin.site.register(Product, ProductAdmin)

admin.site.register(Order)
    # list_display = ('product', 'user', 'order_quantity', 'order_date')
    # search_fields = ('user__username',)
    # list_filter = ('product__category',)
    # ordering = ('-order_date',)
    # list_per_page = 10
# Unregister the Group model from the admin site
admin.site.unregister(Group)


