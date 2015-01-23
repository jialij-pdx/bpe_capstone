from django import forms
from django.forms.widgets import SplitDateTimeWidget, SelectMultiple


STATION_CHOICES = (('station1', 'Station1'),
                   ('station1', 'Station2'),
                   ('station3', 'Station3'))


# The query form attributes
class QueryForm(forms.Form):
    query_name = forms.CharField(label='Name Your Query', max_length=100)
    start_date_time = forms.DateTimeField(label='Start Date/Time', widget=SplitDateTimeWidget)
    end_date_time = forms.DateTimeField(label='End Date/Time', widget=SplitDateTimeWidget)
    stations = forms.CharField(label='Stations', widget=forms.Select(choices=STATION_CHOICES))