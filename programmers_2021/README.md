### 프로그래머스 2021 카카오 '표 편집'

### https://school.programmers.co.kr/learn/courses/30/lessons/81303

### Algorithm: Linked List, Set

- Linked List 사용

```python
from collections import deque

class Node():
    def __init__(self):
        self.next = None
        self.prev = None
        self.is_del = False


def solution(n, k, cmd):

    node_list = [Node() for _ in range(n)]

    for i in range(n-1):
        node_list[i].next = i+1
        node_list[i+1].prev = i

    cur = k
    removed_list = deque()

    for line in cmd:
        line = line.split(' ')

        if len(line) == 2:
            if line[0] == 'U':
                for i in range(int(line[1])):
                    cur = node_list[cur].prev
            else:
                for i in range(int(line[1])):
                    cur = node_list[cur].next

        else:
            if line[0] == 'C':
                node_list[cur].is_del = True
                removed_list.append(cur)

                prev_node = node_list[cur].prev
                next_node = node_list[cur].next

                if prev_node is not None:
                    node_list[prev_node].next = next_node

                if next_node is not None:
                    node_list[next_node].prev = prev_node
                    cur = next_node

                else:
                    cur = prev_node

            else:
                removed_node = removed_list.pop()
                node_list[removed_node].is_del = False

                prev_node = node_list[removed_node].prev
                next_node = node_list[removed_node].next

                if prev_node is not None:
                    node_list[prev_node].next = removed_node

                if next_node is not None:
                    node_list[next_node].prev = removed_node

    ans = []
    for i in range(n):
        if node_list[i].is_del:
            ans.append('X')
        else:
            ans.append('O')

    return ''.join(ans)

```

- Set 사용

```


```
