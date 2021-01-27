from collections import deque
import sys
n = sys.stdin.readline()

def bfs(start):
  q = deque
  q.append(start)
  visited = [0]*n #방문여부 확인
  visited[start] = 1
  while q:
    k = q.pop()
    for i in s[k]:
      if visited[i] == 0:
        q.append(i)
        visited[i] = 1
        result[i] = result[k] +1
 


x,y = map(int,input().split()) #두명의 촌수 찾기
m = sys.stdin.readline()
s = [[] for i in range(n+1)]
result = [0 for i in range(n+1)]
for i in range(m):
  a,b = map(int,input().split())
  s[a].append(b) #각가가 연결된 사람들 표시(1촌관계)
  s[b].append(a)

bfs(a)