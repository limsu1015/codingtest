h, m = map(int, input().split( ))
if 0 <= h <= 23 and 0 <= m <= 59:
    if m  < 45 and h != 0:
        print(f'{h-1} {15+m}')
    elif m < 45 and h == 0:
        print(f'23 {15+m}')
    else:
        print(f'{h} {m-45}')