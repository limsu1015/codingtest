from collections import deque
import sys
input = sys.stdin.read
commands = input().splitlines()
n = int(commands[0])
d = deque()
for i in range(1, n+1):
    command = commands[i].split()
    if command[0] == "push_front":
        d.appendleft(command[1])
    elif command[0] == "push_back":
        d.append(command[1])
    elif command[0] == "pop_front":
        if d:
            d.popleft
            print(d.popleft())
        else:
            print(-1)
    elif command[0] == "pop_back":
        if d:
            d.pop
            print(d.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(d))
    elif command[0] == "empty":
        if d:
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if d:
            print(d[0])
        else:
            print(-1)
    elif command[0] == "back":
        if d:
            print(d[-1])
        else:
            print(-1)
