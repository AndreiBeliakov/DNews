from django_filters import FilterSet, DateFilter
from .models import New
from django import forms

class NewFilter(FilterSet):
    created__gt = DateFilter(
        field_name='created',
        label = 'published not earlier:',
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        ),
        lookup_expr='date__gte'
    )
    class Meta:
        model = New
        fields = {
            'name': [('icontains')],

            'author': ['exact'],
        }