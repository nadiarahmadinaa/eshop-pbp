from django.forms import ModelForm
from main.models import Product

class FreshBakesForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price"]