### 프로그래머스  '리코쳇 로봇' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/169199

### DFS, BFS


```python (DFS)
dx = [0, 1, 0, -1] 
dy = [1, 0, -1, 0]
r, c = None, None
answer = 10001

def dfs(cur_x, cur_y, board, visited, cnt):
    global answer
    if board[cur_x][cur_y] == 'G':
        answer = min(cnt, answer)
        return
    
    else:
        for i in range(4):
            j = 1
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            
            # move maximum
            while 0 <= nx < r and 0 <= ny < c and board[nx][ny] != 'D':
                j += 1
                nx, ny = cur_x + dx[i]*j, cur_y + dy[i]*j
            
            # move formal point
            nx, ny = nx - dx[i], ny - dy[i]

            # check minimum dist
            if cnt < visited[nx][ny]:
                visited[nx][ny] = cnt
                dfs(nx, ny, board, visited, cnt+1)


def solution(board):
    global r, c, answer
    cur_x, cur_y = None, None
    r, c = len(board), len(board[0])
    # find start point
    for i in range(r):
        if board[i].find("R") != -1:
            cur_x, cur_y = i, board[i].find("R")
    
    # define visited and direction
    visited = [[10001]*c for _ in range(r)]
    
    visited[cur_x][cur_y] = 1
    dfs(cur_x, cur_y, board, visited, 0)    
    
    return answer if answer != 10001 else -1
```

```python (BFS)
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(board):
    answer = 0
    cur_x, cur_y = None, None
    r, c = len(board), len(board[0])
    # find start point
    for i in range(r):
        if board[i].find("R") != -1:
            cur_x, cur_y = i, board[i].find("R")
                
    def bfs():
        q = deque()
        q.append((cur_x, cur_y))
        visited = [[0]*c for _ in range(r)]
        visited[cur_x][cur_y] = 1
        
        while q:
            px, py = q.popleft()
            if board[px][py] == 'G':
                return visited[px][py]
            for i in range(4):
                nx, ny = px, py
                while True:
                    nx, ny = nx+dx[i], ny+dy[i]
                    if 0<=nx<r and 0<=ny<c and board[nx][ny]=='D':
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                    if nx<0 or nx>=r or ny<0 or ny>=c:
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                        
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[px][py] + 1
                    q.append((nx, ny))
        return -1
                    
    answer = bfs()
    if answer > 0:
        answer -= 1
        
    return answer
```