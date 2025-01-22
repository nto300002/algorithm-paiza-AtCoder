H, W, D = map(int, input().split())

# マップの初期化
grid = [[0 for _ in range(W)] for _ in range(H)]

def is_valid(y, x):
    return 0 <= y < H and 0 <= x < W

def fill_right_up():  # D = 1
    num = 1
    # 左上から右下への対角線を順番に処理
    for sum_idx in range(H + W - 1):
        # 各対角線上のマスを上から下に処理
        y_start = min(sum_idx, H - 1)
        x_start = max(0, sum_idx - H + 1)
        
        y = y_start
        x = x_start
        while y >= 0 and x < W:
            if is_valid(y, x):
                grid[y][x] = num
                num += 1
            y -= 1
            x += 1

def fill_right():  # D = 2
    num = 1
    for y in range(H):
        for x in range(W):
            grid[y][x] = num
            num += 1

def fill_down():  # D = 3
    num = 1
    for x in range(W):
        for y in range(H):
            grid[y][x] = num
            num += 1

def fill_left_down():  # D = 4
    num = 1
    # 左上から右下への対角線を順番に処理
    for sum_idx in range(H + W - 1):
        # 各対角線上のマスを左から右に処理
        y_start = max(0, sum_idx - W + 1)
        x_start = min(sum_idx, W - 1)
        
        y = y_start
        x = x_start
        while y < H and x >= 0:
            if is_valid(y, x):
                grid[y][x] = num
                num += 1
            y += 1
            x -= 1

# 方向に応じて埋め方を変える
if D == 1:
    fill_right_up()
elif D == 2:
    fill_right()
elif D == 3:
    fill_down()
elif D == 4:
    fill_left_down()

# 結果の出力
for row in grid:
    print(*row)

