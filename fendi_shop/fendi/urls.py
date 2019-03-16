from django.urls import path
from .views import StartView

app_name = 'fendi'

urlpatterns = [
    path('', StartView.as_view(), name='index'),
]
