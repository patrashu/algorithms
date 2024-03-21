### 프로그래머스  '양과 늑대' (레벨 3)

### https://school.programmers.co.kr/learn/courses/30/lessons/92343

### 백트랙킹


```python
"""
루트에서 시작해서 각 노드를 돌아다니며 양을 모은다
노드 방문 시, 늑대/양이 따라오는데 
양의 수 <= 늑대 수 인 경우 잡아먹힘
=> 최대한 많은 양을 따라오게 하고싶다
"""
from collections import defaultdict

def solution(info, edges):
    answer = [0]
    graph = defaultdict(list)
    for p, c in edges:
        graph[(p, info[p])].append((c, info[c]))
    
    # initialize
    data = [1, 0]
    visited = [False]*len(info)
    visited[0] = True
    
    # dfs
    def dfs(candits):
        answer[0] = max(answer[0], data[0])
        if data[0] <= data[1] or len(candits) == 0:
            return
        for i, (cidx, animal) in enumerate(candits):
            data[animal] += 1
            visited[cidx] = True
            new_candits = candits[:]
            new_candits.pop(i)
            if graph[(cidx, info[cidx])]:
                new_candits.extend(graph[(cidx, info[cidx])])
                new_candits.sort(key=lambda x: x[1])
            dfs(new_candits)
            visited[cidx] = False
            data[animal] -= 1

    dfs(sorted(graph[(0, info[0])], key=lambda x: x[1]))
    return answer[0]
```