### 프로그래머스 '다단계 칫솔 판매' (레벨 3)

### https://school.programmers.co.kr/learn/courses/30/lessons/77486

### Algorithm: DFS, Implementation

```python
"""
다단계 조직을 이용해서 칫솔 판매
한 명이 칫솔을 판매하면 아래 조직이 수익을 조금씩 받음

모든 판매원은 칫솔의 판매에 의해 발생하는 이익에서 10프로를 계산에서 자신의 추천인에게 배분하고, 나머지를 가짐
내가 팔아서 발생한 이익 + 내가 추천해서 가입시킨 판매원에서 발생하는 이익의 10%까지 이익이 됨
원단위 미만은 x

amount => 10000 => depth 최대 4
4 * 100000 => 40만 (충분)
"""
from collections import defaultdict

def solution(enroll, referral, seller, amount):
    parents, cost = {}, defaultdict(int)
    
    for enr, ref in zip(enroll, referral):
        parents[enr] = ref
    
    for sell, amo in zip(seller, amount):
        amo = amo*100
        
        while parents.get(sell, -1) != -1:
            v = amo // 10
            q = amo - v
            if v == 0:
                cost[sell] += q
                break
            cost[sell] += q
            sell, amo = parents[sell], v
            
    return [cost[k] for k in enroll]
```
