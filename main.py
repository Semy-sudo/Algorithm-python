#1/6일 다시 풀어보기


#반복적으로 구현
# def func1(n):
#   result = 1
#   for i in range(1,n+1):
#     result *=i
#   return result

# #재귀적으로 구현
# def func2(n):
#   if n<=1:
#     return 1
#   return n*func2(n-1)

#유클리드 호제법(최대공약수 구하기)
# def gcd(a,b):
#   if a%b == 0:
#     return b
#   else:
#     return gcd(b,a%b)

# print(gcd(192,162))

#DFS 예제

#행 열 값 입력받기
m,n = map(int,input().split())
#그래프에 리스트 n 개 만큼 넣어주기
graph = []
for i in range(m):
  graph.append(list(map(int,input())))
# dfs 정의하기 0이 있는것들 주변 1로 바꾸고 True반환
def dfs(x,y):
  if x<=-1 or x>=m or y<=-1 or y>=n:
    return False
  if graph[x][y] == 0:
    graph[x][y] = 1
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
  return False 

#dfs 가 True라면 결과값 1 증가
result = 0
for i in range(m):
  for j in range(n):
    if dfs(i,j) == True:
      result +=1
print(result)


