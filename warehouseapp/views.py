from django.shortcuts import render, redirect
from .models import Product, Transaction
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/admin/gnb/')
def homepage(request):
	products = Product.objects.all()
	return render(request, 'home.html', {'products':products})


@login_required(login_url='/admin/gnb/')
def add_quantity(request,pk):
	if request.method == 'POST':
		product = get_object_or_404(Product, pk=pk)
		quantity = request.POST.get('quantity')
		int_quantity = int(quantity)
		product.quantity += int_quantity
		product.save()
		updated_quantity = product.quantity

		new_transaction = Transaction.objects.create(
				#object_id = uuid.uuid4(),
				operation= 1, 
				product = product, 
				remarks = str(quantity) +' case has been added to the the stock by'

				
		)
		new_transaction.save()
		
		
		data = {
			'quantity':updated_quantity
		}
		
		return JsonResponse(data) 

@login_required(login_url='/admin/gnb/')
def delete_quantity(request, pk):
	if request.method == 'POST':
		product = get_object_or_404(Product,pk=pk)
		quantity = request.POST.get('quantity')
		print (quantity)
		int_quantity = int(quantity)
		product.quantity -=int_quantity
		product.save()
		updated_quantity = product.quantity

		new_transaction = Transaction.objects.create(
			operation = 2,
			product = product,
			remarks = str(quantity) +' case has been deleted from the stock'
			)
		
		data = {
			'quantity':updated_quantity
		}
		return JsonResponse(data)


@login_required(login_url='/admin/gnb/')
def add_product(request):
	if request.method == 'POST':
		name = request.POST.get('product_name')
		price = request.POST.get('price')
		add_product = Product.objects.create(name = name , price = price, quantity=0)
		return redirect('/')
	else:
		return render (request, '/')
