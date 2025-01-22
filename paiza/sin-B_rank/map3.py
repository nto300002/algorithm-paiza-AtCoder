h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]
y, x = map(int, input().split())

# 中心のマスを変更
if grid[y][x] == '.':
    grid[y][x] = '#'
else:
    grid[y][x] = '.'

def flip_cell(y,x):
    if 0 <= y < h and 0 <= x < w:
        if grid[y][x] == '.':
            grid[y][x] = '#'
        else:
            grid[y][x] = '.'

for i in range(h): #全てのマス
    flip_cell(i,x)

for j in range(w):
    flip_cell(y,j)

for a in range(-max(h,w), max(h,w)): #範囲の最大化
    flip_cell(y+a, x+a) #右上から

for a in range(-max(h,w), max(h,w)):
    flip_cell(y+a, x-a) #左上から


# 結果の出力
for row in grid:
    print(*row, sep='')
    