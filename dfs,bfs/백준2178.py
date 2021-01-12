# #2178
#미로탐색
#최소경로 찾기 = bfs = queue

n,m = map(int,input().split())
s = []
queue = []
#문자열로 입력받은것 주의
for i in range(n):
  s.append(list(input()))

#s를 최소위치정보로 갱신해준다
s[0][0] = 1

#최소경로를 넣을 큐
queue = [[0,0]]
#방향벡터
dy = [0,0,1,-1]
dx = [1,-1,0,0]
while queue:
  #a,b = queue.pop() -> 이거틀림
  a,b = queue[0][0], queue[0][1]
  del queue[0]
  print(a,b)
  for i in range(4):
    x = a+dx[i]
    y = b+dy[i]
    if 0<=x<n and 0<=y<m and s[x][y] == "1":
      s[x][y]= s[a][b]+1
      queue.append([x,y])

print(s[n-1][m-1])



## <<헷갈릴수 있는 개념>>
#queue.pop()은 스택처럼 맨위에 있는 애가 선택
#del queue[0]은 큐처럼 맨 밑에 있는 애가 선택
queue = [[1,2],[3,4]]
a,b = queue.pop()
print(a,b)
print(queue)
queue.append([3,4])
print(queue)

print("=============")
queue = [[1,2],[3,4]]
a,b = queue[0][0], queue[0][1]
del queue[0]
print(a,b)
print(queue)
queue.append([3,4])
print(queue)



