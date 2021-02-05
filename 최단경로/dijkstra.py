#다익스트라 알고리즘 = start노드로 부터 다른 노드들 까지의 최단거리
import sys
input = sys.stdin.readline
INF = int(1e9)#무한을 의미하는 값으모 10억 설정

#노드,간선 개수 입력받기
n,m = map(int,input().split())
#시작 노드 번호를 입력받기
start = int(input())
#그래프 입력받기
graph = [[] for _ in range(n+1)]
for i in range(m):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))
#방문 여부 확인
visited = [False]*(n+1)
#최단 거리 테이블을 무한으로 초기화
distance = [INF]*(n+1)

#방문하지 않은 노드 중에서,거리가 최소인 노드 반환

def get_smallest_node():
  min_value = INF
  index = 0
  for i in range(1,n+1):
    if distance[i]<min_value and not visited[i]:
      min_value = distance[i]
      index = i

  return index

def dijkstra(start):
  visited[start] = True
  distance[start] = 0
  #start 노드 인접 노드 먼저 거리 계산
  for i in graph[start]: 
    distance[i[0]] = i[1]

  #start를 제외하고 n-1번 갱신
  for i in range(n-1):
    #현재 그래프에서 가장 비용 적은 노드
    now = get_smallest_node()
    visited[now] = True
    for j in graph[now]:
      cost = distance[now]+j[1]
      #갱신될 비용이 더 적다면 비용 교체
      if cost<distance[j[0]]:
        distance[j[0]] = cost

dijkstra(start)



# 모든 노드로 가기 위한 최단 거리를 출력
for i in distance:
  if i==INF:
    print('infinite')
  #도달할 수 있는 경우 거리를 출력
  else:
    print(i)