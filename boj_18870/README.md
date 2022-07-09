##  BOJ 18870 (S2)

### https://www.acmicpc.net/problem/18870

Algorithm: Set, Dict, sort


``` python
import sys
#sys.stdin = open('input.txt','rt')
input = sys.stdin.readline

if __name__ == '__main__':
    a = int(input())
    num = list(map(int, input().split()))
    score = {}
    
    for k in sorted(num):
        score[k] = a
        
    i = a
    for k in score.keys():
        if score[k] == a:
            score[k] -= i
        i -= 1
        
    for k in num:
        print(score[k], end=' ') 
        
```


