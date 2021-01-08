#dfs 알고리즘은 노드 방문권을 넘겨줌
def dfs(graph,v,visited):
  visited[v] = True
  print(v, end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)



# 1. 그래프를 알고
graph = [
  [],
  [2,3,8], #노드 1에 연결되어 있는 노드들
  [1,7], # 노드 2에 연결되어 있는 노드들
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]
#2. 노드별 방문여부를 리스트로 나태내면
visited = [False]*9 

#3. dfs 를 구할수 있다.
dfs(graph,1,visited) # 그래프, 시작노드, 방문여부 알려줌





