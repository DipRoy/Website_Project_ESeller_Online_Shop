from django.shortcuts import render
from django.views.generic import View, TemplateView, DetailView
from django.shortcuts import render, redirect
from .models import *


# Create your views here.

class UserProfileView(TemplateView):
    
    """
    This class provides the fields and actions that are required for the data you're storing from the user.
    Each model maps to a single database table. This class is used to create a database
    table containing those attributes.
    
    """

    template_name = "user_profile.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Customer.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect("/login/?next=/profile/")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.request.user.customer
        context['customer'] = customer
        orders = Purchased.objects.filter(cart__customer=customer).order_by("-id")
        context["orders"] = orders
        return context


class UserDashboardView(DetailView):

    """
    This class contains the fields and actions that you'll need to store the data from the user's dashboard.
    Each model maps to a single database table. This class is used to create a database
    table containing those attributes.
    
    """
    template_name = "user_dashboard.html"
    model = Purchased
    context_object_name = "ord_obj"

    def dispatch(self, request, *args, **kwargs):

        """
        This method receives a request from the user and returns the database response.
        :param name: request - used to generate responses(Http) depending on the request that it receives
        :param type: HttpResponse
        :param name: product_id - used to find the specific product for update
        :param type: HttpResponse
    
        """
        if request.user.is_authenticated and Customer.objects.filter(user=request.user).exists():
            order_id = self.kwargs["ak"]
            order = Purchased.objects.get(id=order_id)
            if request.user.customer != order.cart.customer:
                return redirect("eseller:userdashboard")
        else:
            return redirect("/login/?next=/profile/")

        return super().dispatch(request, *args, **kwargs)
