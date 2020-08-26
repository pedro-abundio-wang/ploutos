from django.db import models

# Create your models here.

class Share(models.Model):
    code = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=16)
    industry = models.CharField(max_length=16)
    def __str__(self):
        return self.code

    
class YearReport(models.Model):
    share = models.ForeignKey(Share, to_field='code', on_delete=models.CASCADE)
    earn_per_share = models.CharField(max_length=16)
    income = models.CharField(max_length=16)
    income_yoy = models.CharField(max_length=16)
    income_qoq = models.CharField(max_length=16)
    net_profits = models.CharField(max_length=16)
    net_profits_yoy = models.CharField(max_length=16)
    net_profits_qoq = models.CharField(max_length=16)
    net_asset_per_share = models.CharField(max_length=16)
    roe = models.CharField(max_length=16)
    cash_per_share = models.CharField(max_length=16)
    gross_rate = models.CharField(max_length=16)
    distribution = models.CharField(max_length=16)
    publish_date = models.CharField(max_length=16)
