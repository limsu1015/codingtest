x = str(input())
y = str(input())
a = [0] * 26
b = [0] * 26
for i in x:
    a[ord(i) - ord('a')] += 1
for i in y:
    b[ord(i) - ord('a')] += 1
result = 0
for i in range(26):
    result += abs(a[i] - b[i])
print(result)