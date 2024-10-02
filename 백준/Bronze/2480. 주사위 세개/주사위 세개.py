a, b, c = map(int, input().split())
number = [a, b, c]
max_num = max(number)
if a == b == c:
    print(1000*max_num+10000)
elif a == b !=c or a == c != b:
    print(1000+a*100)
elif b == c != a:
    print(1000+b*100)
else:
    print(max_num*100)