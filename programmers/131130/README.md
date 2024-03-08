### 프로그래머스  '혼자 놀기의 달인' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/131130

### DFS


```python
def solution(cards):
    answer = []
    cards = [c-1 for c in cards]
    visited = [False]*len(cards)
    
    def dfs(depth, idx, spt):
        n_num = cards[idx]
        if depth != 1 and n_num == spt:
            answer.append(depth-1)
            return True
        
        if not visited[n_num]:
            visited[n_num] = True
            if dfs(depth+1, n_num, spt):
                return True
            visited[n_num] = False
        return False
    
    
    for i in range(len(cards)):
        if visited[i]:
            continue
        dfs(1, i, cards[i])
        
    if len(answer) == 1:
        return 0
    answer.sort()
    return answer[-1]*answer[-2]
```    