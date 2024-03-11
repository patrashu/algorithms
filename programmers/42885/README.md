### 프로그래머스 구명보트 (level2)

### https://school.programmers.co.kr/learn/courses/30/lessons/42885
### Algorithm: Implementation

```python
"가장 무거운 사람이 가장 가벼운 사람과 같이 못타면 혼자 타야함"

def solution(people, limit):
    ans = 0
    people.sort()
    i, j = 0, len(people)-1
    
    while i <= j:
        ans += 1
        if people[i]+people[j] <= limit: # 같이 타면 +1
            i += 1
        j -= 1 # 맨 뒤는 항상 탑승
    return ans
```
