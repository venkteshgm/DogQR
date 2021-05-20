from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home_view(request,*args, **kwargs):
	# print(request.user,args, kwargs)
	# return HttpResponse("<h1>Hello Doggos!<h1>")
	return render(request,'home.html',{})

def contact(request,*args, **kwargs):
	return render(request, 'contact.html', {})

def about(request,*args, **kwargs):
	my_context = {
		'contact_name' : 'Venkteshprasad Maya Rao',
		'instagram' : '@venktesh_m_rao',
		'linkedIn' : "please don't bother",
		'github' : 'venkteshgm',
		'contact_numbers' : ['+91-8310431987','+91-8904552389','+91-9481484210','+91-8026729059']
	}
	return render(request, 'about.html', my_context)