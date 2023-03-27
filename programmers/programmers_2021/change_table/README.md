### 프로그래머스 2021 카카오 '표 편집' (레벨 3)

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

- dict 사용

```python
from collections import deque

def solution(n, k, cmd):

    up = dict()
    down = dict()
    del_list = deque()

    for a in range(n):
        up[a] = a-1
        down[a] = a+1


    for line in cmd:
        if len(line) > 1:
            line = line.split(' ')
            if line[0] == 'U':
                for _ in range(int(line[1])):
                    k = up[k]
            else:
                for _ in range(int(line[1])):
                    k = down[k]

        else:
            if line[0] == 'C':
                cur_d = down.pop(k)
                cur_u = up.pop(k)

                down[cur_u] = cur_d
                up[cur_d] = cur_u

                del_list.append([cur_u, k, cur_d])

                if cur_d == n:
                    k = cur_u
                else:
                    k = cur_d

            else:
                add_u, idx, add_d = del_list.pop()

                down[add_u] = idx
                down[idx] = add_d
                up[add_d] = idx
                up[idx] = add_u


    ans = []
    for i in range(n):
        if i in down:
            ans.append('O')
        else:
            ans.append('X')

    return ''.join(ans)

```
