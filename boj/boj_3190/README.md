##  BOJ 3190 (G4)

### https://www.acmicpc.net/problem/3190
### Algorithm: Simulation, LinkedList

### Code 1 (60ms) (Linked List)
```python
import sys
# sys.stdin = open("input.txt", "rt")

class Node:
  def __init__(self, x, y):
    self.prev_node = None
    self.next_node = None
    self.pos = [x, y]

class LinkedList:
  def __init__(self) -> None:
    self.head = None
    self.tail = None

  def add_tail(self, node: Node) -> None:
    if self.head is None:
      self.head, self.tail = node, node
    else:
      node.prev_node = self.tail
      self.tail.next_node = node
      self.tail = node

  def pop_head(self) -> None:
    self.head = self.head.next_node
    self.head.prev_node = None

  def search_node(self, node) -> bool:
    start = self.head
    while start.next_node is not None:
      if start.pos == node.pos:
        return True
      start = start.next_node
    return False

  def __str__(self) -> None:
    start = self.head
    lines = "현재 연결 리스트입니다.\n"
    while start is not None:
      lines += f"{start.pos} -> "
      start = start.next_node
    lines += 'None'
    return lines
    

if __name__ == '__main__':
  n = int(input())
  field = [[0]*n for _ in range(n)]
  
  m = int(input())
  for _ in range(m):
    x, y = map(int, input().split())
    field[x-1][y-1] = 1

  dx = [-1, 0, 1, 0]
  dy = [0, 1, 0, -1]
  cmd_idx , cmds = 0, []
  cur_dir = 1
  
  k = int(input())
  for _ in range(k):
    idx, cmd = input().strip().split()
    cmds.append([int(idx), cmd])

  llist = LinkedList()
  llist.add_tail(Node(0, 0))
  cnt = 0
  
  while True:
    cx, cy = llist.tail.pos
    nx, ny = cx + dx[cur_dir], cy + dy[cur_dir]
    n_node = Node(nx, ny)
    llist.add_tail(n_node)
    
    if not (0 <= nx < n and 0 <= ny < n) or llist.search_node(n_node):
      print(cnt+1)
      break 

    if field[nx][ny] == 1:
      field[nx][ny] = 0
    else:
      llist.pop_head()
    cnt += 1

    if cmd_idx < len(cmds) and cmds[cmd_idx][0] == cnt:
      dir = cmds[cmd_idx][1]
      cur_dir = (cur_dir+1)%4 if dir == 'D' else (cur_dir-1)%4
      cmd_idx += 1
```

### Code 2 (76) (list)
```python
import sys
from collections import deque

def simulate():
  queue = deque()
  queue.append([0, 0])
  cnt, dir = 0, 0
  cmd_idx = 0
  
  while queue:
    cnt += 1
    cx, cy = queue[0]
    nx, ny = cx + dx[dir], cy + dy[dir]

    # exit flag
    if nx < 0 or ny < 0 or nx >= n or ny >= n:
      break
    if [nx, ny] in queue:
      break

    queue.appendleft([nx, ny])
    # apple flag
    if field[nx][ny] == 1:
      field[nx][ny] = 0
    else:
      queue.pop()
        
    # cmd
    if cmd_idx < k and cnt == int(cmds[cmd_idx][0]):
      dir = (dir-1)%4 if cmds[cmd_idx][1] == 'L' else (dir+1)%4
      cmd_idx += 1
  
  print(cnt)

if __name__ == '__main__':
  n = int(input())
  field = [[0]*n for _ in range(n)]
  
  m = int(input())
  for _ in range(m):
    x, y = map(int, input().split())
    field[x-1][y-1] = 1

  k = int(input())
  cmds = [input().strip() for _ in range(k)]
  cmds = list(map(lambda x: x.split(), cmds))
  cmds = sorted(cmds, key=lambda x: int(x[0]))

  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]

  simulate()
```