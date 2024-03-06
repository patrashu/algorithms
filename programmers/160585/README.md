### 프로그래머스  '혼자서 하는 틱택토' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/160585

### Case work

```python
def check(board, target):
    candits = [
        [[0,0], [0, 1], [0, 2]],
        [[1,0], [1, 1], [1, 2]],
        [[2,0], [2, 1], [2, 2]],
        [[0,0], [1, 0], [2, 0]],
        [[0,1], [1, 1], [2, 1]],
        [[0,2], [1, 2], [2, 2]],
        [[0,0], [1, 1], [2, 2]],
        [[0,2], [1, 1], [2, 0]],
    ]
    
    for candit in candits:
        flag = True
        for x, y in candit:
            if board[x][y] != target:
                flag = False
        if flag:
            return True
    return False

def solution(board):
    circle, ax = 0, 0
    
    # counting
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                circle += 1
            elif board[i][j] == 'X':
                ax += 1
    
    # 차이가 2이상이거나 X가 많은 경우
    if abs(circle-ax) >= 2 or ax > circle:
        return 0
    
    answer = 0
    c_flag, a_flag = check(board, "O"), check(board, "X")
    if c_flag and not a_flag:
        if circle-ax == 1:
            answer = 1
    
    elif not c_flag and a_flag:
        if circle-ax == 0:
            answer = 1
        
    elif not c_flag and not a_flag:
        answer = 1
    

    return answer
```