from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)

    CHOICES = [
        ('life', 'Страхование жизни'),
        ('health', 'Страхование здоровья'),
        ('property', 'Страхование недвижимости'),
        ('OSAGO', 'ОСАГО'),
        ('CASCO', 'КАСКО')
    ]
    category = models.CharField(max_length=50, choices=CHOICES)
    min_term = models.IntegerField()
    min_payment = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, help_text='Укажите Ваше имя')
    lastname = models.CharField(max_length=30, help_text='Укажите Вашу фамилию')
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(max_length=150)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True) #как сохранить данные, если компания удалит услугу? а пользователь не должен быть
