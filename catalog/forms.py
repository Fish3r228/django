from django import forms
from .models import Product
from django.core.exceptions import ValidationError

# список запрещённых слов
BAD_WORDS = [
    'казино',
    'криптовалюта',
    'крипта',
    'биржа',
    'дешево',
    'бесплатно',
    'обман',
    'полиция',
    'радар',
]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'is_available']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Стилизация через CSS-классы
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        # Булевое поле – делаем красивым чекбоксом
        self.fields['is_available'].widget.attrs.update({'class': 'form-check-input'})

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        for word in BAD_WORDS:
            if word.lower() in name.lower():
                raise ValidationError(f"Слово '{word}' запрещено в названии продукта.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        for word in BAD_WORDS:
            if word.lower() in description.lower():
                raise ValidationError(f"Слово '{word}' запрещено в описании продукта.")
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError("Цена не может быть отрицательной.")
        return price
