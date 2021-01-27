#자료형 set은 왜 시간복잡도가 O(1)인가
#if num in arr 처럼 어떤 집합에 포함되어 있는지 확인하려면, 리스트는 인덱스 0부터 n까지 일일이 검사 => 시간복잡도 o(n)/set은 o(1)

import sys
input = sys.stdin.readline
n = int(input())
arr = set(map(int,input().split()))
m = int(input())
arr_t = list(map(int,input().split()))

for i in range(len(arr_t)):
  if arr_t[i] in arr:
    print(1,end=' ')
  else: 
    print(0,end=' ')