### 프로그래머스 단어 변환 (level 3)

### https://school.programmers.co.kr/learn/courses/30/lessons/43163

### Algorithm: Binary Search

```python
def solution(begin, target, words):
    if target not in words:
        return 0
        
    length, answer = len(begin), [int(1e9)]
    visited = [False] * len(words)
    
    def dfs(depth, ch):
        if ch == target:
            answer[0] = min(answer[0], depth)
            return
        
        candits = []
        for idx, word in enumerate(words):
            if visited[idx]:
                continue
            cnt = length
            for i in range(length):
                if ch[i] == word[i]:
                    cnt -= 1
            if cnt == 1:
                candits.append((idx, word))
                
        for idx, word in candits:
            visited[idx] = True
            dfs(depth+1, word)
            visited[idx] = False
        
    dfs(0, begin)
    return answer[0]
```
