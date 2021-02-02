import sys
input = sys.stdin.readline
n = int(input())
N = list(map(int,input().split()))
m = int(input())
M = list(map(int,input().split()))
N.sort()

def binary(N,index,start,end):
  mid = (start +end)//2
  if start > end:
    return 0
  if N[mid] == index:
    return 1
  elif N[mid] > index:
    return binary(N,index,start,mid-1)
  else:
    return binary(N,index,mid+1,end)

for i in M:
  start = 0
  end = len(N)-1
  result = binary(N,i,start,end)
  print(result,end=' ')
