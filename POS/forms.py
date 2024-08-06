from django import forms
from .models import *

from datetime import datetime , date
# forms.py
# from django.forms import formset_factory

# class DynamicProductForm(forms.Form):
#     product = forms.ModelChoiceField(queryset=products.objects.all(), label='Product')
#     azen = forms.CharField()
#     reminder_quantity = forms.CharField()
#     total_quantity = forms.CharField()

# DynamicProductFormSet = formset_factory(DynamicProductForm,absolute_max=1500)



class ProductForm(forms.Form):
    product_name_choices = ProductMetadata.objects.values_list('name','name').all()
    product_name = forms.ChoiceField(choices=product_name_choices, label='اسم المنتج' , widget=forms.Select(attrs={'class': 'form-select'}))
    azen = forms.IntegerField(label='رقم الأذن', widget=forms.TextInput(attrs={'class': 'form-control' , 'id' : 'id_azen'}))
    expiry_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date' , 'class' : 'form-control' ,'id' : 'id_expiry_date'}),label='تاريخ انتهاء الصلاحية')
    total_quantity = forms.DecimalField(label='كمية المنتج بالجرام' , widget=forms.TextInput(attrs={'class': 'form-control' , 'id' : 'id_total_quantity'}))
    

DAYS_OF_WEEK = [('السبت', 'السبت'),('الاحد', 'الاحد'),('الاتنين', 'الاتنين'),('الثلاثاء', 'الثلاثاء'),('الاربعاء', 'الاربعاء'),('الخميس', 'الخميس'),('الجمعة', 'الجمعة')]
SEASONS = [('صيف', 'صيف'), ('شتاء', 'شتاء'), ('رمضان', 'رمضان')]
LOCATIONS = [('جاف عادي', 'جاف عادي'),('جاف سيناء', 'جاف سيناء')]
TARFEH_CHOICES = [
    ("بسكويت أولكر(بلح)", "بسكويت أولكر(بلح)"),
    ("بسكويت بسكريم(بالشيكولاته)", "بسكويت بسكريم(بالشيكولاته)"),
    ("بسكويت ويفر", "بسكويت ويفر"),
    ("تونه ترفيه أفراد ومجندين", "تونه ترفيه أفراد ومجندين"),
    ("تونه ترفيه ضباط", "تونه ترفيه ضباط"),
    ("مياه معدنية ترفيه", "مياه معدنية ترفيه"),
    ("عصير ترفيه", "عصير ترفيه"),
]
MEAL_CHOICES = [
        ('وجبة التعيين', 'وجبة التعيين'),
        ('وجبة لحوم', 'وجبة لحوم'),
        ('وجبة دواجن', 'وجبة دواجن'),
        ('وجبة بدون', 'وجبة بدون'),
]


class TazaForm(forms.Form):
    workers_count = forms.IntegerField(label='عدد الافراد' , widget=forms.TextInput(attrs={'class': 'form-control'}))
    recruits_count = forms.IntegerField(label='عدد المجندين' , widget=forms.TextInput(attrs={'class': 'form-control'}))
    officers_count = forms.IntegerField(label='عدد الضباط', widget=forms.TextInput(attrs={'class': 'form-control'}))
    azen = forms.IntegerField(label='رقم الأذن', widget=forms.TextInput(attrs={'class': 'form-control'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date' , 'class' : 'form-control' }),label="تاريخ الصرف" , initial= date.today())
    season = forms.ChoiceField(choices= SEASONS, label='الموسم', widget=forms.Select(attrs={'class': 'form-select' }))
    day = forms.ChoiceField(choices = DAYS_OF_WEEK, label='اليوم' , widget=forms.Select(attrs={'class': 'form-select'}))
    wagba = forms.ChoiceField(choices = MEAL_CHOICES ,label = 'نوع الوجبة' , widget=forms.Select(attrs={'class': 'form-select'}))

class GafaForm(forms.Form):
    task_duration = forms.IntegerField(label='عدد ايام المأمورية' , widget=forms.TextInput(attrs={'class': 'form-control'}))
    worker_count = forms.IntegerField(label = 'عدد الافراد' , widget=forms.TextInput(attrs={'class': 'form-control'}))
    recruit_count = forms.IntegerField(label = 'عدد الجنود' , widget=forms.TextInput(attrs={'class': 'form-control'}))
    officer_count = forms.IntegerField(label = 'عدد الضباط' , widget=forms.TextInput(attrs={'class': 'form-control'}))
    azen = forms.IntegerField(label = 'رقم الاذن' , widget=forms.TextInput(attrs={'class': 'form-control'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date' , 'class' : 'form-control'}),label="تاريخ الصرف" , initial= date.today())
    location = forms.ChoiceField(choices= LOCATIONS, label='مكان المأمورية', widget=forms.Select(attrs={'class': 'form-select' }))

class TarfehForm(forms.Form):
    worker_count = forms.IntegerField(label = 'عدد الافراد' , widget=forms.TextInput(attrs={'class': 'form-control'}))
    recruit_count = forms.IntegerField(label = 'عدد الجنود' , widget=forms.TextInput(attrs={'class': 'form-control'}))
    officer_count = forms.IntegerField(label = 'عدد الضباط' , widget=forms.TextInput(attrs={'class': 'form-control'}))
    azen = forms.IntegerField(label = 'رقم الاذن' , widget=forms.TextInput(attrs={'class': 'form-control'}))
    quantity = forms.DecimalField(label='الكمية' ,widget=forms.TextInput(attrs={'class': 'form-control'}) )
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date' , 'class' : 'form-control'}),label="تاريخ الصرف" , initial= date.today())
    product_name = forms.ChoiceField(choices=TARFEH_CHOICES , label = 'نوع المنتج' , widget = forms.Select(attrs={'class':'form-select'}))

class MortgaaForm(forms.Form):
    azen = forms.IntegerField(label = 'رقم الاذن' , widget=forms.TextInput(attrs={'class': 'form-control'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date' , 'class' : 'form-control'}),label="تاريخ الارجاع" , initial= date.today())
