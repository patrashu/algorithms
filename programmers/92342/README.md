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