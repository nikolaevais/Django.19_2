from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'description', 'image')
    success_url = reverse_lazy('blog:list')


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'slug', 'description', 'image')
    success_url = reverse_lazy('blog:list')

   # def get_success_url(self):
   #     return reverse_lazy('blog:list', kwargs={'pk':self.object.pk})


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')