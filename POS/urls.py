from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product-add', views.add, name='add_product'),
    path('all', views.add_all, name='all'),
    path('success_page', views.success_page_view, name='success_page'),  # Define the URL pattern for the success page
    path('sarf', views.sarf, name='sarf'),
    path('tarfeh', views.tarfeh, name='tarfeh'),
    path('gafa', views.gafa, name='gafa'),
    path('taza' ,views.taza , name ='taza' ),
    path('monsaraf-youm' ,views.taza_sarf , name ='monsaraf-youm'),
    path('monsaraf-task' ,views.gaf_sarf , name ='monsaraf-task'),
    path('monsaraf-tarfeh' ,views.tarfeh_sarf , name ='monsaraf-tarfeh'),
    path('mortgaa',views.mortgaa,name='mortgaa'),
    path('mortgaa-add',views.mortgaa_handle , name='mortgaa-add'),
    path('raseed-youmy' , views.product_list , name='raseed-youmy'),
    path('motaahed' , views.Motaahed , name = 'motaahed'),
    path('takarer',views.takarer, name = 'takarer'),
    path('taza-report/<str:azen_number>/', views.taza_report, name='taza_report'),
    path('gaf-report/<str:azen_number>/', views.gaf_report, name='gaf_report'),
    path('tarfeh-report/<str:azen_number>/', views.tarfeh_report, name='tarfeh_report'),
    path('takarer_esthlak',views.takarer_esthlak,name='takarer_esthlak')

]
   
   
# path('taza/add/', views.taza_add, name='taza_add'),
    # path('taza/edit/', views.taza_list, name='taza_edit'),
    # path('taza/delete/', views.taza_add, name='taza_delete'),
    # #Gafa
    # path('gafa/', views.taza_list, name='gafa_list'),
    # path('gafa/add/', views.taza_add, name='gafa_add'),
    # path('gafa/edit', views.taza_list, name='gafa_edit'),
    # path('gafa/delete/', views.taza_add, name='gafa_delete'),
    # #Tarfeh
    # path('rarfeh/', views.taza_list, name='tarfeh_list'),
    # path('tarfeh/add/', views.taza_add, name='tarfeh_add'),
    # path('tarfeh/edit', views.taza_list, name='tarfeh_edit'),
    # path('tarfeh/delete/', views.taza_add, name='tarfeh_delete'),
    # #Monsarf
    # path('monsarf/', views.taza_list, name='monsarf_list'),
    # path('monsarf/add/', views.taza_add, name='monsarf_add'),
    # path('monsarf/edit', views.monsarf_list, name='monsarf_edit'),
    # path('monsarf/delete/', views.monsarf_add, name='monsarf_delete'),

