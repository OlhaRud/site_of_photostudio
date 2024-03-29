from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200, null=True)
    firstname = models.CharField(max_length=200, null=True)
    phonenumber = models.CharField(verbose_name=_('Phone Number'), null=True, blank=True, default=1, max_length=18)
    email = models.EmailField(max_length=200, null=True)
    hall = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return '{} {}'.format(self.title, self.start_time)
    

class Hour(models.Model):
    booking_hour = models.CharField(max_length=512)
    booking_hour1 = models.CharField(max_length=512)


    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})



class Day(models.Model):

    

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
