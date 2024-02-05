##  BOJ 1581 (G4)

### https://www.acmicpc.net/problem/1581
### Algorithm: Case work


``` python
import sys

def main(count: list[int]):
  result = 0
  ## 빠르게 시작하는 노래가 있을 때
  if sum(count[:2]) > 0:
    # 느리게 시작하는 case로 못가면
    if count[1] == 0:
      result = count[0]
    else:
      result = count[0] + count[3]
      tmp = 0
      if count[2] == 0:
         tmp += 1
      else:
        tmp = count[2]*2+1 if count[1] > count[2] else count[1]*2
      result += tmp      
  ## 빠르게 시작하는 노래가 없을 때
  else:
    result = count[3] + int(count[2] > 0)

  return result


if __name__ == '__main__':
  print(main(list(map(int, input().split()))))
```