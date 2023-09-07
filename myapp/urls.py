from django.urls import path
from . import views


urlpatterns = [

    path('',views.index, name='home'),
    path('about/',views.about,name='about'),
    path('appointment',views.appointment,name='appointment'),
    path('doctors',views.doctors,name='doctors'),
    path('contact',views.contact,name='contact'),
    path('department', views.department, name='department'),

]

