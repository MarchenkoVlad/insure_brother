import copy
import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

from .models import Service, Company, Customer

class Filtration (forms.Form):
    """ фильтрация услуг"""
    def add_all_fields_for_selection(list_choices):
        """функция добавляет для выбора все имеющиеся поля """
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(list_choices)
        final_result = [("Все", "Все")]
        for one_choice in list_choices:
            final_result.append(one_choice)
        return final_result

    
    category = forms.ChoiceField(label = "Вид услуги",
                                choices = add_all_fields_for_selection(list(map(lambda one_services: (one_services.category, one_services.category), Service.objects.all()))))
    
    min_term = forms.IntegerField(label = "Срок страхования от (мес)", min_value = 1,
                                       required=False) 
    min_price = forms.IntegerField(label = "Cтоимость услуги (руб) от", min_value = 1,
                                       required=False)
    min_payment = forms.IntegerField(label = "Сумма выплат (руб) от", min_value = 1,
                                       required=False)
    max_payment = forms.IntegerField(label = "Сумма выплат (руб) до", min_value = 1,
                                       required=False)

    price_sorted = forms.ChoiceField(label = "Сортировка по стоимости услуги",
                                     choices = [("по возрастанию", "по возрастанию"), ("по убыванию", "по убыванию")])

    class Meta:
        model = Service
        fields = ('category', 'min_term', 'min_price', 'min_payment', 'max_payment', 'description', 'company' )

    def filter(self, qs, ):
        """ функция для фильтрации услуг """

        #вид услуги
        try: 
            if self.data.get('category') != 'Все':
                qs = qs.filter(category = Service.objects.get(name = self.data.get('type')))
        except Exception:
            pass
       
        #срок страхования
        if self.data.get('min_term') != None and self.data.get('min_term') != "":
            number_term = int(self.data.get('min_term'))
            sorted_list = list((i for i in copy.copy(qs) if i.min_term > number_term))
            for id, one_good_qs in enumerate(sorted_list):
                if id == 0:
                    qs = qs.filter(id=-1)
                qs = qs | Service.objects.filter(id = one_good_qs.id)
            if len(sorted_list) == 0:
                qs = qs.filter(id=-1)

        #минимальная стоимость
        if self.data.get('min_price') != None and self.data.get('min_price') != "":
            number_price = int(self.data.get('min_price'))
            sorted_list = list((i for i in copy.copy(qs) if i.min_price > number_price))
            for id, one_good_qs in enumerate(sorted_list):
                if id == 0:
                    qs = qs.filter(id=-1)
                qs = qs | Service.objects.filter(id = one_good_qs.id)
            if len(sorted_list) == 0:
                qs = qs.filter(id=-1)
        
        #минимальная выплата
        if self.data.get('min_payment') != None and self.data.get('min_payment') != "":
            number_min_payment = int(self.data.get('min_payment'))
            sorted_list = list((i for i in copy.copy(qs) if i.min_payment > number_term))
            for id, one_good_qs in enumerate(sorted_list):
                if id == 0:
                    qs = qs.filter(id=-1)
                qs = qs | Service.objects.filter(id = one_good_qs.id)
            if len(sorted_list) == 0:
                qs = qs.filter(id=-1)
        
        #максимальная выплата
        if self.data.get('max_payment') != None and self.data.get('max_payment') != "":
            number_max_payment = int(self.data.get('max_payment'))
            sorted_list = list((i for i in copy.copy(qs) if i.max_payment > number_max_payment))
            for id, one_good_qs in enumerate(sorted_list):
                if id == 0:
                    qs = qs.filter(id=-1)
                qs = qs | Service.objects.filter(id = one_good_qs.id)
            if len(sorted_list) == 0:
                qs = qs.filter(id=-1)

        #сортировка по минимальной стоимости
        if self.data.get('price_sorted') == "по возрастанию":
            return qs.order_by("min_price")
        else:
            return qs.order_by("-min_price")