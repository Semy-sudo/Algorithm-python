# import sys
# n = int(input())

# lis = []
# for i in range(n):
#   lis.append(int(sys.stdin.readline()))

# lis.sort()

# sum = lis[0]
# total = 0
# if len(lis) == 1:
#   total = lis[0]
# else:
#   for i in range(1,n):
#     sum += lis[i] 
#     total += sum  
# print(total)
# => 안되는 이유 알기

import heapq

n = int(input())
card = []
for _ in range(n):
  heapq.heappush(card,int(input())) #card 리스트에 heap방식으로 넣기

if len(card) == 1:
  print(0)
else:
  result = 0
  while len(card) > 1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    result+= a+b
    heapq.heappush(card,a+b)
  print(result)

