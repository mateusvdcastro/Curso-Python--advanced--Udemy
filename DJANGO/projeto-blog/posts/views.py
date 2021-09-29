from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from posts.models import Post


class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 2
    context_object_name = 'posts'


class PostBusca(ListView):
    pass


class PostCategoria(PostIndex):
    pass


class PostDetalhes(UpdateView):
    pass
