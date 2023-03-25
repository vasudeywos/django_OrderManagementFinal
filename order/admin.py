from django.contrib import admin
from .models import Orders

@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Order_Number', 'get_tags']

    def get_tags(self, obj):
        return ", ".join(o for o in obj.tags.names())