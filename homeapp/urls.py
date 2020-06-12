from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('',views.index , name='home'),
    path('calculate',views.calculate , name = 'calculate')
]