#트리의 부모 찾기

def dfs(n,result,tree):
  stack = [1]
  check = [0]*(n+1)
  while stack:
    parent = stack.pop()
    for i in tree[parent]:#[6,4]
      if check[i] == 0:
        check[i] = 1
        result[i] = parent #result[6,4] = 1
        stack.append(i)
  return  result



n = int(input()) #노드개수
tree = [[] for i in range(n+1)]
result = [0]*(n+1)
for i in range(n-1):
  a,b = map(int,input().split())
  tree[a].append(b)
  tree[b].append(a)

dfs(n,result,tree)
for i in range(2,n+1):
  print(result[i])