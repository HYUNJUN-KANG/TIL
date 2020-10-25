from django.shortcuts import render, redirect

# Create your views here.
from .models import Article

def index(request):

    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    Article.objects.create(title=title, content=content)

    return redirect('articles:index')


def create(request):
    return render(request, 'articles/create.html')


def detail(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        "article": article,
    }

    return render(request, 'articles/detail.html', context)

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        "article": article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    edit_data = Article.objects.get(pk=pk)

    edit_data.title = request.POST.get('title')
    edit_data.content = request.POST.get('content')

    edit_data.save()

    return redirect('articles:detail', edit_data.pk)


def delete(request, pk):
    del_data = Article.objects.get(pk=pk)
    del_data.delete()

    return redirect('articles:index')