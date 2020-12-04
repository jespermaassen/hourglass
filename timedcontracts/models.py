from django.db import models

# Create your models here.
class Market(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ticker = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name} - {self.ticker}'
    
class Contract(models.Model):
    contract_type = models.CharField(max_length=100, choices=[('LONG', "SHORT")])
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    size = models.FloatField()
    date_open = models.DateTimeField(auto_now_add=True)
    date_close = models.DateTimeField(null=True)
    status = models.CharField(max_length=100, default='OPEN')
    result = models.FloatField(null=True)

    def __str__(self):
        return f'{self.contract_type} | {self.size} | {self.date_open} | {self.date_close}'
