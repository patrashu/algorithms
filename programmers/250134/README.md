### 프로그래머스 '수레 움직이기' (레벨 3)

### https://school.programmers.co.kr/learn/courses/30/lessons/250134

### 세트, DFS


```python
def solution(maze):
    answer = [int(1e9)]
    r, c = len(maze), len(maze[0])
    rspt, bspt = None, None
    
    for i in range(r):
        for j in range(c):
            if maze[i][j] in [0, 5]:
                continue
            if maze[i][j] == 1: rspt = (i, j)
            elif maze[i][j] == 2: bspt = (i, j)
            
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    """
    함수 호출 시 rpt, bpt 호출
    도착했으면 pass => Flag로 표현
    """
    rvisit, bvisit = {tuple(rspt)}, set(tuple(bspt))
    def dfs(depth, rpt, bpt, status):
        if answer[0] < depth:
            return

        if sum(status) == 2:
            answer[0] = min(answer[0], depth)
            return
    
        if status[0]:
            for i in range(4):
                nx, ny = bpt[0]+dx[i], bpt[1]+dy[i]
                if nx < 0 or nx >= r or ny < 0 or ny >= c or maze[nx][ny] == 5:
                    continue
                    
                if (nx, ny) not in bvisit:
                    bvisit.add((nx, ny))
                    if maze[nx][ny] == 4:
                        status[1], maze[nx][ny] = True, 5
                        dfs(depth+1, rpt, (nx, ny), status)
                        status[1], maze[nx][ny] = False, 4   
                    else:
                        dfs(depth+1, rpt, (nx, ny), status)
                    bvisit.remove((nx, ny))
            
        elif status[1]:
            for i in range(4):
                nx, ny = rpt[0]+dx[i], rpt[1]+dy[i]
                if nx < 0 or nx >= r or ny < 0 or ny >= c or maze[nx][ny] == 5:
                    continue
                    
                if (nx, ny) not in rvisit:
                    rvisit.add((nx, ny))
                    if maze[nx][ny] == 3:
                        status[0], maze[nx][ny] = True, 5
                        dfs(depth+1, (nx, ny), bpt, status)
                        status[0], maze[nx][ny] = False, 3
                    else:
                        dfs(depth+1, (nx, ny), bpt, status)
                    rvisit.remove((nx, ny))
        
        else:
            rcandit, bcandit = [], []
            for i in range(4):
                nx, ny = bpt[0]+dx[i], bpt[1]+dy[i]
                if nx < 0 or nx >= r or ny < 0 or ny >= c or maze[nx][ny] == 5:
                    continue
                if (nx, ny) not in bvisit:
                    bcandit.append((nx, ny))
                    
            for i in range(4):
                nx, ny = rpt[0]+dx[i], rpt[1]+dy[i]
                if nx < 0 or nx >= r or ny < 0 or ny >= c or maze[nx][ny] == 5:
                    continue
                if (nx, ny) not in rvisit:
                    rcandit.append((nx, ny))
            
            for rc in rcandit:
                for bc in bcandit:
                    if rc == bc or (rc == bpt and bc == rpt):
                        continue
                    rvisit.add(rc)
                    bvisit.add(bc)
                    if maze[rc[0]][rc[1]] == 3 and maze[bc[0]][bc[1]] == 4:
                        maze[rc[0]][rc[1]], maze[bc[0]][bc[1]] = 5, 5
                        status[0], status[1] = True, True
                        dfs(depth+1, rc, bc, status)
                        maze[rc[0]][rc[1]], maze[bc[0]][bc[1]] = 3, 4
                        status[0], status[1] = False, False
                    elif maze[rc[0]][rc[1]] == 3:
                        maze[rc[0]][rc[1]] = 5
                        status[0] = True
                        dfs(depth+1, rc, bc, status)
                        maze[rc[0]][rc[1]] = 3
                        status[0] = False
                    elif maze[bc[0]][bc[1]] == 4:
                        maze[bc[0]][bc[1]] = 5
                        status[1] = True
                        dfs(depth+1, rc, bc, status)
                        maze[bc[0]][bc[1]] = 4
                        status[1] = False
                    else:
                        dfs(depth+1, rc, bc, status)
                    rvisit.remove(rc)
                    bvisit.remove(bc)

    dfs(0, rspt, bspt, [0, 0])
        
    return 0 if answer[0] == int(1e9) else answer[0]
```    