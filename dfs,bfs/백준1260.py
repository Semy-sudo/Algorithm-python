#1260
from collections import deque
#dfs 정의
#그래프와 시작점이 주어졌을때
def dfs(graph,v):
  stack=[]
  check=[]
  stack.append(v)
  while stack:
    t = stack.pop()
    if t not in check:
      check.append(t)
      stack += reversed(graph[t])

  return check

def bfs(graph,v):
  check= []
  queue = deque([v])

  while queue:
    t = queue.popleft()
    if t not in check:
      check.append(t)
      queue+=graph[t]
  return check

#정점의개수, 간선의 수, 시작
n,m,v = map(int,input().split())

#dfs 맞춤 그래프 만들기
graph = {i: [] for i in range(1,n+1)}

for i in range(m):
  x,y = map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)


for i in range(1,n+1):
  graph[i].sort()
#리스트를 공백 포함해 문자열로 변환
print(' '.join(list(map(str,dfs(graph,v)))))
print(' '.join(list(map(str,bfs(graph,v)))))

