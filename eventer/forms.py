from django import forms
from django.db import models
from .widget import DatePickerInput, TimePickerInput, DateTimePickerInput
from .models import Event

class EventForm(forms.Form):
    name=forms.CharField(label='Name',max_length=100)
    description=forms.CharField(label="Description",max_length=255,widget=forms.Textarea)
    date=forms.DateField(label='Date',widget=DatePickerInput)
    time=forms.TimeField(label='time',widget=TimePickerInput)
    image=forms.ImageField(label='Image')
    address1=forms.CharField(label='Address Line 1', max_length=150)
    address2=forms.CharField(label='Address Line 2', max_length=150)
    city=forms.CharField(label='city',max_length=100)
    zip_code=forms.CharField(label='Zip Code', max_length=10)
