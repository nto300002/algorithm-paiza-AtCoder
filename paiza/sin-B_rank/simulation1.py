"""
paiza 君の学校では体力テストがおこなわれており、現在反復横跳びの計測をしています。

いたずら好きの paiza 君は、友達が光の速さで反復横飛びをしている途中、具体的には友達が線を跨ぐのが 4×N 回目になる直前に左の線を元の位置から外側に X cm 遠ざけました。

最終的に友達の反復横跳びの計測結果は K 回となりました。

友達は正規の反復横跳びで計測結果が K 回となるときよりも何 cm 多く移動したでしょうか

なお、今回の反復横跳びでは中央の線を跨いだ状態から始めて、右の線→中央の線→左の線→中央の線→... といった順番で跨いで行くものとします。
"""


N, X, K = map(int, input().split())

if K % 4 == 3:
    # K-4*Nを4で割った商に2*Xを掛け、さらにXを加える
    print(2 * X * ((K - 4 * N) // 4) + X) # +X 画像2　赤い部分が加算されないため
else:
    # K-4*Nを4で割った商に2*Xを掛ける
    print(2 * X * ((K - 4 * N) // 4))

"""
大きい数字が渡ってくることがわかっているため、ループは使わない
2*x 往復分　
4 * N: 線が移動する前の反復回数           画像1の上部分
K - 4 * N: 線が移動した後の追加の反復回数   画像1の下部分  ex
// 4: 4回に1回左の線を跨ぐので、4で割って左線を跨いだ回数を計算

---ex
K: 最終的な合計回数
4*N: 線を移動させる直前の回数
K - 4*N: 線移動後の追加距離が発生する回数

例：N=2, K=10の場合
- 4*N = 8 (8回目の直前で線を移動)
- K = 10 (最終的に10回)
- K - 4*N = 10 - 8 = 2
→ 2回分は追加距離が必要
"""
