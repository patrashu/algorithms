### 프로그래머스 N진수 게임 (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/17677
### Algorithm: Implementation

```python
"""
n진법 T개의 미리 구할 숫자의 수, M명이 참가, P번에 말함
전체의 길이가 T*M개가 되어야 함 => P번쨰만 추출
"""

def solution(n, t, m, p):
    answer = "0"
    notation = "0123456789ABCDEF"

    for num in range(1, m * t):
        result = ""
        while num > 0:
            num, remainder = divmod(num, n)
            result += notation[remainder]

        answer += result[::-1]

    return answer[p-1::m][:t]
```

```python
def solution(n, t, m, p):
    word, idx, alpha = [], 0, None
    if n > 10:
        alpha = { k: chr(k+55) for k in range(10, n)}
    while True:
        if len(word) >= t*m:
            break
        
        if idx < n:
            if idx >= 10: word.append(alpha[idx])
            else: word.append(idx)
            idx += 1
        else:
            res, tmp = [], idx
            while tmp > 0:
                tmp, mod = divmod(tmp, n)
                if mod >= 10: mod = alpha[mod]
                res.append(mod)
            word.extend(res[::-1])
            idx += 1
    
    return ''.join([str(word[k]) for k in range(p-1, t*m, m)])

```