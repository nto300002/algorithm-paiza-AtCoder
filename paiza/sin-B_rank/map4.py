"""
マップへのナンバリング問題
問題文
マップの行数 H と列数 W とナンバリングの向き D が与えられるので、(0, 0) から指示通りにナンバリングした時のマップを出力してください。

ナンバリングの規則
数字は1から始まり、1つ進むごとに1ずつ増加
方向Dによって進み方が異なる：
D = 1 (右上方向)
例: 3×4マップ
1  3  6  9
2  5  8  11
4  7  10 12
D = 2 (右方向)
例: 3×4マップ
1  2  3  4
5  6  7  8
9  10 11 12
D = 3 (下方向)
例: 3×4マップ
1  4  7  10
2  5  8  11
3  6  9  12
D = 4 (左下方向)
例: 3×4マップ
1  4  8  11
2  6  9  12
3  7  10 13
"""

def fill_right_up():
    # 右上方向へのナンバリング
    # y_start, x_start: 開始位置
    # 右上に進みながら番号を振り、はみ出したら下の行から再開
    global num
    y_start = 0
    x_start = 0
    while x_start < W:
        y = y_start
        x = x_start
        while y >= 0 and x < W: #右上方向へ移動 yが0になる　または　xがWより大きくなるまでループ
            if y < H:  #範囲内かチェック
                grid[y][x] = num #番号を振る
                num += 1  #数字をインクリメント
            y -= 1  #上
            x += 1  #右
        if y_start < H - 1:  #始動位置　下に移動可能な場合
            y_start += 1
        else:                #下にたどり着いた場合
            x_start += 1

def fill_right():
    global num
    for i in range(H):
        for j in range(W):
            grid[i][j] = num
            num += 1

def fill_down():
    global num
    for j in range(W):
        for i in range(H):
            grid[i][j] = num
            num += 1

def fill_left_down():
    global num
    y_start = 0
    x_start = 0
    while y_start < H:
        y = y_start
        x = x_start
        while y < H and x >= 0:
            if is_valid(y, x):
                grid[y][x] = num
                num += 1
            y += 1
            x -= 1
        if x_start < W - 1:
            x_start += 1
        else:
            y_start += 1

def is_valid(y, x):
    return 0 <= y < H and 0 <= x < W

# メイン処理
H, W, D = map(int, input().split())
grid = [[0] * W for _ in range(H)]
num = 1

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
