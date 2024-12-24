import os
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.models import User
from products.models import Product

# view function for fruit page
def fruit(request):
    """
    This method will get products where category is Fruit.
    After that it will return the url of fruit html page.

    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :return: returns fruit page

    """
    product = Product.objects.filter(category="Fruit")
    n = Product.objects.filter(category="Fruit").count()
    params = {'product': product, 'n': n}
    return render(request, 'products/fruit.html', params)

# view function for vegetable page
def vegetable(request):
    """
    This method will get products where category is Vegetable.
    After that it will return the url of vegetable html page.

    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :return: returns vegetable page

    """
    product = Product.objects.filter(category="Vegetable")
    n = Product.objects.filter(category="Vegetable").count()
    params = {'product': product, 'n': n}
    return render(request, 'products/vegetable.html', params)

# view function for fish page
def fish(request):
    """
    This method will get products where category is Fish.
    After that it will return the url of fish html page.

    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :return: returns fish page

    """
    product = Product.objects.filter(category="Fish")
    n = Product.objects.filter(category="Fish").count()
    params = {'product': product, 'n': n}
    return render(request, 'products/fish.html', params)

# view function for medicine page
def medicine(request):
    """
    This method will get products where category is Medicine.
    After that it will return the url of medicine html page.

    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :return: returns medicine page

    """
    product = Product.objects.filter(category="Medicine")
    n = Product.objects.filter(category="Medicine").count()
    params = {'product': product, 'n': n}
    return render(request, 'products/medicine.html', params)

# view function for meat page
def meat(request):
    """
    This method will get products where category is Meat.
    After that it will return the url of meat html page.

    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :return: returns meat page

    """
    product = Product.objects.filter(category="Meat")
    n = Product.objects.filter(category="Meat").count()
    params = {'product': product, 'n': n}
    return render(request,'products/meat.html',params)

# Add Product
def add_product(request):
    """
    This method will use to add new products in the shop. It will take
    the product name, category, price, photo, description and will store
    them in database. Only admin can access this function, if the user is
    not admin it will show an error message. Otherwise, it will store the
    data into the database and return the url of home page.

    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :return: returns home page
    """
    if request.user.is_superuser:

        if request.method == 'POST':
            product_name = request.POST['product_name']
            product_category = request.POST['product_category']
            product_price = request.POST['product_price']
            product_photo = request.FILES['product_photo']
            product_description = request.POST['product_description']

            add_product = Product(product_name = product_name, category = product_category, price = product_price,
                                  description = product_description, pub_date = datetime.today(), image = product_photo)
            add_product.save()

            messages.success(request, 'Product has been added successfully!!!')
            return render(request, 'home/home.html')

        else:
            return HttpResponse("404-Not Found")

    else:
        return render(request, 'html_view_with_error', {"error" : "PERMISSION DENIED"})

# For Updating Product
def update_product(request, product_id):
    """
    This method will use to update or edit products in the shop. It will find the
    specific product with product id which is the primary key of the product.
    Only admin can access this function, if the user is not admin it will show an
    error message. Otherwise, it will update the data into the database and return
    the url of home page.

    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :param name: product_id - used to find the specific product for update
    :param type: HttpResponse
    :return: returns home page

    """
    if request.user.is_superuser:

        if request.method == 'POST':
            product = Product.objects.get(pk=product_id)
            product.product_name = request.POST['product_name']
            product.category = request.POST['product_category']
            product.price = request.POST['product_price']

            if 'product_photo' in request.FILES:
                os.remove(product.image.path)
                product.image = request.FILES['product_photo']

            product.description = request.POST['product_description']
            product.pub_date = datetime.today()
            product.save()

            messages.success(request, 'Product has been updated successfully!!!')
            return redirect("/")

        else:
            return HttpResponse("404-Not Found")

    else:
        return render(request, 'html_view_with_error', {"error" : "PERMISSION DENIED"})

# For Deleting Product
def delete_product(request,product_id):
    """
    This method will use to delete products in the shop. It will find the
    specific product with product id which is the primary key of the product,
    and delete that specific product. Only admin can access this function,
    if the user is not admin it will show an error message. Otherwise, it
    will delete the data from the database and return the url of home page.

    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :param name: product_id - used to find the specific product for update
    :param type: HttpResponse
    :return: returns home page

    """
    if request.user.is_superuser:
        product = Product.objects.get(pk=product_id)
        os.remove(product.image.path)
        product.delete()
        messages.success(request, 'Product has been deleted successfully!!!')
        return redirect("/")

    else:
        return render(request, 'html_view_with_error', {"error" : "PERMISSION DENIED"})



