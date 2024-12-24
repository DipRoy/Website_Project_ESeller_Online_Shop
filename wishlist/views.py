from django.shortcuts import render
from wishlist.models import Wishlist
from django.contrib import messages
# Create your views here.



def wishlist(request):
    """
    This method will display the wishlist page and in wishlist page there
    will be a form to request for your wishes products to the admin. It will take data from the
    customer and will store those data in the database
    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :return: returns wishlist page
    """
    
    category = request.POST.get('category')
    name = request.POST.get('name')
    file = request.POST.get('file')
    description = request.POST.get('description')
    
    """
    This method will display a from where product category, product name, product image file and discription 
    will be asked to a customer in wishlist page. Customers can be given the information of their wishes.  
    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :return: returns wishlist page
    
    """
    
    wishlist = Wishlist(category = category, name = name, file = file, description = description)
    wishlist.save()
    
    messages.success(request, 'Your wish has been sent.')
    """
    This method will display a confirmation message after submitting the wishes of the customer. 
    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :return: returns wishlist page
    """
    
    return render(request, 'wishlist/wishlist.html')


def admin_wishlist(request):
    """
    This method will display the list of messages that customers has sent to
    admins. To view this list a user must have to login with admin account.
    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :return: returns customer wishes view page
    """
    
    wishlist = Wishlist.objects.all()
    params = {'wishlist': wishlist}
    return render(request, 'wishlist/admin_wishlist.html', params)
 
    
 