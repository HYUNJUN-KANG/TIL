from django import template
from django.shortcuts import render

register = template.Library()
@register.filter


# Create your views here.
def index(List, i, j):
    return List[int(i)][int(j)]

def card(request):
    articles = [
    ['test title1', 'test content1'],
    ['test title2', 'test content2'],
    ['test title3', 'test content3'],
    ['test title4', 'test content4'],
    ['test title5', 'test content5'],
    ]



    context = {
        'articles': articles,
        'article_0_0': articles[0][0],
        'article_0_1': articles[0][1],
        'article_1_0': articles[1][0],
        'article_1_1': articles[1][1],
        'article_2_0': articles[2][0],
        'article_2_1': articles[2][1],
        'article_3_0': articles[3][0],
        'article_3_1': articles[3][1],
        'article_4_0': articles[4][0],
        'article_4_1': articles[4][1]
    }
   

    return render(request, 'card.html', context)

def community(request):
    articles = [
    ['#', 'Title', 'Content', 'Creation Time'],
    ['test title 1', 'test content 1', 'test creation time1'],
    ['test title 2', 'test content 2', 'test creation time2'],
    ['test title 3', 'test content 3', 'test creation time3'],
    ['test title 4', 'test content 4', 'test creation time4'],
    ['test title 5', 'test content 5', 'test creation time5'],
    ['test title 6', 'test content 6', 'test creation time6'],
    ]

    context = {
        'articles': articles,
        'article_1_0': articles[1][0],
        'article_1_1': articles[1][1],
        'article_1_2': articles[1][2],
        'article_2_0': articles[2][0],
        'article_2_1': articles[2][1],
        'article_2_2': articles[2][2],
        'article_3_0': articles[3][0],
        'article_3_1': articles[3][1],
        'article_3_2': articles[3][2],
        'article_4_0': articles[4][0],
        'article_4_1': articles[4][1],
        'article_4_2': articles[4][2],
        'article_5_0': articles[5][0],
        'article_5_1': articles[5][1],
        'article_5_2': articles[5][2],
        'article_6_0': articles[6][0],
        'article_6_1': articles[6][1],
        'article_6_2': articles[6][2],
    }

    return render(request, 'community.html', context)


def base(request):

    return render(request, 'base.html')