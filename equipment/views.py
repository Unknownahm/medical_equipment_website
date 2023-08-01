# views.py

from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, HttpResponse
from .models import MedicalEquipment

def equipment_list(request):
    equipment = MedicalEquipment.objects.all()
    return render(request, 'equipment_list.html', {'equipment': equipment})

def add_to_cart(request, pk):
    equipment = get_object_or_404(MedicalEquipment, pk=pk)
    # Add the logic here to handle adding the item to the cart
    # For example, you can use sessions to store the cart data
    # and display a success message or redirect to the cart page.
    return render(request, 'add_to_cart.html', {'equipment': equipment})

def remove_from_cart(request, pk):
    equipment = get_object_or_404(MedicalEquipment, pk=pk)
    # Add the logic here to handle removing the item from the cart
    # For example, you can use sessions to modify the cart data
    # and display a success message or redirect to the cart page.
    return render(request, 'remove_from_cart.html', {'equipment': equipment})

def home(request):
    return HttpResponse("This is the Home page")

def about(request):
    return HttpResponse("This is the About page")

def contact(request):
    return HttpResponse("This is the Contact page")