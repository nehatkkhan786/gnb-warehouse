from django.shortcuts import render, redirect
from .models import Product, Transaction
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
def homepage(request):
	products = Product.objects.all()
	return render(request, 'home.html', {'products':products})



def add_quantity(request,pk):
	if request.method == 'POST':
		product = get_object_or_404(Product, pk=pk)
		quantity = request.POST.get('quantity')
		int_quantity = int(quantity)
		product.quantity += int_quantity
		product.save()

		new_transaction = Transaction.objects.create(
				#object_id = uuid.uuid4(),
				operation= 1, 
				product = product
		)
		new_transaction.save()
		updated_quantity = product.quantity
		
		data = {
			'quantity':updated_quantity
		}
		
		return JsonResponse(data) 

def delete_quantity(request, pk):
	if request.method == 'POST':
		product = get_object_or_404(Product,pk=pk)
		quantity = request.POST.get('quantity')
		int_quantity = int(quantity)
		product.quantity -=int_quantity
		product.save()

		new_transaction = Transaction.objects.create(
			operation = 2,
			product = product
			)
		updated_quantity = product.quantity
		data = {
			'quantity':updated_quantity
		}
		return JsonResponse(data)
