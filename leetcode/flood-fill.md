##  Leetcode week1-9

### https://leetcode.com/problems/flood-fill/description/
### Algorithm: BFS


``` python
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        r, c, scolor = len(image), len(image[0]), image[sr][sc]
        dq = deque([(sr, sc)])
        visited = [[False]*c for _ in range(r)]
        visited[sr][sc] = True

        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        while dq:
            cx, cy = dq.popleft()
            image[cx][cy] = color
            for i in range(4):
                nx, ny = cx+dx[i], cy+dy[i]
                if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                    if image[nx][ny] == scolor:
                        visited[nx][ny] = True
                        dq.append((nx, ny))
        return image
```