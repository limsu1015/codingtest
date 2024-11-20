import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    stack = []
    vps = input()
    for i in vps:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break

        else:
            if len(stack) == 0:
                print("YES")
            else:
                print("NO")


