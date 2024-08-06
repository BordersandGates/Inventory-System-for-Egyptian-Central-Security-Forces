from django.contrib import admin
from .models import *
admin.site.register(ProductMetadata)
admin.site.register(Product)
admin.site.register(TazaMonsaraf)
admin.site.register(TazaTayyen)
admin.site.register(TaskMonsaraf)
admin.site.register(TaskMortgaa)
admin.site.register(TarfehMonsaraf)
admin.site.register(Member)

admin.site.index_title = 'الأمن المركزى'
admin.site.site_header = 'الأمن المركزى'
admin.site.site_title = 'الأمن المركزى'
