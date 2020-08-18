from django.shortcuts import render

# Create your views here.
import requests
import random

def lotto(request):

    url = "http://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=924"
    response = requests.get(url).json()
    
    # 이번 회차 당첨 번호
    winner = []

    for i in range(1, 7):
        winner.append(response.get(f'drwtNo{i}')
    bonus = response.get('bnusNo')

    # 천번 돌리기
    win_rate = {
     '1등': 0,
     '2등': 0,
     '3등': 0,
     '4등': 0,
     '5등': 0, 
      '꽝': 0,
      }
    for _ in range(1000):
        # 내가 뽑은 로또
        numbers = random.sample(range(1, 46), 6)
        matched = 0
        
        # 1. numbers에 이는 값을 하나씩 뽑아서 winner에 있는지 확인
        for num in numbers:
            if num in winner:
                matched += 1
        
        # 2. set을 이용해서 교집합


        if matched == 6: # 1등
            win_rate['1등'] += 1
        elif matched ==  5 and bonus in numbers: # 2등
            win_rate['2등'] += 1
        elif matched == 5:
            win_rate['3등'] += 1
        elif matched == 4:
            win_rate['4등'] += 1
        elif matched == 3:
            win_rate['5등'] += 1
        else:
            win_rate['꽝'] += 1
        
    context = {
        'numbers': numbers,
        'winner': winner,
        'bonus': bonus,
        'win_rate': win_rate,
    }



    return render(request, 'lotto.html', context)