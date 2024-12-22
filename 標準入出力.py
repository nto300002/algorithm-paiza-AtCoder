n = int(input())


for m in range(n):
    name, age = input().split()
    age_inc = int(age)
    print(f'{name} {age_inc+1}')
