# Create your views here.
from datetime import datetime
from django.shortcuts import render

from django.views import generic
from django.views import View
from django.utils.safestring import mark_safe
from django.http import JsonResponse
from django.shortcuts import redirect
from .models import *
from .utils import Calendar
from .forms import EventForm
from datetime import date


class CalendarView(generic.ListView):
    model = Event
    template_name = 'booking.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = self.get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)

        return context

    def get_date(self, req_day):
        if req_day:
            year, month = (int(x) for x in req_day.split('-'))
            return date(year, month, day=1)
        return datetime.today()
    

# class EventView(generic.ListView):
#     model = Event
#     template_name = 'try_schedule.html'


class EventView(View):

    def post(self, request):
        post = request.POST
        id_pk = post.get('id_pk')
        if id_pk is None:
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
                                                           end_time=dateend, description=description, user=request.user)
        else:
            event = Event.objects.get(pk=id_pk)
            post = request.POST
            event.title = post.get('title')
            event.lastname = post.get('lastname')
            event.firstname = post.get('firstname')
            event.phonenumber = post.get('phonenumber')
            event.email = post.get('email')
            event.start_time = post.get('datebegin')
            event.end_time = post.get('dateend')
            event.description = post.get('description')
            event.save()
        return redirect('schedule')


class GetEventAJAX(View):
    def post(self, request):
        event = Event.objects.get(pk=request.POST.get('event_id'))
        id_pk = event.pk
        title = event.title
        lastname = event.lastname
        firstname = event.firstname
        phonenumber = event.phonenumber
        email = event.email
        datebegin = event.start_time
        dateend = event.end_time
        description = event.description
        return JsonResponse({'id_pk': id_pk, 'title': title, 'lastname': lastname, 'firstname': firstname, 'phonenumber': phonenumber,
                             'email': email, 'datebegin': datebegin, 'dateend': dateend, 'description': description})

