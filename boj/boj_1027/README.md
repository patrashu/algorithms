##  BOJ 1027 (G4)

### https://www.acmicpc.net/problem/1027

### Algorithm: Bruteforce


``` python
import sys

def main(n: int, buildings: list[int]):
    max_value = 0
    for i in range(n):
        left, right, grad = 0, 0, [0] * n
        # cal gradient
        for j in range(n):
            if i == j:
                continue
            if j < i:
                grad[j] = (buildings[j] - buildings[i]) / (i - j)
            else:
                grad[j] = (buildings[j] - buildings[i]) / (j - i)
    
    # find maximum dist (left)
    formal_grad = -sys.maxsize
    for j in range(i - 1, -1, -1):
        if grad[j] > formal_grad:
            left += 1
            formal_grad = grad[j]
        else:
            continue

    # find maximum dist (right)
    formal_grad = -sys.maxsize
    for j in range(i + 1, n):
        if grad[j] > formal_grad:
            right += 1
            formal_grad = grad[j]
        else:
            continue
    max_value = max(max_value, left + right)

  return max_value


if __name__ == '__main__':
  n = int(input())
  buildings = list(map(int, input().split()))
  print(main(n, buildings))
```