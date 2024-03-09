### 프로그래머스 '모음사전' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/84512

### Algorithm: backtracking


```python
def solution(word):
    cnt = [0]
    flag = [True]
    
    def dfs(cur_word, target):
        if cur_word == target:
            print(cur_word, target, cnt[0])
            flag[0] = False
            return
        
        # 5글자 이상은 pass
        if len(cur_word) == 5:
            return
        
        for ch in ["A", "E", "I", "O", "U"]:
            if flag[0]:
                cur_word += ch
                cnt[0] += 1
                dfs(cur_word, target)
                cur_word = cur_word[:-1]
            else:
                break
    
    dfs("", word)
    return cnt[0]
```