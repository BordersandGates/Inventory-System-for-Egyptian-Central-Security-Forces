from django.db import models
import django.utils.timezone as timezone
import json


class ProductMetadata(models.Model):
    name = models.CharField(primary_key = True ,max_length=100 ,verbose_name = 'اسم المنتج' )
    type = models.CharField(max_length=15, verbose_name ='نوع المنتج' , default = 'طازة')
    class Meta:
        verbose_name = 'اسم المنتج'
        verbose_name_plural = 'اسماء المنتجات'
    def __str__(self):
        return str(self.name)    


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.ForeignKey(ProductMetadata , on_delete = models.CASCADE , verbose_name = 'اسم المنتج')
    azen = models.IntegerField(verbose_name = 'رقم الاذن' , default = 0)
    expiration_date = models.DateField(verbose_name ='تاريخ انتهاء الصلاحية')
    quantity = models.DecimalField(max_digits=20, decimal_places=3, default=0, verbose_name = 'الكمية')  # e.g., "2 Kg of rice", "8 eggs"
    class Meta:
        verbose_name =  'المنتج'
        verbose_name_plural =  'المنتجات'
    def __str__(self):
        return str(self.name)    


class TazaTayyen(models.Model):
    taayeen_id = models.AutoField(primary_key=True)
    taayeen_weekday = models.CharField(max_length=50 , verbose_name = 'اليوم')
    taayeen_season = models.CharField(max_length=50 , verbose_name = 'الموسم')
    member = models.CharField(max_length=50 , verbose_name = 'نوع التعيين')
    ارز_بلدى = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    بصل_ناشف = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    بهارات = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    بيض = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    ثوم = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    جبنة_بيضاء_80جم = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    حلاوة_قطع = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    خبز = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    خضار_مجمد = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    دواجن_مجمده = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    زبادى = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    زيت_طعام = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    سكر_باكيت = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    سلاطه = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    شاى_فتلة = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    شعرية = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    صلصة = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    عدس = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    فاصوليا_جافة = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    فاكهه = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    فلفل_اسود = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    فول_صحيح = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    فول_معلب_360_جرام_العلبة = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    كمون_حصى = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    لحوم_مجمده = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    مربى_قطع = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    مكرونة = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    ملح_طعام = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    عصير_جاف = models.IntegerField(default=0)
    class Meta:
        verbose_name =  'مقررات التعينات'
        verbose_name_plural =   'مقررات التعينات'
    def __str__(self) -> str:
            return f"{str(self.taayeen_weekday)} - {str(self.taayeen_season)}"      


class TazaMonsaraf(models.Model):
    TazaMonsaraf_id = models.AutoField(primary_key=True)
    azen_number = models.IntegerField(verbose_name = 'رقم الاذن' , default = 0 , unique = True)
    taayeen_weekday = models.CharField(max_length=50 , verbose_name = 'اليوم')
    taayeen_season = models.CharField(max_length=50 , verbose_name = 'الموسم')
    ارز_بلدى = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    بصل_ناشف = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    بهارات = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    بيض = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    ثوم = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    جبنة_بيضاء_80جم = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    حلاوة_قطع = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    خبز = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    خضار_مجمد = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    دواجن_مجمده = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    زبادى = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    زيت_طعام = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    سكر_باكيت = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    سلاطه = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    شاى_فتلة = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    شعرية = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    صلصة = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    عدس = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    فاصوليا_جافة = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    فاكهه = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    فلفل_اسود = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    فول_صحيح = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    فول_معلب_360_جرام_العلبة = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    كمون_حصى = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    لحوم_مجمده = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    مربى_قطع = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    مكرونة = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    ملح_طعام = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    عصير_جاف = models.IntegerField(default=0)
    officer_count = models.IntegerField(verbose_name='عدد الضباط' , default = 0)
    recruit_count = models.IntegerField(verbose_name = 'عدد المجندين' , default = 0)
    worker_count = models.IntegerField(verbose_name = 'عدد الافراد' , default = 0)
    date = models.DateField(verbose_name = 'تاريخ الصرف')
    class Meta:
        verbose_name =  'منصرف الطازة'
        verbose_name_plural =  'منصرفات الطازة'
    def __str__(self):
        return str(self.azen_number)


class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    class Meta:
        verbose_name =  'العضو'
        verbose_name_plural =  'الاعضاء'
    def __str__(self) -> str:
        return f"{str(self.type)} - {str(self.name)}"    




class TaskMonsaraf(models.Model):
    TaskMonsaraf_id = models.AutoField(primary_key=True)
    azen = models.IntegerField(default= 0 , verbose_name = 'رقم الاذن' , unique = True) 
    task_location = models.CharField(max_length=10 , default = 'جاف' , verbose_name = 'مكان المأمورية')
    duration = models.IntegerField(default = 0 , verbose_name = 'عدد ايام المأمورية')  
    officer_count = models.IntegerField(default = 0 , verbose_name = 'عدد الضباط')
    recruit_count = models.IntegerField(default = 0 , verbose_name = 'عدد المجندين')
    worker_count = models.IntegerField(default = 0 , verbose_name = 'عدد الافراد')
    date = models.DateField(verbose_name = 'تاريخ الصرف')
    مياه_معدنية_جاف = models.IntegerField(default = 0)
    عصير_جاف = models.IntegerField(default=0)
    تونه_جاف=models.IntegerField(default = 0)
    حلاوة_قطع = models.IntegerField(default = 0)
    مربى_قطع = models.IntegerField(default = 0)
    جبنة_بيضاء_80جم= models.IntegerField(default = 0)
    فول_معلب_360_جرام_العلبة = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    members = models.ManyToManyField(Member, verbose_name='أعضاء المأمورية')
    class Meta:
        verbose_name =  'منصرف الجاف'
        verbose_name_plural =  'منصرفات الجاف'
    def __str__(self):
        return str(self.azen)    



class TaskMortgaa(models.Model):
    Mortgaa_id = models.AutoField(primary_key=True)
    TaskMonsaraf_id = models.ForeignKey(TaskMonsaraf,on_delete=models.CASCADE)
    date = models.DateField()
    مياه_معدنية_جاف = models.IntegerField(default = 0)
    عصير_جاف = models.IntegerField(default=0)
    تونه_جاف=models.IntegerField(default = 0)
    حلاوة_قطع = models.IntegerField(default = 0)
    مربى_قطع = models.IntegerField(default = 0)
    جبنة_بيضاء_80جم= models.IntegerField(default = 0)
    فول_معلب_360_جرام_العلبة = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    class Meta:
        verbose_name =  'مرتجع الجاف'
        verbose_name_plural =  'مرتجعات الجاف'
    def __str__(self):
        return str(self.TaskMonsaraf_id)      




class TarfehMonsaraf(models.Model):
    TarfehMonsaraf_id = models.AutoField(primary_key=True )
    officer_count = models.IntegerField(verbose_name='عدد الضباط' , default = 0)
    recruit_count = models.IntegerField(verbose_name = 'عدد المجندين' , default = 0)
    worker_count = models.IntegerField(verbose_name = 'عدد الافراد' , default = 0)
    azen = models.IntegerField(default= 0 , verbose_name = 'رقم الاذن')
    quantity = models.DecimalField(max_digits=20, decimal_places=3, default = 0 ,verbose_name = 'المقرر')
    date = models.DateField(verbose_name = 'تاريخ الصرف')
    product_name = models.CharField(max_length=100 ,verbose_name = 'اسم المنتج' )
    class Meta:
        verbose_name =  'منصرف الترفيه'
        verbose_name_plural =  'منصرفات الترفيه'
    def __str__(self):
        return str(self.azen)        




    
