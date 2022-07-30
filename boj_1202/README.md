##  BOJ 1202 (G2)

### https://www.acmicpc.net/problem/1202
### Algorithm: Greedy, Sort, Priority Queue
### Trial: 3   


#### Non pass Code
- Using Knapsack Algorithm
- sorted by value_per_weights
- Time Error and index Error
``` python
import sys
sys.stdin = open('input.txt', 'rt')
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    dias = [list(map(int, input().split())) for _ in range(n)]
    bags = [int(input()) for _ in range(m)]
    
    value_per_weight = []
    for i in range(n):
        tmp = dias[i][1] / dias[i][0]
        value_per_weight.append([tmp, i])
    value_per_weight = sorted(value_per_weight, key=lambda x:-x[0])
    
    total_v = 0
    
    for bag in bags:
        tmp_idx = []
        for i in range(len(value_per_weight)):
            idx = value_per_weight[i][1]
            if bag > dias[idx][0]:
                tmp_idx.append([value_per_weight[i], i])

        tmp_idx = sorted(tmp_idx, key=lambda x: -x[0][1])
        idx = tmp_idx[0][0][1]
        total_v += dias[idx][1]
        value_per_weight.pop(tmp_idx[0][1])
            
    print(total_v)  
```
#### pass code
- Using Priority Queue
```python
import sys
import heapq
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    dia = []
    bags = []
    
    for _ in range(n):   
        heapq.heappush(dia, list(map(int, input().split())))
        
    for _ in range(m):
        bags.append(int(input()))
        
    bags.sort()
    res = 0
    tmp_dia = []
    for bag in bags:
        while dia and bag >= dia[0][0]:
            w, v = heapq.heappop(dia)
            heapq.heappush(tmp_dia, -v)
            
        if tmp_dia:
            res -= heapq.heappop(tmp_dia)
            
    print(res)
```

