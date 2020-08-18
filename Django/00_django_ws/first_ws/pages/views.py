from django.shortcuts import render
import random
from datetime import datetime


# Create your views here.


def lotto(request):
    b = []

    for i in range(1, 100):
        b.append(i)

    pick = []

    for i in range(6):
        pick_1 = random.choice(b)
        pick.append(pick_1)
        
    context = {
        'pick': pick,
    }
    return render(request, 'lotto.html', context)


def dtl(request):
    my_sentence = 'Life is short, you need python'
    menus = ['a', 'b', 'c']
    datetimenow = datetime.now()
    context = {
        'my_sentence': my_sentence,
        'menus': menus,
        'datetimenow': datetimenow,
    }
    return render(request, 'dtl.html', context)

def index(request):
    return render(request, 'pages/index.html')