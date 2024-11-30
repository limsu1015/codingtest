import sys
input = sys.stdin.readline

N = int(input())
villages = []
total_population = 0

for _ in range(N):
    x, a = map(int, input().split())
    villages.append((x, a))
    total_population += a

villages.sort()

half_population = total_population / 2
accumulated_population = 0

for x, a in villages:
    accumulated_population += a
    if accumulated_population >= half_population:
        print(x)
        break