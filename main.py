from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
      # 각 노드에 연결된 그래프 만들기
      graph = defaultdict(int)
      for i,j in edges:
        graph[i].append(j)
        graph[j].append(i)
      
      leaves = [] #연결된 노드가 하나뿐인 리프노드
      for i in range(n+1):
        if len(graph[i])==1:
          leaves.append(i) #리프노드 넣어주기
      
      new_leaves = []
      while n<2:
        for leaf in leaves:#[]
          neighbor = graph[leaf].pop()
          graph[neighbor].remove(leaf) #서로 제거

          if len(graph[leaf])==1:
            new_leaves.append(neighbor)
        
        leaves = new_leaves

edges = [[1,3],[2,3],[3,4],[3,5],[4,6],[6,10],[5,7],[5,8],[8,9]]

