from django.shortcuts import render
from django.views import View
import redis

# Create your views here.

class StartView(View):

    template_name = 'index.html'

    def __init__(self):
    	self.r = redis.Redis(host='localhost', port=6379) 


    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name)

    def post(self, request, *args, **kwargs):
    	url = self.request.

