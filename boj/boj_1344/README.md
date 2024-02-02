##  BOJ 1344 (G4)

### https://www.acmicpc.net/problem/1344
### Algorithm: Math, Prob


``` python
import sys
from functools import reduce

def func(x: int, y: int):
  return x*y


def main(n: float, m: float):
  sa, sb = 0, 0
  game = list(range(1, 19))
  c = [2, 3, 5, 7, 11, 13, 17]
  total = reduce(func, game)
  d = []
  
  # 이항계수 구하기
  for i in c:
    bl, br = i, 18-i
    bl = reduce(func, game[:bl])
    br = reduce(func, game[:br])
    d.append(total // (bl*br))

  # 소수일 확률 구하기
  for i in range(7):
    sa += d[i] * pow(n, c[i]) * pow(1-n, 18-c[i])
    sb += d[i] * pow(m, c[i]) * pow(1-m, 18-c[i])

  print(sa+sb-sa*sb)
    


if __name__ == '__main__':
  n = int(input())
  m = int(input())
  main(n/100, m/100)
```


