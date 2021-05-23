from django.shortcuts import render

from .models import Product

from .forms import ProductForm

# Create your views here.

# def product_create_view(request):
# 	context = {}
# 	# return render(request, 'products/detail.html',context)
# 	return render(request, 'products/product_create.html',context)


def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
	# context = { 
	# 	# 'object' : obj
	# 	'form' : form
	# }
	context = {
		'form' : ProductForm()
	}
	# return render(request, 'products/detail.html',context)
	return render(request, 'products/product_create.html',context)


def product_detail_view(request):
	obj = Product.objects.get(id=1)
	# context = {
	# 	'title' : obj.title,
	# 	'description' : obj.description,
	# 	'summary' : obj.summary
	# }
	context = { 'object' : obj}
	return render(request, 'products/detail.html',context)