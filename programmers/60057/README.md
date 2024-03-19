### 프로그래머스 '문자열 압축' (레벻 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/60057

### Algorithm: Implementation, String

```python
def solution(s):
    answer = len(s)
    
    for pack in range(1, len(s)//2+1):
        tmp, formal, cnt = "", s[:pack], 1
        for j in range(pack, len(s)+pack, pack):
            if formal == s[j:j+pack]:
                cnt += 1
            else:
                if cnt == 1:
                    tmp += formal
                else:
                    tmp += f"{cnt}{formal}"
                formal = s[j:j+pack]
                cnt = 1
        answer = min(answer, len(tmp))
        
    return answer
```
