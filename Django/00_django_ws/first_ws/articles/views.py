from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'form.html')


def catch(request):
    name = request.GET.get('name')

    context = {
        'name':: name,
    }

    return render(request, 'catch.html', context)


def index(request):
    return render(request, 'articles/index.html')