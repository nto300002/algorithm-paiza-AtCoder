"""
#条件　3枚の別々の種類のカードから合計kになる組み合わせが何通りあるか調べたい　コードは上記　nは書いてある数字　kは合計
"""

import io
import sys

# テストケースを文字列として定義
test_input = """3 6
"""

# 標準入力を一時的にテスト入力に置き換える
sys.stdin = io.StringIO(test_input)

n, k = map(int, input().split())

count = 0

# i, j を固定して、k = target_sum - (i + j) を計算
for i in range(1, n+1):
    for j in range(1, n+1): #重複を防ぐ(i + 1)
        # 3つ目の数を計算
        t = k - (i + j)
        print(i,j,t)
        
        # 条件チェック
        """
        1 1 4  x n(3)
        1 2 3  1
        1 3 2  2
        ...
        3 3 0 x 0は存在しない
        """
        if 1 <= t <= n:  # t が 1 より大きく、n 以下であることを確認
            count += 1

print(count)
