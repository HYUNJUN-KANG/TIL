from django.shortcuts import render

# Create your views here.

def dinner(request, dinner, person):

    context = {
        'dinner': dinner,
        'person': person,
    }

    return render(request, 'dinner.html', context)