### 프로그래머스 오픈 채팅방 (level2)

### https://school.programmers.co.kr/learn/courses/30/lessons/42888
### Algorithm: Implementation

```python
def solution(record):
    answer = []
    
    tmp = []
    uid_dict = {}
    for i in range(len(record)):
        cmd = record[i].split()
        
        if cmd[0] == 'Enter':
            uid_dict[cmd[1]] = cmd[2]
            tmp.append((cmd[0], cmd[1]))
        elif cmd[0] == 'Leave':
            tmp.append((cmd[0], cmd[1]))
        else:
            uid_dict[cmd[1]] = cmd[2]
            
    for cmd, uid in tmp:
        if cmd == 'Enter':
            answer.append(uid_dict[uid]+"님이 들어왔습니다.")
        else:
            answer.append(uid_dict[uid]+"님이 나갔습니다.")
    
    
    return answer
```
