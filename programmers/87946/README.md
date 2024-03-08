### 프로그래머스 '피로도' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/87946

### Algorithm: DFS


```python
def solution(k, dungeons):
    answer = [0]
    length = len(dungeons)
    visited = [False]*length
    
    def bt(depth, hp):
        answer[0] = max(depth, answer[0])
        if depth == length:
            return
        
        # 탐색
        for i in range(length):
            if visited[i]:
                continue
            limit, use = dungeons[i]
            if limit <= hp:
                visited[i] = True
                bt(depth+1, hp-use)
                visited[i] = False
    
    bt(0, k)
    return answer[0]
```