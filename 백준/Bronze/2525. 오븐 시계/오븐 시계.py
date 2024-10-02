a, b = map(int, input().split( ))
c = int(input())
cook = a*60 + b + c
cook_hour = (cook//60) % 24
cook_minute = cook % 60
if 0 <= a <= 23 and 0 <= b <= 59 and 0 <= c <= 1000:
    print(f'{cook_hour} {cook_minute}')