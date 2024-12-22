#工事
#N週間続く　2
#13:00時始まり 1h 30m 続く
#終了14:30

#n = int(input())
#t,h,m = input().split()
#times = [list(map(int, input().split())) for _ in range(n)]
n = 2
#t = "13:30"
#h = "1"
#m = "30"
#time=[["15:30","1","30"],["23:20","1","0"]]
for i in range(n):
    t,h,m = input().split()
    t=time[i][0]
    h=time[i][1]
    
    t_h,t_m = t.split(sep=":")
    u_min = int(t_m) + int(m)
    
    #min
    flag = False
    if u_min >= 60:
        flag = True
        overflow = u_min - 60
        t_h = int(t_h)+1
        t_m = overflow
    
    #hour
    t_h = int(t_h)+int(h)
    if t_h > 23:
        t_h = 0
    
    end_h,end_m = t_h,t_m
    h_digits = len(str(end_h))
    m_digits = len(str(end_m))
    
    if h_digits <= 1:
        end_h = str(f'0{end_h}')
    if m_digits <= 1:
        end_m = str(f'0{end_m}')
    
    print(f'{end_h}:{end_m}')
#-------------------------------------------------------------:w
n = int(input())


for i in range(n):
    t,h,m = input().split()
    t_h,t_m = t.split(sep=":")
    u_min = int(t_m) + int(m)

    #min
    flag = False
    if u_min >= 60:
        flag = True
        overflow = u_min - 60
        t_h = int(t_h)+1
        t_m = overflow
    
    #hour
    t_h = int(t_h)+int(h)
    if t_h > 23:
        t_h = 0
    
    end_h,end_m = t_h,t_m
    h_digits = len(str(end_h))
    m_digits = len(str(end_m))
    
    if h_digits <= 1:
        end_h = str(f'0{end_h}')
    if m_digits <= 1:
        end_m = str(f'0{end_m}')
    if flag == False:
        end_m = u_min
    
    print(f'{end_h}:{end_m}')
