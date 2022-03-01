from dataclasses import fields
import django_filters
from .models import Content
from django import forms
from django.contrib.admin.widgets import AdminDateWidget


class DateInput(forms.DateInput):
    input_type = 'date'



class ContentFilter(django_filters.FilterSet):

    is_published = django_filters.BooleanFilter(method='content_is_published')
    content_title = django_filters.CharFilter(label='Title',lookup_expr='icontains')
    created_at = django_filters.DateFilter(label='Date', lookup_expr='contains', widget=DateInput())
    
    





    
    class Meta:
        model=Content
        fields= ["content_title","created_at"]


    def content_is_published(self, queryset, name, value):
        return queryset.filter(published ="True")


            
