a, b = map(int, input().split( ))
c = int(input())
if 0 <= a <= 23 and 0 <= b <= 59 and 0 <= c <= 1000:
    if b + c >= 60 and a+((b+c)//60) < 24:
        print(f'{a+((b+c)//60)} {(b+c)%60}')
    elif b + c >= 60 and a+((b+c)//60) >= 24:
        print(f'{(a+((b+c)//60))-24} {(b+c)%60}')
    else:
        print(f'{a} {b+c}')