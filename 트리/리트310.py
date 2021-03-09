class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
      
        if n<=1:
            return [0]
        
        graph = collections.defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
            
        leaves = []
        #첫번째 리트 노드 구하기
        for i in range(n+1):
            if len(graph[i])==1:
                leaves.append(i)
                
        
        #리트 노드 제거하고, 다음 리트 노드 구하기
        while n>2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf) #쌍방제거

                if len(graph[neighbor])==1:
                    new_leaves.append(neighbor)
                    
                leaves = new_leaves
                
        return leaves