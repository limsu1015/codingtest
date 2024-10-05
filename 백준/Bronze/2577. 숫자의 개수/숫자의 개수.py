A = int(input())
B = int(input())
C = int(input())
X = A * B * C
Y = str(X)
for i in range(10):
    print(Y.count(str(i)))