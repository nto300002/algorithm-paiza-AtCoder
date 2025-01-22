import io
import sys
import itertools

# テストケースを文字列として定義
test_input = """10011001
"""

# 標準入力を一時的にテスト入力に置き換える
sys.stdin = io.StringIO(test_input)

ns = input()

w = [128,64,32,16,8,4,2,1]
nw = []
for s in ns:
    x = w.pop(0)
    if s == '1':
        nw.append(x)

ans = sum(nw)
print(ans)
        
        

"""
2進数を10進数に変換
"""
