from .models import Company, Service, Customer
from django.contrib.auth.models import User
def get_services ():
    services = Service.objects.all()
    return services


""" 
по id услуги сначала получает название компании, а затем сравнивает название компании 
с названием группы пользователей и возвращает список email
"""
def get_all_company_user_by_service_id(service_id):
    service = Service.objects.filter(id=service_id)
    name_company = service[0].company.name
    emails = User.objects.filter(groups__name=name_company).values_list('email', flat=True)
    
    return list(emails)
