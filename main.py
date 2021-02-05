# 도시개수n, 통로개수 m, 메시지 보내고자 하는 도시C 주어짐
# 2~m+1 줄 통로에 대한 정보
# 도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간 공백으로 구분하여 출력

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

#다익스트라 알고리즘 최소힙을 이용하여 distance 완성하기
def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q:
    dist,now = heapq.heappop(q)
    if dist>distance[now]:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost<distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))




n,m,start = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for i in range(m):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))

dijkstra(start)

count = 0
#도달할 수 있는 노드중에서 가장 멀리 있는 노드와 최단거리
max_distance = 0
for i in distance:
  if i != INF:
    count +=1
    max_distance = max(max_distance,i)

#시작 노드 제외해야해서
print(count-1,max_distance)