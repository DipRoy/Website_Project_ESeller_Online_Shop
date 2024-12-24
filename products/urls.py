from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [

    path("fruit", views.fruit, name='fruit'),
    path("vegetable", views.vegetable, name='vegetable'),
    path("medicine", views.medicine, name='medicine'),
    path("meat", views.meat, name='meat'),
    path("fish", views.fish, name='fish'),
    path("add_product", views.add_product, name='add_product'),
    path("update_product/<int:product_id>", views.update_product, name='update_product'),
    path("delete_product/<int:product_id>", views.delete_product, name='delete_product')

]

