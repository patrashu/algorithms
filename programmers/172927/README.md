### 프로그래머스  '주차 요금 계산' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/172927

### 그리디, 정렬


```python
def solution(picks, minerals):
    # 다 못캐면 리스트 분할
    if sum(picks) * 5 < len(minerals):
        minerals = minerals[:sum(picks)*5]
        
    counted_list = count_minerals(minerals)
    ans = cal_cost(counted_list, picks)
    
    return ans
    
    
    
def count_minerals(minerals):
    i = 0
    counted = []
    flag = True
    
    # 탐색 가능할 때까지
    while flag:
        target = []
        # 아직 캘 광물이 남아있다.
        if i + 5 < len(minerals):
            target = minerals[i:i+5]
        # 캘 광물이 없다. or 5개 미만으로 남아있다.
        else:
            target = minerals[i:]
            flag = False
            
        dias, irons, stones = target.count("diamond"), target.count("iron"), target.count("stone")
        counted.append([dias, irons, stones])
        i += 5
        
    # 다 끝나면 정렬 (그리디)
    counted = sorted(counted, key=lambda x: (-x[0], -x[1], -x[2]))
    return counted

def cal_cost(counted_list, picks):
    result = 0
    for target in counted_list:
        if picks[0] > 0:
            picks[0] -= 1
            result += sum(target)
            
        elif picks[1] > 0:
            picks[1] -= 1
            result += target[0]*5 + target[1] + target[2]
        
        elif picks[2] > 0:
            picks[2] -= 1
            result += target[0]*25 + target[1]*5 + target[2]
            
        else:
            break
    return result
```

- 다 캘수 있는지/ 없는지 판단 
- 5개씩 묶어서 각 묶음당 cost를 구한다.
- 묶은 list를 광물 별 cost가 많이 드는 순서대로 정렬
- 차례대로 피로도 계산

            
    
    