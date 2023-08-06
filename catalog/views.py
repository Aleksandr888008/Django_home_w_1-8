# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    extra_context = {
        'title': 'Главная'
    }


# def home(request):
#     product_list = Product.objects.all()
#     context = {
#         'object_list': product_list,
#         'title': 'Главная'
#     }
#     return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} {phone} {message}')
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)
