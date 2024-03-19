### 프로그래머스 '괄호 변환' (레벻 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/60058

### Algorithm: Implementation, Stack

```python
def solution(p):
    answer = ""
    ch_dict, stack = { "(": 1, ")": -1 }, []
    while True:
        if len(p) == 0:  # case 1
            break
        
        u, v, cnt = None, None, ch_dict[p[0]]  # case 2
        for i in range(1, len(p)):
            cnt += ch_dict[p[i]]
            if cnt == 0:  # cnt가 0이면 균형
                break
                
        u, v = p[:i+1], p[i+1:]
        cnt, flag = 0, True  
        for ch in u:
            cnt += ch_dict[ch]
            if cnt < 0:  # cnt가 0보다 작으면 )가 더 많은 case => 불균형
                flag = False
                break
                
        if flag:  # case 3
            answer += u
            p = v
            continue
        
        # case 4
        # 4-2 까지만 적용하고 stack에 4-4, 4-3 순으로 추가
        # 거꾸로 넣는 이유는 LIFO니까 4-4가 먼저들어가야 맨 마지막에 추가됨
        answer += "("  # 4-1
        p = v  # 4-2
        u = u[1:-1] # 4-4 
        nu = ""
        for tu in u:
            tmp = '(' if tu == ')' else ')'
            nu += tmp
        stack.append(nu)  
        stack.append(")")  # 4-3

    while stack:
        answer += stack.pop()
    
    return answer
```
