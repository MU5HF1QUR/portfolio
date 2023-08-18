from django.urls import path
from . import views

urlpatterns = [
    path('',views.ind, name='index'),
    path('cUS/',views.contactUs, name='contact'),
    path('img/',views.img, name='image'),


]