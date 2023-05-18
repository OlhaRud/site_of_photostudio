# Create your views here.
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views import View
from django.utils.safestring import mark_safe
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect
from .models import *
from .utils import Calendar
from datetime import date
from .forms import EventForm


class CalendarView(generic.ListView):
    model = Event
    template_name = 'try_schedule.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = self.get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['event_form'] = EventForm()
        return context

    def get_date(self, req_day):
        if req_day:
            year, month = (int(x) for x in req_day.split('-'))
            return date(year, month, day=1)
        return datetime.today()
    
    class EventView(generic.ListView):
        model = Event
        template_name = 'try_schedule.html'


class EventView(View):

    def post(self, request):
        post = request.POST
        title = post.get('title')
        lastname = post.get('lastname')
        firstname = post.get('firstname')
        phonenumber = post.get('phonenumber')
        email = post.get('email')
        datebegin = post.get('datebegin')
        dateend = post.get('dateend')
        description = post.get('description')
        event, create = Event.objects.update_or_create(title=title, lastname=lastname, firstname=firstname,
                                                       phonenumber=phonenumber, email=email, start_time=datebegin,
                                                       end_time=dateend, description=description, user=request.user
                                                      )
        return redirect('schedule')

