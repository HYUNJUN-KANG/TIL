from django.shortcuts import render

# Create your views here.
e

def index(request):

    articles = Article.object.all()
    context = {
        'articles': article,
    }

    return render(request, 'articles/index.html', context)


def create(request):
    return render(request, 'articles/create.html', context)


def new(request):
    

    # print(request.GET.get('title'))
    # print(request.GET.get('content'))

    # 1번 방법
    article = Article()
    article.title = request.GET.get('title')
    article.content = request.GET.get('content')

    # 만약 POST 방법이면
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    # 2번 방법
    title = request.GET.get('title')
    content = request.GET.get('content')
    article = Article(title=title, content=content)
    article.save()

    # 3번 방법
    title = request.GET.get('title')
    content = request.GET.get('content')

    Article.objects.create(title=title, content=content)

    return render(request, 'articles/new.html')


    # 만약 index로 바로 가고싶으면
    
    return redirect('articles:index')


    def detail(request, pk):
        article = Article.objects.get(pk=pk)
        context = {
            "article": article,
        }
        return render(request, 'articles/detail.html', context)


    def edit(request, pk):

        return render(request, 'articles/edit.html')


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