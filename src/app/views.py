from django.shortcuts import render
from django.http import HttpResponse, request
from django.contrib import messages
from .models import Stock, Index
import json
from .nse import NSELiveAPI
import html

# Create your views here.

def root_view(request):
    return render(request, 'index.html')

def stocks_list(request):
    stocks = Stock.objects.exclude(Active=False)
    indexes = Index.objects.all()
    return render(request, 'stocks.lister.html', {
        'stocks' : stocks,
        'indexes' : indexes
    })

def get_stocks_api(request, id):
    stocks = Stock.objects.filter(Active=True, index__id=id)
    data = {}
    symbols = []
    for stock in stocks:
        symbols.append(stock.Symbol)
    data['symbols'] = symbols
    return HttpResponse(json.dumps(data), content_type='application/json')

def get_stock_view_data(stock : Stock):
    data = {}
    data['symbol'] = stock.Symbol
    data['exchange'] = stock.Exchange
    livedata = stock.get_buy_sell_quantity()
    
    buy = int(livedata.get('buy')) if livedata.get('buy') is not None else 0
    sell = int(livedata.get('sell')) if livedata.get('sell') is not None else 0

    percent = ((buy - sell) / 1 if sell == 0 else sell ) * 100
    data['data'] = {
        'quantity' : livedata,
        'percent' : percent,
        'percent_cell_colour' : 'bg-success' if buy > sell else 'bg-danger',
    }
        
    return data

def get_live_api(request, symbol):
    symbol = html.escape(symbol)
    stock = Stock.objects.filter(Symbol=symbol)
    data = {}
    data['symbol'] = symbol
    if stock:
        stock = stock.get()
        data = get_stock_view_data(stock)
    return HttpResponse(json.dumps(data), content_type='application/json')
