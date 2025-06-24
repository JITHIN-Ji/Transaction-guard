from django.urls import path
from .import views

urlpatterns=[

    path('',views.index_page,name='index_page'),
    path('adm_usr_login',views.adm_usr_login,name='adm_usr_login'),
    path('thrreg',views.thrreg,name='thrreg'),
    path('admin_page',views.admin_page,name='admin_page'),
    path('user_page',views.user_page,name='user_page'),
    path('', views.index, name='index'),








]
