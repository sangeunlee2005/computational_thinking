import random
# 9x9 스도쿠 보드 생성
board = [[0] * 9 for _ in range(9)]

def is_valid(y, x, num):
    # 행 검사
    for i in range(9):
        if board[y][i] == num:
            return False
    # 열 검사
    for i in range(9):
        if board[i][x] == num:
            return False
    # 3x3 박스 검사
    start_y = (y // 3) * 3
    start_x = (x // 3) * 3

    for i in range(start_y, start_y + 3):
        for j in range(start_x, start_x + 3):
            if board[i][j] == num:
                return False
    return True

def fill_board():
    for y in range(9):
        for x in range(9):
            # 빈 칸 찾기
            if board[y][x] == 0:
                nums = list(range(1, 10))
                random.shuffle(nums)
                for num in nums:
                    if is_valid(y, x, num):
                        board[y][x] = num
                        if fill_board():
                            return True
                        board[y][x] = 0
                return False
    return True

fill_board()

# 출력
for row in board:
    print(*row)