### 프로그래머스 '쿼드압축 후 개수 세기' (레벻 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/68936

### Algorithm: DFS

```python
def solution(arr):
    answer = [0, 0]
    depth, length = 0, len(arr)
    while length > 1:
        length //= 2
        depth += 1
    
    def dfs(x, y, depth):
        if depth == 0:
            answer[arr[x][y]] += 1
            return
        
        flag = True
        for i in range(x, x+2**depth):
            for j in range(y, y+2**depth):
                if not flag:
                    break
                if arr[x][y] != arr[i][j]:
                    flag = False
                    break                
        if flag:
            answer[arr[x][y]] += 1
        else:
            dfs(x, y, depth-1)
            dfs(x, y+2**(depth-1), depth-1)
            dfs(x+2**(depth-1), y, depth-1)
            dfs(x+2**(depth-1), y+2**(depth-1), depth-1)
    
    dfs(0, 0, depth)
    
    return answer
```
