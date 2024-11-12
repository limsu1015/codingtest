import sys
input = sys.stdin.read

data = input().split()
n, m = int(data[0]), int(data[1])
a = set(map(int, data[2:2+n]))
b = set(map(int, data[2+n:]))

result = a - b

if result:
    print(len(result))
    print(" ".join(map(str, sorted(result))))
else:
    print(0)