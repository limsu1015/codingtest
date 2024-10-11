k = int(input())
num = []
for i in range(k):
    number = int(input())
    if number == 0:
        if num:
            num.pop()
    else:
        num.append(number)
print(sum(num))