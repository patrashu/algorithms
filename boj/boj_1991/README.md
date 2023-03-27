##  BOJ 1991 (S1)

### https://www.acmicpc.net/problem/1991
### Algorithm: Data Structure(Tree), Dict

```python
import sys
# sys.stdin = open('input.txt', 'rt')
input = sys.stdin.readline


class Tree:
    def __init__(self, node, l_child, r_child):
        self.node = node
        self.l_child = l_child
        self.r_child = r_child


def pre_order(node):
    print(node.node, end='')
    if node.l_child != '.':
        pre_order(Tree_list[node.l_child])
    if node.r_child != '.':
        pre_order(Tree_list[node.r_child])

def in_order(node):
    if node.l_child != '.':
        in_order(Tree_list[node.l_child])
    print(node.node, end='')
    if node.r_child != '.':
        in_order(Tree_list[node.r_child])


def postorder(node):
    if node.l_child != '.':
        postorder(Tree_list[node.l_child])
    if node.r_child != '.':
        postorder(Tree_list[node.r_child])
    print(node.node, end='')


if __name__ == '__main__':
    n = int(input())
    Tree_list = {}

    for _ in range(n):
        node, l_child, r_child = input().split()
        Tree_list[node] = Tree(node, l_child, r_child)

    pre_order(Tree_list['A'])
    print()
    in_order(Tree_list['A'])
    print()
    postorder(Tree_list['A'])
```

