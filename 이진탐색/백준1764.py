import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lis_n = [input().strip() for i in range(n)]
lis_m = [input().strip() for i in range(m)]

duplicate = list(set(lis_n) & set(lis_m)) 

print(len(duplicate)) #개수
for i in sorted(duplicate):
  print(i)
