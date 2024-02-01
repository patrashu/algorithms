##  BOJ 1062 (G4)

### https://www.acmicpc.net/problem/1062
### Algorithm: Set, Combinations


``` python
import sys
from itertools import combinations


def main(k: int, words: list[str]) -> int:
  if k < 5:
    return 0

  # 공통적으로 필요한 부분을 제거하고 set로 표현
  total = 0
  initial_set, words_set = {'a', 'n', 't', 'i', 'c'}, {}
  for idx, word in enumerate(words):
    tmp = set([c for c in word])
    # 초기 상태로 워드를 표현할 수 있으면
    if tmp.issubset(initial_set):
      total += 1
    else:
      words_set[idx] = tmp.difference(initial_set)

  # 읽을 수 있는 최대 길이 단어수만큼 필터링
  words_set = list(filter(lambda x: len(x) <= k-5, words_set.values()))
  total_set = set()
  for word_set in words_set:
    total_set = total_set.union(word_set)

  total_list = list(total_set)
  total_list = combinations(total_list, min(k-5, len(total_list)))
  
  cnt = 0
  for candit in total_list:
    candit = set(candit)
    cnt = max(cnt, len(list(filter(lambda x: x.issubset(candit), words_set))))

  
  return total + cnt
                         

if __name__ == '__main__':
  n, k = map(int, input().split())
  words = [list(input().strip()) for _ in range(n)]
  print(main(k, words))
```


