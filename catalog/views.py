from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

from catalog.models import Product, Contact


class ProductList(ListView):
    model = Product
    template_name = 'catalog/index.html'


class ProductDetail(DetailView):
    model = Product
    template_name = 'catalog/item.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        item = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['item'] = item
        context_data['title'] = item
        return context_data


class ContactsView(ListView):
    model = Contact
    template_name = 'catalog/contacts.html'
