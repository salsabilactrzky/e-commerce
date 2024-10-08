from django.forms import ModelForm
from .models import Product
from django import forms
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "category",
                   "brand", "condition", "stock", "image"]

    price = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'Integer only'}),
        label="Price"
    )

    def price_pos(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError('Harga harus lebih besar dari nol.')
        return price

    def stock_pos(self):
        stock = self.cleaned_data.get('stock')
        if stock <= 0:
            raise forms.ValidationError('Stok harus lebih besar dari nol.')
        return stock
    
    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)

    def clean_brand(self):
        brand = self.cleaned_data.get("brand")
        return strip_tags(brand)
