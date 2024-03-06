### 프로그래머스  '이모티콘 할인행사' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/150368

### BFS, DFS

### DFS
```python
def solution(users, emoticons):
    answer = []
    discounts = [10, 20, 30, 40]
    check = [0]* len(emoticons)
    
    def backtrack(depth):
        if depth == len(emoticons):
            cnt = 0
            res = 0
            for sale, bound in users:
                sum_value = 0
                for i in range(len(check)):
                    if sale <= check[i]:
                        sum_value += emoticons[i] - int(emoticons[i]*(check[i]/100))
                if sum_value >= bound:
                    cnt += 1
                    res -= sum_value
                res += sum_value
            answer.append((cnt, res))
            return
    
        for i in range(len(discounts)):
            check[depth] = discounts[i]
            backtrack(depth+1)
            check[depth] = 0
            
    backtrack(0)
    answer.sort(key=lambda x: (x[0], x[1]))
    return answer[-1]
```    

### BFS
```python
import math
from collections import deque

def solution(users, emoticons):
    answer = [0, 0]
    emo_dict = {}
    length = len(users)
    for i, c in enumerate(emoticons):
        tmp = [round(cost, 6) for cost in [c*0.9, c*0.8, c*0.7, c*0.6]] # 높은 순으로
        emo_dict[i] = tmp
        
    dq = deque([(0, [0]*length)]) # depth, user 정보
    user_sidx = [math.ceil(p[0]/10)-1 for p in users] # 할인율 idx 기록

    while dq:
        depth, user_infos = dq.popleft()
        if depth == len(emoticons):
            apply, cost = 0, 0
            for i in range(length):
                if users[i][1] <= user_infos[i]:
                    apply += 1
                else:
                    cost += user_infos[i]
            if answer[0] < apply:
                answer = [apply, cost]
            elif answer[0] == apply and answer[1] < cost:
                answer = [apply, cost]
            continue
        
        # 이모티콘 개수마다 10->40
        for i in range(4):
            new_arr = user_infos[:]
            for j in range(length):
                if i >= user_sidx[j]:
                    new_arr[j] += emo_dict[depth][i]
                else:
                    continue
            dq.append((depth+1, new_arr))
    return answer
```