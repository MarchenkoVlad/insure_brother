from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date_creat = models.DateField(verbose_name="Дата создания компании")

    def __str__(self):
        return self.name


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, verbose_name="Название услуги")

    CHOICES = [
        ('life', 'Страхование жизни'),
        ('health', 'Страхование здоровья'),
        ('property', 'Страхование недвижимости'),
        ('OSAGO', 'ОСАГО'),
        ('CASCO', 'КАСКО')
    ]
    category = models.CharField(verbose_name="Вид услуги", max_length=50, choices=CHOICES)
    min_term = models.IntegerField(verbose_name="Срок страхования от (мес)")
    min_price = models.IntegerField(verbose_name="Cтоимость услуги от")
    min_payment = models.IntegerField(verbose_name="Сумма выплат от")
    max_payment = models.IntegerField(verbose_name="Сумма выплат до")
    description = models.CharField(max_length=400)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name="Имя")
    phone = PhoneNumberField(null=False, blank=False, verbose_name="Номер телефона")
    email = models.EmailField(max_length=150)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Вид услуги")
    data_time = models.DateTimeField(default=datetime.now, blank=True, verbose_name="Дата и время")

