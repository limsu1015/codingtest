def number(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
m = int(input())
n = int(input())
x = []
for num in range(m, n+1):
    if number(num):
        x.append(num)
if x:
    print(sum(x))
    print(min(x))
else:
    print(-1)