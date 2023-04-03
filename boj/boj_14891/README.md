##  BOJ 14891 (G5)

### https://www.acmicpc.net/problem/14891
### Algorithm: Implementation, deque

```python
import sys
from collections import deque
input = sys.stdin.readline


def move_crank(arr, dir):
  tmp = arr
  if dir == 1:
    tmp = arr[-1] + arr[:-1]
  else:
    tmp = arr[1:] + arr[0]

  return tmp


if __name__ == '__main__':
  cranks = deque()

  # input을 받아온다.
  for _ in range(4):
    cranks.append(input().strip())

  n = int(input())
  moves = [list(map(int, input().split())) for _ in range(n)]

  for num, dir in moves:
    turn = None
    num = num - 1

    # 움직일 방향을 설정
    if dir == 1:
      if num in [0, 2]:
        turn = [1, -1, 1, -1]
      else:
        turn = [-1, 1, -1, 1]

    else:
      if num in [0, 2]:
        turn = [-1, 1, -1, 1]
      else:
        turn = [1, -1, 1, -1]

    # 움직임
    if num == 0:
      i = 0
      while i < 3:
        if turn[i] != 0 and cranks[i][2] != cranks[i + 1][6]:
          pass
        else:
          turn[i + 1] = 0
        i += 1

    elif num == 1:
      if cranks[0][2] == cranks[1][6]: turn[0] = 0
      if cranks[1][2] == cranks[2][6]: turn[2] = 0
      if turn[2] == 0 or cranks[2][2] == cranks[3][6]: turn[3] = 0

    elif num == 2:
      if cranks[1][2] == cranks[2][6]: turn[1] = 0
      if cranks[2][2] == cranks[3][6]: turn[3] = 0
      if turn[1] == 0 or cranks[0][2] == cranks[1][6]: turn[0] = 0

    else:
      i = 3
      while i > 0:
        if turn[i] != 0 and cranks[i][6] != cranks[i - 1][2]:
          pass
        else:
          turn[i - 1] = 0
        i -= 1
        
    # 최종 회전
    for i in range(4):
      if turn[i] != 0:
        cranks[i] = move_crank(cranks[i], turn[i])

  ans = 0
  tmp = 1
  for i in range(4):
    if cranks[i][0] == '1':
      ans += tmp
    tmp *= 2

  print(ans)
```
- python의 deque에 rotate() 내장함수가 있는지 처음 알게 되었다.
- 다음에는 활용해보도록 하자.