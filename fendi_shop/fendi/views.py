import subprocess
import redis
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import ItemShop

# Create your views here.


class StartView(View):
    r = redis.Redis(host='localhost', port=6379)
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name)

    def post(self, request, *args, **kwargs):
        url = self.request.POST.get('url_scrapy')
        self.r.lpush('fendi:start_urls', url)
        #subprocess.call(['redis-cli', 'lpush', 'fendi:start_urls', url])
        context = {'message': 'Please wait scraping process is running'}
        return render(self.request, self.template_name, context)


class ItemShopListView(ListView):

    model = ItemShop
    template_name = 'shop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_list'] = ItemShop.objects.all()
        return context  
