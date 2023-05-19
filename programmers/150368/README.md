### 프로그래머스  '이모티콘 할인행사' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/150368

### 백트랙킹, 구현


```python
def solution(users, emoticons):
    answer = []
    discounts = [10, 20, 30, 40]
    check = [0]* len(emoticons)
    
    def backtrack(depth):
        if depth == len(emoticons):
            cnt = 0
            res = 0
            for sale, bound in users:
                sum_value = 0
                for i in range(len(check)):
                    if sale <= check[i]:
                        sum_value += emoticons[i] - int(emoticons[i]*(check[i]/100))
                if sum_value >= bound:
                    cnt += 1
                    res -= sum_value
                res += sum_value
            answer.append((cnt, res))
            return
    
        for i in range(len(discounts)):
            check[depth] = discounts[i]
            backtrack(depth+1)
            check[depth] = 0
            
    backtrack(0)
    answer.sort(key=lambda x: (x[0], x[1]))
    return answer[-1]
```    