from django.contrib import admin

# Register your models here.

from .models import Share

class ShareAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'industry')
    fields = ['code', 'name', 'industry']

from .models import YearReport

class YearReportAdmin(admin.ModelAdmin):
    list_display = ('share', 'earn_per_share', 'income', 'income_yoy', 'income_qoq', 'net_profits', 'net_profits_yoy', 'net_profits_qoq', 'net_asset_per_share', 'roe', 'cash_per_share', 'gross_rate', 'distribution', 'publish_date')
    fieldsets = [
        ('Share information',               {'fields': ['share', 'earn_per_share']}),
        ('Income information', {'fields': ['income', 'income_yoy', 'income_qoq']}),
        ('Net profits information', {'fields': ['net_profits', 'net_profits_yoy', 'net_profits_qoq']}),
        ('Others information', {'fields': ['net_asset_per_share', 'roe', 'cash_per_share', 'gross_rate', 'distribution', 'publish_date']}),
    ]

admin.site.register(Share, ShareAdmin)
admin.site.register(YearReport, YearReportAdmin)