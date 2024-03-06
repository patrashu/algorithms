### 프로그래머스  '택배 배달과 수거하기' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/150369

### 우선순위 큐


```python
import heapq

def solution(cap, n, deliveries, pickups):
    answer = 0
    dv_q, pk_q = [], [] # 배달, 수거 큐
    length = len(deliveries)    
    for i in range(length):
        if deliveries[i]:
            heapq.heappush(dv_q, -i) # 최대 heap으로
        if pickups[i]:
            heapq.heappush(pk_q, -i)
            
    while True:
        if not dv_q and not pk_q: # 둘다 비면 break
            break
        dv_cap, pk_cap = cap, cap
        
        # cost 처리
        dv_max = -dv_q[0] if dv_q else 0
        pk_max = -pk_q[0] if pk_q else 0
        cost = max(dv_max, pk_max)
        answer += (cost+1)*2

        while dv_q:
            cur_node = -heapq.heappop(dv_q)
            # 여유가 없을 때 처리하고 다시 삽입
            if deliveries[cur_node] > dv_cap:
                deliveries[cur_node] -= dv_cap
                heapq.heappush(dv_q, -cur_node)
                # dv_cap = 0
                break
            # 여유있으면 반복 진행
            else:
                dv_cap -= deliveries[cur_node]
                deliveries[cur_node] = 0
                
                while dv_cap and dv_q:
                    cur_node = -heapq.heappop(dv_q)
                    if deliveries[cur_node] > dv_cap:
                        deliveries[cur_node] -= dv_cap
                        heapq.heappush(dv_q, -cur_node)
                        dv_cap = 0
                    else:
                        dv_cap -= deliveries[cur_node]
                        deliveries[cur_node] = 0
            
        while pk_q:
            cur_node = -heapq.heappop(pk_q)
            # 여유가 없을 때 처리하고 다시 삽입
            if pickups[cur_node] > pk_cap:
                pickups[cur_node] -= pk_cap
                heapq.heappush(pk_q, -cur_node)
                break
            # 여유있으면 반복 진행
            else:
                pk_cap -= pickups[cur_node]
                pickups[cur_node] = 0
                
                while pk_cap and pk_q:
                    cur_node = -heapq.heappop(pk_q)
                    if pickups[cur_node] > pk_cap:
                        pickups[cur_node] -= pk_cap
                        heapq.heappush(pk_q, -cur_node)
                        pk_cap = 0
                    else:
                        pk_cap -= pickups[cur_node]
                        pickups[cur_node] = 0

    return answer
```    