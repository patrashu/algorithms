### 프로그래머스  '양궁대회' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/92342

### 백트랙킹


```python
def solution(n, info):
    check = [0]*len(info)
    ans = []
    cnt = 0
    
    def backtrack(depth, idx, remain):
        global cnt
        if depth == n:
            apc, rion = 0, 0
            # 총 점수 계산
            tmp = []
            for i, (n1, n2) in enumerate(zip(info, check)):
                tmp.append(n2)
                if n1 > 0 or n2 > 0:
                    if n1 >= n2:
                        apc += (10-i)
                    else:
                        rion += (10-i)
            
            if rion-apc > 0:
                cnt = 0
                for k in tmp:
                    if k > 0: cnt += 1
                ans.append((rion-apc, cnt, tmp))

        for i in range(idx+1, n+1):
            if i == n:
                check[i] = remain
                backtrack(n, i, 0) 
                check[i] = 0
            else:
                if depth + info[i] + 1 <= n:
                    tmp = info[i] + 1
                    check[i] = tmp
                    backtrack(depth+tmp, i, n-(depth+tmp))
                    check[i] = 0
    
    backtrack(0, -1, n)
    ans.sort(key=lambda x: [-x[0], -x[1]])
    return ans[0][2] if ans else [-1]
```    

### BFS

``` python
from collections import deque

def bfs(n, info):    
    res = []
    q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
    maxGap = 0
    
    while q:
        focus, arrow = q.popleft()
        
        if sum(arrow) == n:  # 종료조건 1) 화살 다 쏜 경우
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            if apeach < lion:  # 라이언이 이기면
                gap = lion - apeach
                if maxGap > gap:
                    continue
                if maxGap < gap:
                    maxGap = gap  # 최대점수차 갱신
                    res.clear()
                res.append(arrow)  # 최대점수차를 내는 화살상황 저장
        
        elif sum(arrow) > n:  # 종료조건 2) 화살 더 쏜 경우
            continue
        
        elif focus == 10:  # 종료조건 3) 화살 덜 쏜 경우
            tmp = arrow.copy()
            tmp[focus] = n - sum(tmp)
            q.append((-1, tmp))
        
        else:  # 화살 쏘기
            tmp = arrow.copy()
            tmp[focus] = info[focus]+1 
            q.append((focus+1, tmp))  # 어피치보다 1발 많이 쏘기
            tmp2 = arrow.copy()
            tmp2[focus] = 0
            q.append((focus+1, tmp2))  # 0발 쏘기
    return res

def solution(n, info):
    winList = bfs(n, info)
    
    if not winList:
        return [-1]
    elif len(winList) == 1:
        return winList[0]
    else:
        return winList[-1]
```