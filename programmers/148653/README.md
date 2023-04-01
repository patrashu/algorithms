### 프로그래머스  '택배 배달과 수거하기' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/150369

### 우선순위 큐, 구현


```python
from heapq import heappop, heappush

def solution(cap, n, deliveries, pickups):
    answer = 0
    dq = []
    pq = []
    total = 0
    
    # 우선순위 큐에 넣기 (최대 힙)
    for i in range(n):
        if deliveries[i]: 
            heappush(dq, (-(i+1), deliveries[i]))
            total += deliveries[i]
        if pickups[i]: 
            heappush(pq, (-(i+1), pickups[i]))
    
    # 큐에서 하나씩 꺼내서 확인
    while dq and pq:
        didx, dcost = heappop(dq)
        pidx, pcost = heappop(pq)
    
        cost = min(total, cap)
        max_idx = max(abs(didx), abs(pidx))
        
        answer += max_idx*2
        total -= cost
        
        # cap이 남을 때 + 배달할 곳이 있을 때
        if cost >= dcost:
            cost -= dcost
        
            while cost and dq:
                ndidx, ndcost = heappop(dq)
                if cost >= ndcost:
                    cost -= ndcost
                else:
                    heappush(dq, (ndidx, ndcost-cost))
                    cost = 0
                    
        # cap이 남지 않을 때
        else:
            heappush(dq, (didx, dcost-cost))
        
        # 돌아갈 때 더 수용 가능하면 
        if cap >= pcost:
            tmp = cap - pcost
            
            while tmp and pq:
                npidx, npcost = heappop(pq)
                if tmp >= npcost:
                    tmp -= npcost
                else:
                    heappush(pq, (npidx, npcost-tmp))
                    tmp = 0
        
        # 더 수용 못하면
        else:
            heappush(pq, (pidx, pcost-cap))

    # 남은 큐 처리
    while dq:
        didx, dcost = heappop(dq)
        cost = cap
        
        if cost >= dcost:
            cost -= dcost
        
            while cost and dq:
                ndidx, ndcost = heappop(dq)
                if cost >= ndcost:
                    cost -= ndcost
                else:
                    heappush(dq, (ndidx, ndcost-cost))
                    cost = 0
        else:
            heappush(dq, (didx, dcost-cost))
        answer += abs(didx) * 2
        
    while pq:
        pidx, pcost = heappop(pq)
        cost = cap
        
        if cost >= pcost:
            cost -= pcost
            
            while cost and pq:
                npidx, npcost = heappop(pq)
                if cost >= npcost:
                    cost -= npcost
                else:
                    heappush(pq, (npidx, npcost-cost)) 
                    cost = 0
        else:
            heappush(pq, (pidx, pcost-cost))
        answer += abs(pidx) * 2
        
        
    return answer
```    