from dataclasses import fields
import django_filters
from .models import GameUpdates
from django import forms
from django.contrib.admin.widgets import AdminDateWidget


class DateInput(forms.DateInput):
    input_type = 'date'



class GameUpdateFilter(django_filters.FilterSet):

    
    update_title = django_filters.CharFilter(label='Title',lookup_expr='icontains')
    created_at = django_filters.DateFilter(label='Date', lookup_expr='contains', widget=DateInput())
    
    





    
    class Meta:
        model=GameUpdates
        fields= ["update_title","created_at"]


            
