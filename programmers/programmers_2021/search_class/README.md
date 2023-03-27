### 프로그래머스 2021 카카오 '순위 검색'(레벻 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/72412

### Algorithm:

- 정확도 성공, 효율성 실패

```python
from collections import defaultdict
import re

def solution(info, query):
    ans = []
    a = defaultdict(list)
    b = {
        'cpp':'a',
        'backend':'a',
        'junior':'a',
        'chicken':'a',
        'java':'b',
        'frontend':'b',
        'senior':'b',
        'pizza':'b',
        'python':'c'
    }

    for line in info:
        tmp = ''
        line = line.split(' ')
        score = line[4]
        for k in line[:4]:
            tmp += b[k]

        a[tmp].append(score)

    for line in query:
        line = line.split(' and ')
        last = line.pop().split(' ')
        line.append(last[0])
        score = last[1]

        tmp = ''
        for word in line:
            if word == '-':
                tmp += '[a-z]'
            else:
                tmp += b[word]

        cnt = 0
        for key in a:
            find = re.compile(tmp)
            p = find.findall(key)
            if len(p) != 0:
                for num in a[key]:
                    if int(num) >= int(score):
                        cnt += 1
        ans.append(cnt)

    return ans
```

- 정확도 성공, 효율성 성공

```python
from itertools import combinations
def solution(info, query):
    answer = []
    db = {}
    for i in info:
        temp = i.split()
        conditions = temp[:-1]
        score = int(temp[-1])
        for n in range(5):
            combi = list(combinations(range(4), n))
            for c in combi:
                t_c = conditions.copy()
                for v in c:
                    t_c[v] = '-'
                changed_t_c = '/'.join(t_c)
                if changed_t_c in db:
                    db[changed_t_c].append(score)
                else:
                    db[changed_t_c] = [score]

    for value in db.values():
        value.sort()

    for q in query:
        qry = [i for i in q.split() if i != 'and']
        qry_cnd = '/'.join(qry[:-1])
        qry_score = int(qry[-1])
        if qry_cnd in db:
            data = db[qry_cnd]
            if len(data) > 0:
                start, end = 0, len(data)
                while start != end and start != len(data):
                    if data[(start + end) // 2] >= qry_score:
                        end = (start + end) // 2
                    else:
                        start = (start + end) // 2 + 1
                answer.append(len(data) - start)
        else:
            answer.append(0)

    return answer
```
