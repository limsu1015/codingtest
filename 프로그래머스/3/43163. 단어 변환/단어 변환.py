def dfs(begin, words, ans, target):
    if begin == target:
        return ans
    diff = []
    for i in range(len(words)):
        diffCnt = 0
        for j in range(len(begin)):
            if words[i][j] != begin[j]:
                diffCnt += 1
        if diffCnt == 1 and words[i] == target:
            ans.append(words[i])
            return ans
        diff.append(diffCnt)
    if not 1 in diff:
        return 0
    else:
        next_word = words[diff.index(1)]
        ans.append(next_word)
        words.pop(diff.index(1))
        dfs(next_word, words, ans, target)

def solution(begin, target, words):
    if not target in words:
        return 0
    else:
        ans = []
        dfs(begin, words, ans, target)
        return len(ans)