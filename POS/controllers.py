from .models import *
from django.db.models import F
from decimal import Decimal
from datetime import datetime , timedelta


excluded_fields = ['taayeen_id', 'taayeen_weekday', 'taayeen_season' , 'member']
column_names = [field.name for field in TazaTayyen._meta.get_fields() if field.name not in excluded_fields]
included_product_names = ['خبز','زبادي','خضار مجمد', 'سلاطه', 'فاكهه', 'ثوم', 'بصل ناشف', 'بهارات', 'بيض', 'لحوم مجمده' , 'دواجن مجمده']

def issue_taza_products(season, weekday, officer_count, recruits_count, workers_count, azen, date, issuance_type):
    Tayyen_1 = TazaTayyen.objects.get(taayeen_season=season, taayeen_weekday=weekday, member='ضباط')
    Tayyen_2 = TazaTayyen.objects.get(taayeen_season=season, taayeen_weekday=weekday, member='افراد و مجندين')
    New_Monsaraf = TazaMonsaraf.objects.create(taayeen_season=season, taayeen_weekday=weekday,officer_count=officer_count, azen_number=azen, recruit_count=recruits_count, worker_count=workers_count, date=date)
    ret = True
    if issuance_type == 'وجبة التعيين':
        for product in column_names:
            quantity = officer_count * getattr(Tayyen_1, product) + (recruits_count + workers_count) * getattr(Tayyen_2, product)
            product_name = product.replace('_', ' ')
            if product_name not in included_product_names:
                cond, rem = issue_product(product_name, quantity)
                ret = ret and cond
                setattr(New_Monsaraf, product, quantity - rem)
            else:
                setattr(New_Monsaraf, product, quantity)
    elif issuance_type == 'وجبة لحوم':
        # Define custom quantities for 'لحوم' issuance
        custom_quantities = {
    'لحوم_مجمده': Decimal('0.100'),
    'دواجن_مجمده': Decimal('0'),
    'خضار_مجمد': Decimal('0.090'),
    'فاصوليا_جافة': Decimal('0'),
    'مكرونة': Decimal('0'),
    'ارز_بلدى': Decimal('0.090'),
    'شعرية': Decimal('0.015'),
    'صلصة': Decimal('0.015'),
    'فلفل_اسود': Decimal('0.25')
        }
        for product in column_names:
            product_name = product.replace('_',' ')
            if product in custom_quantities.keys() and product_name in included_product_names:
                setattr(New_Monsaraf, product, (officer_count + recruits_count + workers_count)*custom_quantities[product])
            elif product in custom_quantities.keys():
                cond, rem = issue_product(product_name, (officer_count + recruits_count + workers_count)*custom_quantities[product])
                ret = ret and cond
                setattr(New_Monsaraf, product,  (officer_count + recruits_count + workers_count)*custom_quantities[product] - rem)
            else:
                quantity = officer_count * getattr(Tayyen_1, product) + (recruits_count + workers_count) * getattr(Tayyen_2, product)
                if product_name not in included_product_names:
                    cond, rem = issue_product(product_name, quantity)
                    ret = ret and cond
                    setattr(New_Monsaraf, product, quantity - rem)
                else:
                    setattr(New_Monsaraf, product, quantity)




    elif issuance_type == 'وجبة دواجن':
        # Define custom quantities for 'دواجن' issuance
        custom_quantities = {
    'لحوم_مجمده': Decimal('0'),
    'دواجن_مجمده': Decimal('0.225'),
    'خضار_مجمد': Decimal('0.090'),
    'فاصوليا_جافة': Decimal('0'),
    'مكرونة': Decimal('0'),
    'ارز_بلدى': Decimal('0.090'),
    'شعرية': Decimal('0.015'),
    'صلصة': Decimal('0.015'),
    'فلفل_اسود': Decimal('0.25')
}

        for product in column_names:
            product_name = product.replace('_',' ')
            if product in custom_quantities.keys() and product_name in included_product_names:
                setattr(New_Monsaraf, product, (officer_count + recruits_count + workers_count)*custom_quantities[product])
            elif product in custom_quantities.keys():
                cond, rem = issue_product(product_name, (officer_count + recruits_count + workers_count)*custom_quantities[product])
                ret = ret and cond
                setattr(New_Monsaraf, product, (officer_count + recruits_count + workers_count)*custom_quantities[product] - rem)
            else:
                quantity = officer_count * getattr(Tayyen_1, product) + (recruits_count + workers_count) * getattr(Tayyen_2, product)
                if product_name not in included_product_names:
                    cond, rem = issue_product(product_name, quantity)
                    ret = ret and cond
                    setattr(New_Monsaraf, product, quantity - rem)
                else:
                    setattr(New_Monsaraf, product, quantity)
    elif issuance_type == 'وجبة بدون':
        # Define custom quantities for 'بدون' issuance
        custom_quantities = {
    'لحوم_مجمده': Decimal('0'),
    'دواجن_مجمده': Decimal('0'),
    'خضار_مجمد': Decimal('0'),
    'فاصوليا_جافة': Decimal('0.040'),
    'مكرونة': Decimal('0.090'),
    'ارز_بلدى': Decimal('0'),
    'شعرية': Decimal('0'),
    'صلصة': Decimal('0.025'),
    'فلفل_اسود': Decimal('0.75')
}
        for product in column_names:
            product_name = product.replace('_',' ')
            if product in custom_quantities.keys() and product_name in included_product_names:
                setattr(New_Monsaraf, product, (officer_count + recruits_count + workers_count)*custom_quantities[product])
            elif product in custom_quantities.keys():
                cond, rem = issue_product(product_name, (officer_count + recruits_count + workers_count)*custom_quantities[product])
                ret = ret and cond
                setattr(New_Monsaraf, product, (officer_count + recruits_count + workers_count)*custom_quantities[product] - rem)
            else:
                quantity = officer_count * getattr(Tayyen_1, product) + (recruits_count + workers_count) * getattr(Tayyen_2, product)
                if product_name not in included_product_names:
                    cond, rem = issue_product(product_name, quantity)
                    ret = ret and cond
                    setattr(New_Monsaraf, product, quantity - rem)
                else:
                    setattr(New_Monsaraf, product, quantity)

    New_Monsaraf.save()
    return ret

def issue_product(product_name,quantity):
    remaining_quantity = quantity
    selected_products = []
    while remaining_quantity > 0:
        product = Product.objects.filter(name=product_name, quantity__gt=0).order_by('expiration_date').first()

        if product is None:
            print(f"No more {product_name} available in stock.")
            return False, remaining_quantity

        quantity_to_take = min(remaining_quantity, product.quantity)
        
        selected_products.append({
            'name': product.name,
            'expiration_date': product.expiration_date,
            'quantity': quantity_to_take
        })

        remaining_quantity -= quantity_to_take
        
        Product.objects.filter(pk=product.pk).update(quantity=F('quantity') - quantity_to_take)
        if product.quantity - quantity_to_take <= 0:
            product.delete()

    return True , 0 

def issue_gaf_products(worker_count,recruit_count,officer_count,azen,date,location , duration , members):
    new_gaf_product = TaskMonsaraf.objects.create(officer_count=officer_count, azen=azen, recruit_count=recruit_count, worker_count=worker_count , task_location = location , date =date , duration = duration)
    if  len(members) > 0:
        json_data = json.dumps(members, ensure_ascii=False)
        decoded_data = json.loads(json_data)  # Decode the JSON string into Python object

        for member_data in decoded_data:  # Iterate over the list of dictionaries
            new_member = Member.objects.get(name=member_data['name'])
            new_gaf_product.members.add(new_member)

    count = (worker_count + recruit_count + officer_count) * duration
    ret = True
    cond, rem = issue_product(product_name="تونه جاف", quantity=count)
    ret = ret and cond
    setattr(new_gaf_product, "تونه_جاف",count - rem)

    cond, rem = issue_product("جبنة بيضاء 80جم", count)
    ret = ret and cond
    setattr(new_gaf_product, "جبنة_بيضاء_80جم",count - rem)

    cond, rem = issue_product("حلاوة قطع", count)
    ret = ret and cond
    setattr(new_gaf_product, "حلاوة_قطع",count - rem)

    cond, rem = issue_product("عصير جاف", count*2)
    ret = ret and cond
    setattr(new_gaf_product, "عصير_جاف",count*2 - rem)

    cond, rem = issue_product("فول معلب 360 جرام العلبة", count*Decimal(0.5))
    ret = ret and cond
    setattr(new_gaf_product, "فول_معلب_360_جرام_العلبة",count*Decimal(0.5) - rem)

    cond, rem = issue_product("مربى قطع", count)
    ret = ret and cond
    setattr(new_gaf_product, "مربى_قطع",count - rem)

    quan = count 
    if location == 'جاف سيناء' :
        quan *= 2 
    cond, rem = issue_product("مياه معدنية جاف", quan)
    ret = ret and cond
    setattr(new_gaf_product, "مياه_معدنية_جاف",quan - rem)
    new_gaf_product.save()

    return ret


def issue_tarfeh_products( officer_count ,recruit_count , worker_count , azen , quantity , date , product_name):
    new_tarfeh_monsaraf = TarfehMonsaraf.objects.create(recruit_count = recruit_count , worker_count=worker_count,officer_count = officer_count, azen = azen , quantity= 0,date=date , product_name = product_name)
    ret = True
    cond, rem = issue_product(product_name, quantity*(officer_count+recruit_count+worker_count))
    ret = ret and cond
    setattr(new_tarfeh_monsaraf, 'quantity', quantity*(officer_count+recruit_count+worker_count) - rem)
    new_tarfeh_monsaraf.save()
    return ret

def mortgaaControll(date , azen):
    excluded_fields = ["taskmortgaa","TaskMonsaraf_id","azen","task_location","duration","officer_count","recruit_count","worker_count","date","members"]
    column_names = [field.name for field in TaskMonsaraf._meta.get_fields() if field.name not in excluded_fields]
    print(column_names)
    Mamorya = TaskMonsaraf.objects.get(azen = azen)
    end_date = getattr(Mamorya,'date') + timedelta(days=getattr(Mamorya,'duration'))
    added = False
    if end_date <= getattr(Mamorya,'date'): 
        for product_name in column_names:
            search_str = product_name.replace('_',' ')
            product = Product.objects.filter(name=search_str, quantity__gt=0).order_by('expiration_date').first()
            if product is not None:
                Product.objects.filter(pk=product.pk).update(quantity=F('quantity')+getattr(Mamorya,product_name))
                added = True
    if added == False:
        officer_count = getattr(Mamorya,'officer_count')
        recruit_count = getattr(Mamorya,'recruit_count')
        worker_count = getattr(Mamorya,'worker_count')
        duration = getattr(Mamorya,'duration')
        date_object = datetime.strptime(date, "%Y-%m-%d").date()

        real_duration = (end_date - date_object).days + 1 
        newMortgaa = TaskMortgaa.objects.create(TaskMonsaraf_id = Mamorya, date = date)
        for product_name in column_names:
            use_daily = getattr(Mamorya,product_name)/((officer_count + recruit_count + worker_count)*duration)
            search_str = product_name.replace('_',' ')
            product = Product.objects.filter(name=search_str, quantity__gt=0).order_by('expiration_date').first()

            if product is not None:
                Product.objects.filter(pk=product.pk).update(quantity=F('quantity')+ use_daily*real_duration)
                added = True

                setattr(Mamorya,product_name,getattr(Mamorya,product_name)-use_daily*real_duration)
            setattr(newMortgaa,product_name,use_daily*real_duration)

        newMortgaa.save()
        Mamorya.save()





def convert_to_hindi_numbers(number):
    hindi_numerals = ['٠', '١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩']
    
    # Convert the integer part
    integer_part, _, fractional_part = str(number).partition('.')
    integer_hindi = ''.join(hindi_numerals[int(digit)] if digit.isdigit() else digit for digit in integer_part)
    
    # Convert the fractional part if it exists
    if len(fractional_part)>0:
        fractional_hindi = ''.join(hindi_numerals[int(digit)] if digit.isdigit() else digit for digit in fractional_part) if fractional_part else ''
        return f"{integer_hindi}.{fractional_hindi}"
    else:
        return integer_hindi

def convert_to_arabic_date(gregorian_date):
    day = convert_to_hindi_numbers(gregorian_date.day)
    month = convert_to_hindi_numbers(gregorian_date.month)
    year = convert_to_hindi_numbers(gregorian_date.year)
    return f"{day}/{month}/{year}"

def takrer_gaf(azen_number):
        exclude_fields = ['TaskMonsaraf_id', 'azen', 'officer_count', 'recruit_count', 'worker_count', 'date' , 'task_location' , 'duration','taskmortgaa','members']
        columns = [field.name for field in TaskMonsaraf._meta.get_fields() if field.name not in exclude_fields]
        product = TaskMonsaraf.objects.get(azen = azen_number)
        products_data = {}
        for col in columns:
            name = col.replace('_' , ' ')
            products_data[name] = convert_to_hindi_numbers(getattr(product, col, 0))

        members = product.members.all()
        members_data = []
        for member in members:
            member_info = {
            'name': member.name,
            'type': member.type
            # Add more fields if needed
            }
            members_data.append(member_info)

        return products_data , members

def takrer_taza(azen_number):
    exclude_fields = ['TazaMonsaraf_id', 'azen_number', 'officer_count', 'recruit_count', 'worker_count', 'date','taayeen_season','taayeen_weekday']
    columns = [field.name for field in TazaMonsaraf._meta.get_fields() if field.name not in exclude_fields]
    product = TazaMonsaraf.objects.get(azen_number = azen_number)
    Tayeen_1 = TazaTayyen.objects.get(taayeen_weekday = product.taayeen_weekday , taayeen_season =product.taayeen_season ,member = 'ضباط')
    Tayeen_2 = TazaTayyen.objects.get(taayeen_weekday = product.taayeen_weekday , taayeen_season =product.taayeen_season ,member = 'افراد و مجندين')
    products_data = {}
    for col in columns:
        name = col.replace('_' , ' ')
        products_data[name] = [convert_to_hindi_numbers(getattr(product, col, 0)),convert_to_hindi_numbers(getattr(Tayeen_1, col, 0)),convert_to_hindi_numbers(getattr(Tayeen_2, col, 0))]
    meta_data={"اليوم":product.taayeen_weekday, 'تاريخ الصرف':convert_to_arabic_date(product.date),'رقم الأذن':convert_to_hindi_numbers(product.azen_number), 'عدد الضباط':convert_to_hindi_numbers(product.officer_count), 'عدد الأفراد':convert_to_hindi_numbers(product.recruit_count), 'عدد المجندين' : convert_to_hindi_numbers(product.worker_count)}    
    return products_data,meta_data


def takrer_tarfeh(azen_number):
    products = TarfehMonsaraf.objects.filter(azen=azen_number)
    products_data = {}
    for product in products:
        product_name = getattr(product, 'product_name', None)
        quantity = getattr(product, 'quantity', 0)
        
        products_data[product_name]=convert_to_hindi_numbers(quantity)
    return products_data

