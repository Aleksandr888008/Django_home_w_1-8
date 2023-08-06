# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from pytils.translit import slugify
from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('name', 'content_blog', 'image_blog', 'is_published')
    success_url = reverse_lazy('blog:list')


class BlogListView_published(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'title': 'Блог'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        object.views_count += 1
        object.save()
        return object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('name', 'content_blog', 'image_blog', 'is_published')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        # Формируем slug
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.name)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        # Перенаправляем на страницу для просмотра данных
        return reverse('blog:view', args=[self.kwargs.get('pk')])
