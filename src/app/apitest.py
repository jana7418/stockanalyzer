from nse import NSELiveAPI

stock = NSELiveAPI('INDUSINDBK')
print(stock.get_order_book())