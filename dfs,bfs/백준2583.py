m,n,k = map(int,input().split())
s = [[0]*n for _ in range(m)]
for i in range(k):
  x1,y1,x2,y2 = map(int,input().split())
  for j in range(y1,y2):
    for k in range(x1,x2):
      s[j][k] = 1

dx = [0,0,1,-1]
dy = [1,-1,0,0]
lis = [] # 영역의 크기 저장
count = 0
num = 0
for j in range(m):
  for i in range(n):
    if s[j][i]==0:
      stack = []
      stack.append([i,j])
      s[j][i] = 1
      count +=1 #영역 추가
      while stack:
        num +=1
        a,b = stack.pop()
        for i in range(4):
          x = a + dx[i]
          y = b + dy[i]
          if 0<=x<n and 0<=y<m and s[y][x]==0:
            stack.append([x,y])
            s[y][x] = 1
      lis.append(num)
    num = 0

lis.sort()
print(count)
for i in lis:
  print(i,end=' ')

