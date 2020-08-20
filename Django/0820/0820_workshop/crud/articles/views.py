from django.shortcuts import render

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
    article = Article(title=title, content=content)
    article.save()

    return render(request, 'articles/new.html')


def create(request):
    title = reqeust.POST.get('title')
    content = request.POST.get ('content')

    article = Article.objects.create(title=title, content=content)

    return redirect('articles:index')


def detail(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        "article": article
    }

    return render(request)