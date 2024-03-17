### 프로그래머스 프렌즈4블록 (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/17679
### Algorithm: Dict, Implementation

```python
from collections import defaultdict, Counter

def rot90_left(arr):
    return [list(row)[::-1] for row in zip(*arr[::-1])]

def rot90_right(arr):
    return [list(row) for row in zip(*arr)][::-1]

def solution(m, n, board):
    answer = 0
    r, c = len(board), len(board[0])
    board = [list(map(str, k)) for k in board]

    while True:
        remove_pts = []
        
        # 서칭
        for i in range(r-1):
            for j in range(c-1):
                p1, p2, p3, p4 = \
                    board[i][j], board[i][j+1], board[i+1][j], board[i+1][j+1]
                cnt = Counter([p1, p2, p3, p4])
                if p1 != '.' and cnt[p1] == 4:
                    remove_pts.extend([(i, j), (i+1, j), (i, j+1), (i+1, j+1)])
        
        # 더이상 없을 경우
        if len(remove_pts) == 0:
            break
        
        # 방문 처리
        for x, y in set(remove_pts):
            board[x][y] = '.'
        answer += len(set(remove_pts))
            
        # 오른쪽 회전 / sort / 왼쪽 회전
        board = rot90_left(board)
        new_board = []
        
        for line in board:
            tmp = []
            cnt = 0
            for ch in line[::-1]:     
                if ord(ch) < 65:
                    cnt += 1
                else:
                    tmp.append(ch)
            tmp.extend(['.']*cnt)
            new_board.append(tmp)     
        board = rot90_right(new_board)
        board = [list(k) for k in board]

    return answer
```
