from django.db import models

# Create your models here.
class Market(models.Model):
    name = models.CharField(max_length=100)
    ticker = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} - {self.ticker}'
    
class Contract(models.Model):
    contract_type = models.CharField(max_length=100)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    size = models.FloatField()
    date_open = models.DateTimeField('contract start date')
    date_close = models.DateTimeField('contract expiry date')
    status = models.CharField(max_length=100)
    result = models.FloatField()

    def __str__(self):
        return f'{self.contract_type} | {self.size} | {self.date_open} | {self.date_close}'
