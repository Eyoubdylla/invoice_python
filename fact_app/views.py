from django.shortcuts import render
from django.views import View
from .models import *
from django.contrib import messages


# Create your views here.
class HomeView(View):
    template_name = 'index.html'
    invoices = Invoice.objects.select_related('customer','save_by').all()
    
    context = {
        'invoices' : invoices
    }
    def get(self, request, *args, **kwagrs):
        return render(request, self.template_name, self.context)
    
    def post(self, request, *args, **kwagrs):
        return render(request, self.template_name, self.context)
  
class AddCustomerView(View):
    template_name = 'add_customer.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        print(request.POST)
        data = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('plone'),
            'address': request.POST.get('address'),
            'sex': request.POST.get('sex'),
            'age': request.POST.get('age'),
            'city' : request.POST.get('city'),
            'zip_code': request.POST.get('Zip'),
            'save_by' : request.user
            }
        try:
            created = Customer.objects.create(**data)
            if created:
                messages.success(request, "customer register successfuly")
            else :
                messages.error(request, " sorry, pleese tru again the sent data is corrupt.")
        except Exception as e:
            messages.error(request, f"sorry our system is decting the following issus{e}")
        return render(request, self.template_name)
        