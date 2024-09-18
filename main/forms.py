from django.forms import ModelForm
from .models import Product
from django import forms

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
    