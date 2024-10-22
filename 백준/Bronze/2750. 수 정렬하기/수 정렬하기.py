n = int(input())
num = []
for i in range(n):
    command = int(input())
    num.append(command)
num.sort()
for a in num:
    print(a)