##  BOJ 14890 (G3)

### https://www.acmicpc.net/problem/14890
### Algorithm: Simulation, Implement

```python
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def rotate(arr):
  new_field = [[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      new_field[n-j-1][i] = field[i][j]
  return new_field

def check_slide(route) :
    ramp = [0]*n
    for i in range(n-1) :
        if route[i] != route[i+1] :
            if abs(route[i] - route[i+1]) > 1 :
                return False
            else :
                if route[i] - route[i+1] == 1 :
                    if i+1+l > n : return False
                    check = route[i+1]
                    for j in range(i+1, i+1+l) :
                        if ramp[j] or route[j] != check : return False
                        ramp[j] = 1
                elif route[i] - route[i+1] == -1 :
                    if i-l < -1 : return False
                    check = route[i]
                    for j in range(i, i-l, -1) :
                        if ramp[j] or route[j] != check : return False
                        ramp[j] = 1
    return True
                   

if __name__ == '__main__':
  n, l = map(int, input().split())
  field = [list(map(int, input().split())) for _ in range(n)]
  ans = 0


  for _ in range(2):
    for i in range(n):      
      if check_slide(field[i]): ans += 1
        
    field = rotate(field)

  print(ans)
```