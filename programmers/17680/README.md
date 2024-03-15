### 프로그래머스 캐시 (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/17680
### Algorithm: dict

```python
def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities)*5
    
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        try:
            idx = cache.index(city)
            answer += 1
            tmp = cache.pop(idx)
            cache.append(tmp)
        except:
            if len(cache) == cacheSize:
                cache.pop(0)
            answer += 5
            cache.append(city)
    
    return answer
```
