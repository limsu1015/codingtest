s = input()
abc = [0] * 26

for i in s:
    abc[ord(i) - ord('a')] += 1

print(" ".join(map(str, abc)))
