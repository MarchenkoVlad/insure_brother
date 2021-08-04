from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, CreateView
from django.contrib.auth import logout
from django.conf import settings

from .query import get_services, get_all_company_user_by_service_id
from .models import Service, Customer
from .form import Filtration, CustomerForm
from .elastic import search
from insurance import celery



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
        search_query = self.request.GET.get('search')

        context = super(Home, self).get_context_data(**kwargs)

        if search_query:
            context_object_name = search(search_query)
            context['services'] = context_object_name.to_queryset()

        context['form'] = Filtration(data = self.request.GET)
        return context


def create_customer_form(request):
    """запускает проверку валидности, создает клиента в БД и отправляет информацию сотруднику компании о создании"""
    form = CustomerForm(request.POST)
    if form.is_valid():
        subject = "Новый клиент"
        message = f"У вас новая заявка от клиента. Информация о клиенте: \
          имя: {form.data.get('name')} \
          телефон: {form.data.get('phone')} \
          email: {form.data.get('email')}"
        email_from = settings.EMAIL_HOST_USER  
        recipient_list = get_all_company_user_by_service_id(form.data.get('id'))
        form.save()
        celery.send_task_email.delay(subject, message, email_from, recipient_list)
        return HttpResponse("Данные получены")
    else:
        return HttpResponse("Ошибки в формате данных")


def user_logout(request):
    '''
    выход из аккаунта
    '''
    logout(request)
    return redirect("home")


class Register(CreateView):
    template_name = 'register.html'
    

def admin_company(request):
    return redirect("insure_brother/admin_company.html")