import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Place(models.Model):
    #Dane miejsca zawodow
    name = models.CharField(max_length=75)
    adress = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Category(models.Model):
    #Rodzaj zawodow - mecz towarzyski, ligowy, pucharowy
    name = models.CharField(max_length=75)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u"Category"
        verbose_name_plural = u"Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

class Event(models.Model):
    #Wydarzenie
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name

    home_team_goals = models.CharField(max_length=5, default=0)
    away_team_goals = models.CharField(max_length=5, default=0)
    date = models.DateField()
    starts = models.TimeField(blank=True, null=True)
    ends = models.TimeField(blank=True, null=True)
    price = models.CharField(max_length=20)
    place = models.ForeignKey(Place)
    category = models.ForeignKey(Category)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
