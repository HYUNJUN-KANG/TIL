arr = [1,2,3,4]
N = 4
selected = [0] * N
T = 2 #원하는 조합의 요소 개수
# selected : 어떤 요소가 선택되었는지 표시하는 배열
# idx : 요소의 인덱스
# cnt : 선택된 요소의 개수
def comb(selected,idx,cnt):
    if cnt == T:
        # 내가 원하는 개수만큼의 요소를 선택했음
        print(selected)
        return
    if idx >= N-1:
        return

    #요소를 선택하거나/ 선택하지 않거나 모든 경우의 수 감안

    selected[idx] = 1   #idx에 해당하는 요소를 포함
    comb(selected,idx+1,cnt+1)
    selected[idx] = 0
    comb(selected,idx+1,cnt)
    return  # 내가 할 수 있는 모든 경우의 수 다 봤으니 내 턴을 종료한다.

comb(selected,0,0)