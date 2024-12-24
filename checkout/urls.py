from django.contrib import admin
from django.urls import path,include

app_name = 'checkout'

urlpatterns = [

   path('checkout/', include('checkout.urls', namespace='checkout')),


]
