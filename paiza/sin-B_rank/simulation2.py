"""
トランプのシャッフルの種類の一つにパーフェクトシャッフルというものがあり、パーフェクトシャッフルにおける 1 回のシャッフルは次の一連の操作を指します。

1. 全52枚の山札を上半分と下半分に分ける。
2. 下半分の一番下のカード, 上半分の一番下のカード, 下半分の下から 2 番目のカード, 上半分の下から 2 番目のカード, ... , 下半分の一番上のカード, 上半分の一番上のカード という順番でカードを積み重ねていく。

トランプの絵柄をS(スペード), H(ハート), D(ダイア), C(クラブ) と表現するものとし、その絵柄の 1 からキングまでの各カードを S_1 , ... , S_13 のように表現するものとします。

上から S_1, ... , S_13, H_1, ... , H_13, D_1, ... , D_13, C_1, ... , C_13 という順のトランプの山札を用いてパーフェクトシャッフルの操作を K 回おこなった後の山札のカードを上から順に出力してください。

カードの出力には {絵柄のアルファベット}_{カードの数字} の表現法を用いてください。
"""

K = int(input())

S = [];D = [];H = [];C = [];
for i in range(1,14):
    s_i = "S_"+str(i)
    d_i = "D_"+str(i)
    h_i = "H_"+str(i)
    c_i = "C_"+str(i)
    S.append(s_i);D.append(d_i);H.append(h_i);C.append(c_i)

card =[S,H,D,C]
cards = [card for row in card for card in row]


for i in range(K):
    shuffle_card = []
    mid = 26
    l=cards[:mid]
    r=cards[mid:]
    for j in range(mid):
        shuffle_card.append(l[j])
        shuffle_card.append(r[j])
        
    cards = shuffle_card

for c in cards: 
    print(c)

