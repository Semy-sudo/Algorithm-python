#백준 1697
import sys
from collections import deque

n,k = map(int,input().split())

max = 100001
visited = [-1]*max #초기화

visited[n] = 0
q = deque([n])
while q:
  m = q.popleft()
  if m==k:
    print(visited[k])
    sys.exit()# 시스템 종료
  for adj in [m-1,m+1,m*2]:
    if 0<=adj<max and visited[adj] == -1:
      visited[adj] = visited[m]+1
      q.append(adj)
