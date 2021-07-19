from .models import Company, Service, Customer

def get_services ():
    services = Service.objects.all()
    return services