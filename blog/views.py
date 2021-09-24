from django.shortcuts import render
from .models import Post, Categoria

# Create your views here.
def blog(request):
    cate = Categoria.objects.all()
    post = Post.objects.all()
    return render(request, 'blog/blog.html', {'post': post, 'categoria': cate})

def categoria(request, categoria_id):
    cate = Categoria.objects.get(id=categoria_id)
    post = Post.objects.filter(categorias=cate)
    return render(request, 'blog/blog_categorias.html', {'categoria': cate, 'post': post})