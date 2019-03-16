from django.urls import path
from .views import StartView, ItemShopListView

app_name = 'fendi'

urlpatterns = [
    path('', StartView.as_view(), name='index'),
    path('shop_list', ItemShopListView.as_view(), name='shop_list'),
]
