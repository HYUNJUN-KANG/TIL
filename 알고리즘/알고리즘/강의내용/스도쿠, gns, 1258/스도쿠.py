def check_sudoku():    # 스도쿠라면 True, 아니라면 False
    # 모든 행 검사
    for i in range(9):
        check = [0]*10
        for j in range(9):
            if check[sudoku[i][j]] == 0:
                check[sudoku[i][j]] = 1
            else:    # 숫자 중복 발생 >> 스도쿠 아님
                return 0

    # 모든 열 검사
    for j in range(9):
        check = [0] * 10
        for i in range(9):
            if check[sudoku[j][i]] == 0:
                check[sudoku[j][i]] = 1
            else:  # 숫자 중복 발생 >> 스도쿠 아님
                return 0

    # 3#3 행렬 9개 검사
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            check = [0] * 10
            for r in range(i, i+3):
                for c in range(j, j+3):
                    if check[sudoku[r][c]] == 0:
                        check[sudoku[r][c]] == 1:
                    else:
                        return 0
    return 1



T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(input().split())) for _ in range(9)]
    # 1~9까지 숫자가 한번씩 나오는지 검사
    # 0  1  2  3  4  5  6  7  8  9
    #[0][0][0][0][0][0][0][0][0][0]
    result = check_sudoku(sudoku)

