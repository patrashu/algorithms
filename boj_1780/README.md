##  BOJ 1780 (S2)

### https://www.acmicpc.net/problem/1780

Algorithm: Divide and Conquer


``` python
import sys
input = sys.stdin.readline


def div_and_conq(x, y, n):
    global count
    
    check = num_list[x][y]
    for xx in range(x, x+n):
        for yy in range(y, y+n):
            if check != num_list[xx][yy]:
                div = n//3
                for k in range(3):
                    for j in range(3):
                        div_and_conq(x+k*div, y+j*div, div)
                return
              
              
    count[num_list[x][y] + 1] += 1


if __name__ == '__main__':
    ## input
    n = int(input())
    num_list = [list(map(int, input().split())) for _ in range(n)]
    count = [0, 0, 0]

    div_and_conq(0, 0, n)
    for num in count:
        print(num)
        
```


