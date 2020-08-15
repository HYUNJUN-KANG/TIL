import random
from django.shortcuts import render


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