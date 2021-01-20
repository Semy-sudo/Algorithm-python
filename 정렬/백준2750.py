n = int(input())
lis = []
for i in range(n):
  lis.append(int(input()))

lis.sort(reverse=True)
for i in range(n):
  print(lis.pop())