from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.http import HttpResponse , HttpResponseRedirect
from django.db.models import Sum
from .models import *
from .forms import *
from .controllers import *
from django.forms import modelformset_factory
import json
import time
from django.contrib import messages


def success_page_view(request):
    return render(request, 'POS/success_page.html')

def add(request):
    form = ProductForm()
    if request.method == "POST":
        return redirect("success_page")
    return render(request, 'POS/add.html', {'form': form})


def add_all(request):
    data = json.loads(request.body)
    print(data)
    for product in data:
        product_metadata_instance = ProductMetadata.objects.get(name=product['product_name'])
        azen = product['azen']
        if azen == '':
            azen = 0 
        
        expiration_date = product['expiry_date']
        if expiration_date == '':
            expiration_date = date.today()

        quantity = product['total_quantity']
        if product not in included_product_names:
            Product.objects.create(name=product_metadata_instance, azen = azen  , expiration_date = expiration_date , quantity = quantity)
    return JsonResponse({'data':'success'},status=200)

def home(request):
    return render(request ,'POS/home.html')

def sarf(request):
    return render(request ,'POS/sarf.html')

def tarfeh(request):
    form = TarfehForm()
    if request.method == "POST":
        time.sleep(1)
        azen_number = request.POST.get('azen')
        return redirect(reverse('tarfeh_report', args=[azen_number]))

    return render(request ,'POS/tarfeh.html' , {'form' : form})

def gafa(request):
    form = GafaForm()
    if request.method == "POST":
        time.sleep(1)
        azen_number = request.POST.get('azen')
        return redirect(reverse('gaf_report', args=[azen_number]))
    
    member_names = Member.objects.values_list('name', flat=True)
    context = {
        'form' : form,
        'member_names_json': json.dumps(list(member_names))  # Convert to JSON string
    }

    return render(request ,'POS/gafa.html' , context)

def taza(request):
    form = TazaForm()
    if request.method == "POST":
        time.sleep(1)
        azen_number = request.POST.get('azen')
        return redirect(reverse('taza_report', args=[azen_number]))
    return render(request, 'POS/Taza.html', {'form': form})

def mortgaa(request):
    form = MortgaaForm()
    if request.method == "POST":
        return redirect("success_page")
    return render(request,'POS\Mortgaa.html' , {'form' : form})

def taza_report(request, azen_number):
    products_data,meta_data = takrer_taza(azen_number)
    return render(request, 'POS/Results.html', {'meta_data':meta_data,"products_data":products_data})

def gaf_report(request, azen_number):
    products_data , members = takrer_gaf(azen_number)

    return render(request, 'POS/Results.html', {'products_data': products_data ,'members' : members})

def tarfeh_report(request, azen_number):
    products_data = takrer_tarfeh(azen_number)
    return render(request, 'POS/Results.html', {'products_data': products_data})

def takarer(request):
    if request.method == "POST":
        takrer_type = request.POST.get('takrer_type')
        azen_number = request.POST.get('azen_number')

        if takrer_type == 'تقرير صرف طازة':
            return redirect(reverse('taza_report', args=[azen_number]))

        elif takrer_type == 'تقرير صرف جاف':
            return redirect(reverse('gaf_report', args=[azen_number]))

        elif takrer_type == 'تقرير صرف ترفيه':
            return redirect(reverse('tarfeh_report', args=[azen_number]))

    return render(request, 'POS/takarer.html')

def taza_sarf(request):
    data = json.loads(request.body)
    print(data)
    if issue_taza_products(data['season'] , data['day'] , int(data['officers_count']),int(data['recruits_count']), int(data['workers_count']) , int(data['azen']) , data['date'] , data['wagba']):
        return JsonResponse({'data': 'success' , 'azen' : data['azen']}, status=200)
    else :
        return JsonResponse({'data': 'quantity not enough'}, status=500)

def gaf_sarf(request):
    data = json.loads(request.body)
    print(data)
    if issue_gaf_products(int(data['worker_count']),int(data['recruit_count']),int(data['officer_count']),int(data['azen']),data['date'],data['location'] , int(data['task_duration']) ,data['members']):
        print(data['members'])
        return JsonResponse({'data': 'success'}, status=200)
    else :
        return JsonResponse({'data': 'quantity not enough'}, status=500)
    
def tarfeh_sarf(request):
    data = json.loads(request.body)
    print(data)
    if issue_tarfeh_products(int(data['officer_count']) ,int(data['recruit_count']),int(data['worker_count']) ,int(data['azen']),int(data['quantity']) , data['date'] , data['product_name']):
        return JsonResponse({'data': 'success'}, status=200)
    else :
        return JsonResponse({'data': 'quantity not enough'}, status=500)
    
def mortgaa_handle(request):
    data = json.loads(request.body)
    mortgaaControll(data['date'],data['azen'])
    if data:
        return JsonResponse({'data': 'success'}, status=200)
    else :
        return JsonResponse({'data': 'quantity not enough'}, status=500)



def product_list(request):

    product_names = Product.objects.values_list('name__name', flat=True).distinct()
    products_data = {}
    for name in product_names:
        products = Product.objects.filter(name__name=name)
        total_quantity = products.aggregate(total_quantity=Sum('quantity'))['total_quantity']
        products_data[name] = []
        

        for product in products:
            products_data[name].append({'product': product, 
                               'azen' : convert_to_hindi_numbers(product.azen),
                               'expiration_date' : convert_to_arabic_date(product.expiration_date),
                               'quantity' : convert_to_hindi_numbers(product.quantity),
                               'total_quantity' : convert_to_hindi_numbers(total_quantity)
                               })
    return render(request, 'POS/raseed.html', {'products_data': products_data })


def Motaahed(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        print(start_date,end_date)
        column_names = ['زبادى','خضار_مجمد', 'سلاطه', 'فاكهه', 'ثوم', 'بصل_ناشف', 'بهارات', 'بيض', 'لحوم_مجمده','دواجن_مجمده']
        products_data = {}
        new_products_data = {}
        products = TazaMonsaraf.objects.filter(date__range=[start_date, end_date])
        products_data = {name: 0 for name in column_names}
        final_dict = {}
        date_dict=[]
        if '-' in start_date:
            # Splitting the year and month
            year, month, day= start_date.split('-')  # Using the * operator to catch extra values

            # Dictionary mapping English numbers to Arabic numbers
            arabic_numbers = {'0': '٠', '1': '١', '2': '٢', '3': '٣', '4': '٤', '5': '٥', '6': '٦', '7': '٧', '8': '٨', '9': '٩'}
            # List of Arabic month names
            arabic_months = {
                '01': 'يناير',
                '02': 'فبراير',
                '03': 'مارس',
                '04': 'أبريل',
                '05': 'مايو',
                '06': 'يونيو',
                '07': 'يوليو',
                '08': 'أغسطس',
                '09': 'سبتمبر',
                '10': 'أكتوبر',
                '11': 'نوفمبر',
                '12': 'ديسمبر'
            }

            # Get the Arabic month name
            arabic_month = arabic_months.get(month, 'Invalid Month')
            # Convert year and month to Arabic numbers
            arabic_year = ''.join(arabic_numbers[digit] for digit in year)
            date_dict.append(arabic_month)
            date_dict.append(arabic_year)
        days = []
        product_dict = {}
        for product in products:
            days.append(product.taayeen_weekday)
        for col in column_names:
            quantities = []
            for product in products:
                quantities.append(convert_to_hindi_numbers(getattr(product,col)))
            col_name = col.replace('_',' ')
            product_dict[col_name] = quantities
            
        final_dict['days'] = days
        final_dict['product_dict']=product_dict
        for product in products:
            for col in column_names:
                products_data[col] += getattr(product, col, 0)

        for col in column_names:
            name = col.replace('_',' ')
            new_products_data[name] = convert_to_hindi_numbers(products_data[col])
        for key in final_dict['product_dict'].keys():
            value = new_products_data.get(key)
            if value is not None:
                final_dict['product_dict'][key].append(value)
        return render(request, 'POS/Mota3hd.html', {'final_dict': final_dict,"date_dict":date_dict })
    return render(request,'POS/motaahed.html')


def takarer_esthlak(request):
    if request.method == 'POST':
        takrer_type = request.POST.get('takrer-select')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        print(takrer_type,start_date,end_date)
        if takrer_type == 'تقرير استهلاك طازة':
            exclude_fields = ['TazaMonsaraf_id', 'azen_number', 'date','taayeen_weekday','taayeen_season']
            columns = [field.name for field in TazaMonsaraf._meta.get_fields() if field.name not in exclude_fields]
            products_data = {}
            new_products_data = {}
            products = TazaMonsaraf.objects.filter(date__range=[start_date, end_date])
            products_data = {name: 0 for name in columns}
            final_dict = {}
            date_dict=[]
            if '-' in start_date:
                # Splitting the year and month
                year, month, day= start_date.split('-')  # Using the * operator to catch extra values

                # Dictionary mapping English numbers to Arabic numbers
                arabic_numbers = {'0': '٠', '1': '١', '2': '٢', '3': '٣', '4': '٤', '5': '٥', '6': '٦', '7': '٧', '8': '٨', '9': '٩'}
                # List of Arabic month names
                arabic_months = {
                    '01': 'يناير',
                    '02': 'فبراير',
                    '03': 'مارس',
                    '04': 'أبريل',
                    '05': 'مايو',
                    '06': 'يونيو',
                    '07': 'يوليو',
                    '08': 'أغسطس',
                    '09': 'سبتمبر',
                    '10': 'أكتوبر',
                    '11': 'نوفمبر',
                    '12': 'ديسمبر'
                }

                # Get the Arabic month name
                arabic_month = arabic_months.get(month, 'Invalid Month')
                # Convert year and month to Arabic numbers
                arabic_year = ''.join(arabic_numbers[digit] for digit in year)
                date_dict.append(arabic_month)
                date_dict.append(arabic_year)
            days = []
            product_dict = {}
            for product in products:
                days.append(product.taayeen_weekday)
            for col in columns:
                quantities = []
                for product in products:
                    
                    quantities.append(convert_to_hindi_numbers(getattr(product,col)))
                    col_name = col.replace('_',' ')
                    if col == 'recruit_count':
                        col_name = 'عدد المجندين'
                    if col == 'officer_count':
                        col_name = 'عدد الضباط'
                    if col == 'worker_count':
                        col_name = 'عدد الأفراد'
                    product_dict[col_name] = quantities
            
                   
            
            final_dict['days'] = days
            final_dict['product_dict']=product_dict
            for product in products:
                for col in columns:
                    products_data[col] += getattr(product, col, 0)

            for col in columns:
                name = col.replace('_',' ')
                if col == 'recruit_count':
                    name = 'عدد المجندين'
                if col == 'officer_count':
                    name = 'عدد الضباط'
                if col == 'worker_count':
                    name = 'عدد الأفراد'
                new_products_data[name]= convert_to_hindi_numbers(products_data[col])
            for key in final_dict['product_dict'].keys():
                value = new_products_data.get(key)
                if value is not None:
                    final_dict['product_dict'][key].append(value)
            return render(request, 'POS/takarer_esthlak.html', {'final_dict': final_dict,"date_dict":date_dict})
        
        if takrer_type == 'تقرير استهلاك جاف':
            exclude_fields = ['TaskMonsaraf_id', 'azen', 'date' , 'task_location' , 'duration','taskmortgaa','members']
            columns = [field.name for field in TaskMonsaraf._meta.get_fields() if field.name not in exclude_fields]
            products = TaskMonsaraf.objects.filter(date__range=[start_date, end_date])
            new_products_data = {}

            products_data = {name: 0 for name in columns}
            final_dict = {}
            date_dict=[]
            if '-' in start_date:
                # Splitting the year and month
                year, month, day= start_date.split('-')  # Using the * operator to catch extra values

                # Dictionary mapping English numbers to Arabic numbers
                arabic_numbers = {'0': '٠', '1': '١', '2': '٢', '3': '٣', '4': '٤', '5': '٥', '6': '٦', '7': '٧', '8': '٨', '9': '٩'}
                # List of Arabic month names
                arabic_months = {
                    '01': 'يناير',
                    '02': 'فبراير',
                    '03': 'مارس',
                    '04': 'أبريل',
                    '05': 'مايو',
                    '06': 'يونيو',
                    '07': 'يوليو',
                    '08': 'أغسطس',
                    '09': 'سبتمبر',
                    '10': 'أكتوبر',
                    '11': 'نوفمبر',
                    '12': 'ديسمبر'
                }

                # Get the Arabic month name
                arabic_month = arabic_months.get(month, 'Invalid Month')
                # Convert year and month to Arabic numbers
                arabic_year = ''.join(arabic_numbers[digit] for digit in year)
                date_dict.append(arabic_month)
                date_dict.append(arabic_year)
            days = []
            product_dict = {}
            for product in products:
                days.append(product.taayeen_weekday)
            for col in columns:
                quantities = []
                for product in products:
                    quantities.append(convert_to_hindi_numbers(getattr(product,col)))
                    col_name = col.replace('_',' ')
                    if col == 'recruit_count':
                        col_name = 'عدد المجندين'
                    if col == 'officer_count':
                        col_name = 'عدد الضباط'
                    if col == 'worker_count':
                        col_name = 'عدد الأفراد'
                    product_dict[col_name] = quantities
            
                   
            
            final_dict['days'] = days
            final_dict['product_dict']=product_dict
            for product in products:
                for col in columns:
                    products_data[col] += getattr(product, col, 0)

            for col in columns:
                name = col.replace('_',' ')
                if col == 'recruit_count':
                    name = 'عدد المجندين'
                if col == 'officer_count':
                    name = 'عدد الضباط'
                if col == 'worker_count':
                    name = 'عدد الأفراد'
                new_products_data[name] = convert_to_hindi_numbers(products_data[col])
            for key in final_dict['product_dict'].keys():
                value = new_products_data.get(key)
                if value is not None:
                    final_dict['product_dict'][key].append(value)
            return render(request, 'POS/takarer_esthlak.html', {'final_dict': final_dict,"date_dict":date_dict})
        
        if takrer_type == 'تقرير استهلاك ترفيه':
            products = TarfehMonsaraf.objects.filter(date__range=[start_date, end_date])
            column_sums = {}
            product_data ={}
            for product in products:
                product_name = getattr(product, 'product_name',None)
                column_sums[product_name] = 0


            for product in products:
                product_name = getattr(product, 'product_name',None)
                quantity = getattr(product, 'quantity', 0)
                column_sums[product_name] += quantity

            for name in column_sums.keys():
                product_data[name] = convert_to_hindi_numbers(column_sums[name])
            return render(request, 'POS\Results.html', {'products_data': product_data})




        
    return render(request, 'POS/takarer.html')








