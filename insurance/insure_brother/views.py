from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from django.views.generic import ListView

from .query import get_services
#from .filter import ServiceFilter
from .models import Service

from .form import Filtration


class Home(ListView):
    '''
    Главная страница
    '''
    model = Service
    template_name = 'insure_brother/home.html'
    context_object_name = 'services'


    def get_queryset(self):
        '''
        фильтрует по выбранным параметрам
        '''
        filter = Filtration(data=self.request.GET)
        return filter.filter(super().get_queryset())

    def get_context_data(self, **kwargs):
        '''
        создает форму фильтрации
        '''
        context = super(Home, self).get_context_data(**kwargs)
        context['form'] = Filtration(data = self.request.GET)
        return context

"""

def home(request):
    services = get_services()
    form
    filter_backends = (DjangoFilterBackend)
    current_filter = ServiceFilter(request.GET, queryset=Service.objects.all() )
    context = {
        'services': services,
        'filter': current_filter,
    }
    return render(request, 'insure_brother/home.html', context)
"""
def admin(request):
    pass