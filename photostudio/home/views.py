from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import  View
from django.template.loader import render_to_string
# Create your views here.


class HomeStartView(View):
    def get(self, request):
        template = render_to_string('index.html')
        return HttpResponse(template)


class ScheduletView(View):
    def get(self, request):
        template = render_to_string('try_schedule.html')
        return HttpResponse(template)