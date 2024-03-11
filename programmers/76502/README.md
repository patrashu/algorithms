### 프로그래머스 '괄호 회전하기' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/76502

### Algorithm: Bruteforce

```python
from collections import deque

def solution(s):
    answer = 0
    length = len(s)
    s = deque((map(str, s)))
    
    for i in range(length):
        # check
        stack, j = [], 0
        for j in range(length):
            if not stack or s[j] in ['[', '(', '{']:
                stack.append(s[j])
                continue
            if s[j] == ']' and stack[-1] == '[':
                stack.pop()
            elif s[j] == ')' and stack[-1] == '(':
                stack.pop()
            elif s[j] == '}' and stack[-1] == '{':
                stack.pop()
            else:
                break
        
        if not stack:
            answer += 1
        s.rotate(-1)
    
    return answer
```
