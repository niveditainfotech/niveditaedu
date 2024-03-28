from django.urls import path
from .import views


urlpatterns=[
    path('',views.home,name='home'),
    path('english/',views.english,name='english'),
    path('compotetive/',views.compotetive,name='compo'),
    path('entrence/',views.entrence,name='entrences'),
    path('adoutus/',views.about,name='abouts'),
    path('contact/',views.conatct,name='contacts'),
    path('form/',views.contactform,name='forms'),
]