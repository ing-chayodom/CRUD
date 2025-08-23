from django.contrib import admin
from .models import InspectionRecord

@admin.register(InspectionRecord)
class InspectionAdmin(admin.ModelAdmin):
    list_display = ('inspection_no', 'product_code', 'smell', 'ph', 'status', 'created_at')
    search_fields = ('inspection_no', 'product_code', 'smell', 'status')
    list_filter = ('status',)