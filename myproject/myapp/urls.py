from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('services/',views.services,name='services'),
    path('form/',views.form,name='form'),
    path('table/',views.table,name='table'),
    path('testing/',views.testing,name='testing'),
    path('webpage/', views.webpage, name='webpage'),
    path('taskweb/', views.taskweb, name='taskweb'),
    path('food1/',views.food1,name='food1'),
    path('food2/',views.food2,name='food2'),
    path('food3/',views.food3,name='food3'),
    path('stdform/', views.stdform, name='stdform'),
    path('result/', views.result, name='result'),
    path('website/', views.website, name='website'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
  
  

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 