
from django.contrib import admin
from django.urls import path,include

app_name = 'checkout'

urlpatterns = [
    
             path('user_dashboard/', include('user_dashboard.urls', namespace='user_dashboard')),


]
