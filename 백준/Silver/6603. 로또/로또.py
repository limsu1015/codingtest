import sys
input = sys.stdin.readline

while True:
    a = list(map(int, input().split()))
    if a == [0]:
        break

    s, n = a[1:], a[0] - 5


    def rotto(minn, r):
        if len(r) == 6:
            print(*r)
            return

        for i in s[len(r):n + len(r)]:
            if i > minn:
                r.append(i)
                rotto(i, r)
                r.remove(i)


    rotto(0, [])
    print()