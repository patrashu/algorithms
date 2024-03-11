### 프로그래머스 '삼각 달팽이' (레벻 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/68645

### Algorithm: DFS

```python
def solution(n):
    if n == 1:
        return [1]
    
    direc = { 0: (1, 0), 1: (0, 1), 2:(-1, -1) }
    bound, cnt = sum(list(range(n+1))), 0
    x, y, di = 0, 0, 0
    score = [[0]*n for _ in range(n)]
    
    while cnt < bound:
        cnt += 1
        score[x][y] = cnt
        nx, ny = x+direc[di][0], y+direc[di][1]
        
        if 0 <= nx < n and 0 <= ny < n:
            if score[nx][ny] != 0:
                di = (di+1)%3
                x, y = x+direc[di][0], y+direc[di][1]
            else:
                x, y = nx, ny
            continue
            
        if nx >= n:
            di += 1
        elif ny >= n:
            di += 1
        x, y = x+direc[di][0], y+direc[di][1]
    
    answer = []
    for i in range(n):
        for j in range(i+1):
            if score[i][j] == 0:
                break
            answer.append(score[i][j])
    return answer
```
