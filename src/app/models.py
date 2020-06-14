from django.db import models
from .nse import NSELiveAPI
from django.contrib import messages
from django.http import HttpResponse, request

class Index(models.Model):
    name = models.CharField(max_length=100, name='Name', null=False, unique=True)

    def __str__(self):
        return (self.Name)

class Stock(models.Model):
    EXCHANGES = (
        ('NSE', 'NSE'),
        ('BSE', 'BSE')
    )
    symbol = models.CharField(max_length=100, name='Symbol', null=False)
    exchange = models.CharField(name='Exchange', max_length=3, choices=EXCHANGES, null=False, default='NSE')
    index = models.ForeignKey(Index, on_delete=models.CASCADE)
    active = models.BooleanField(name='Active', default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['Symbol', 'Exchange'], name='Unique Stock')
        ]

    def nse(self):
        return NSELiveAPI(self.Symbol)

    def get_buy_sell_quantity(self):
        orderbook = self.nse().get_order_book()
        print(orderbook)
        if orderbook is not None:
            ret = {
                'buy' : orderbook.get('totalBuyQuantity'),
                'sell' : orderbook.get('totalSellQuantity'),
            }
            return ret
        else:
            return {
                'buy' : 0,
                'sell' : 0,
                'bid' : 0,
                'ask' : 0,
            }

    def __str__(self):
        return self.Symbol + " (" + self.Exchange + ")"
