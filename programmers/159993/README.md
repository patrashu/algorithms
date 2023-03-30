### 프로그래머스  '미로 탈출' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/159993

### BFS


```python (BFS)
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(spt, ept, row, col, maps, pt):
    queue = deque()
    queue.append((spt[0], spt[1]))
    visited = [[0]*col for _ in range(row)]
    visited[spt[0]][spt[1]] = 1
    while queue:
        cx, cy = queue.popleft()
        
        # 한 방향씩 탐색
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            # map 안에 있으면
            if 0 <= nx < row and 0 <= ny < col and maps[nx][ny] != 'X':
                if visited[nx][ny] == 0 and maps[nx][ny] != pt:
                    visited[nx][ny] = visited[cx][cy] + 1
                    queue.append((nx, ny))
                    
                # 기존 값보다 작으면 최소값 저장 후 큐에 삽입
                else:
                    if visited[nx][ny] > visited[cx][cy] + 1:  
                        visited[nx][ny] = visited[cx][cy] + 1
                        queue.append((nx, ny))
    return visited


def solution(maps):
    row, col = len(maps), len(maps[0])
    # 시작, 래버, 목표 pts
    sx, sy, lx, ly, gx, gy = None, None, None, None, None, None   
    for i in range(row):
        if 'S' in maps[i]:
            sx, sy = i, maps[i].find('S')
        if 'L' in maps[i]:
            lx, ly = i, maps[i].find('L')
        if 'E' in maps[i]:
            gx, gy = i, maps[i].find('E')
    
    cnt = 0
    visited = bfs((sx, sy), (lx, ly), row, col, maps, 'S')
    if visited[lx][ly] == 0:
        return -1
    cnt += visited[lx][ly]-1
        
    g_visited = bfs((lx, ly), (gx, gy), row, col, maps, 'L')
    if g_visited[gx][gy] == 0:
        return -1
    cnt += g_visited[gx][gy] - 1

    return cnt
```