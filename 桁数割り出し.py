n = int(input())
l = [int(input()) for _ in range(n)]

for i in l:
    if i == 0:
        print(i+1)
    for j in range(i):
        i = i // 10
        if i <= 0:
            print(j+1)
            break
        
