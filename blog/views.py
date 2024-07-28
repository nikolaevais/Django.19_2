from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'description', 'image')
    success_url = reverse_lazy('blog:blog_list')


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'slug', 'description', 'image', 'is_published', 'views_counter')
    success_url = reverse_lazy('blog:blog_list')