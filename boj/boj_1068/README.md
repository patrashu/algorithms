##  BOJ 1068 (G5)

### https://www.acmicpc.net/problem/1068
### Algorithm: Tree, DFS


``` python
#import sys
from collections import deque
#sys.stdin = open("input.txt", "rt")


def main(n: int, tree_list: list, remove_node: int):
  tree = [[] * n for _ in range(n)]
  root = None
  # search root node
  for i in range(n):
    if tree_list[i] == -1:  # root이면 idx 저장
      if i == remove_node:
        return 0
      root = i
    else:
      if i == remove_node:
        continue
      tree[tree_list[i]].append(i)  # 아니면 부모->자식 단방향 연결

  leaf_cnt = 0
  # search
  dq = deque([root])
  while dq:
    cnode = dq.popleft()
    if len(tree[cnode]) == 0:
      leaf_cnt += 1
      continue
    
    for child in tree[cnode]:
      dq.append(child)

  return leaf_cnt


if __name__ == '__main__':
  print(main(int(input()), list(map(int, input().split())), int(input())))
```


