from django.urls import path
from . import views

urlpatterns = [
    path("", views.stocks_list),
    path("api/get/index/<id>", views.get_stocks_api),
    path("api/get/stock/<symbol>", views.get_live_api),
]