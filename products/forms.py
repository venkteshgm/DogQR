from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price'
			]

class RawProductForm(forms.Form):
	title       = forms.CharField()
	description = forms.CharField(required=False,
		widget=forms.Textarea(attrs={
					'rows':20,
					'cols':50
			}))
	price       = forms.DecimalField()