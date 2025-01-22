H, W = map(int, input().split())
S = [input() for _ in range(H)]
y, x = map(int, input().split())

# 文字列をリストに変換（変更可能にする）
grid = [list(row) for row in S]

# 移動方向
move = [-1, 1]

# 中心マスの反転
grid[y][x] = '#' if grid[y][x] == '.' else '.'

# 上下左右の反転
for i in move:
    # 上下方向
    if 0 <= y + i < H:
        grid[y + i][x] = '#' if grid[y + i][x] == '.' else '.'
    # 左右方向
    if 0 <= x + i < W:
        grid[y][x + i] = '#' if grid[y][x + i] == '.' else '.'

# 結果出力
for row in grid:
    print(''.join(row))
