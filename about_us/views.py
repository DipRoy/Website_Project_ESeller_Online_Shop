from django.shortcuts import render
from about_us.models import AboutUs

 
def create_about_us(request):
    """
    This method will display the About us page where admin can add more information and also change information. These will save in database.
    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :return: returns about us page
    """
    
    if request.method == "POST":
        about_us = request.POST.get("about_us")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        is_open = request.POST.get("is_open")


    about_us = AboutUs(about_us = about_us, email = email, phone = phone, is_open = is_open)
    about_us.save()
    return render(request, 'about_us/about_us.html')
     
 
def about_us(request):
    """
    This method will display the About us page and in About us page there
    will be a description of this website and admins which are given by the admin in the database. 
    :param name: request - used to generate responses(Http) depending on the request that it receives
    :param type: HttpResponse
    :return: returns about us page
    """
    
    about_us = AboutUs.objects.all()
    params = {'about_us':about_us}
    return render(request, 'about_us/about_us.html', params)