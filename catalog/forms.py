# -*- coding: utf-8 -*-
from django import forms

from catalog.models import Product, Version

EXCEPTION_WORDS = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('owner',)

        def clean_name(self):
            """Запрещенные слова при создании товара models product, поле name"""
            cleaned_data = self.cleaned_data['name']
            if cleaned_data in EXCEPTION_WORDS:
                raise forms.ValidationError('Название товара содержит запрещенные слова')
            return cleaned_data

        def clean_description(self):
            """Запрещенные слова при создании товара в models product, поле description"""
            cleaned_data = self.cleaned_data['description']
            if cleaned_data in EXCEPTION_WORDS:
                raise forms.ValidationError('Описание товара содержит запрещенные слова')
            return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
