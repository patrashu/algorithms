### 프로그래머스 '거리두기 확인하기' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/81302

### Algorithm: BFS

```python
from collections import deque

def solution(places):
    answer = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    for place in places:
        flag = True
        for i in range(5):
            for j in range(5):
                if not flag or place[i][j] != 'P':
                    continue
                dq = deque([(i, j, 0)])
                while dq:
                    cx, cy, dist = dq.popleft()
                    if [cx, cy] != [i, j] and place[cx][cy] == 'P':
                        flag = False
                        break   
                    if dist == 2:
                        continue
                    
                    for k in range(4):
                        nx, ny = cx+dx[k], cy+dy[k]
                        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5 or place[nx][ny] == 'X':
                            continue
                        dq.append((nx, ny, dist+1))
        if flag:
            answer.append(1)
        else:
            answer.append(0)
    return answer
```
