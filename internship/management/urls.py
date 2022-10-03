from django.urls import path
from . import views

urlpatterns = [
   path('',views.login,name='login'),
   path('home',views.home,name='hi'),
   path('home/<str:id>',views.details,name='detail'),
   path('midterm/<str:id>',views.midterm,name='mid'),
   path('endterm/<str:id>',views.endterm,name='end'),
]
