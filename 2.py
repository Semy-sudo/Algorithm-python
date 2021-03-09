# p,n,h = map(int,input().split())
# lis = {i:[] for i in range(5)}
# print(lis)
# for i in range(n):
#   x, y = map(int,input().split())
#   if y<=h:
#     lis[x]+=y

# ans = [[] for _ in range(n)]

# for i in (1,n+1):
#   if h >= sum(lis[i]):
#     ans.append([i,sum(lis[i])*1000])
#   else:
#     ans.append([i,h*1000])
# print(ans)

ans = [[1,1000],[2,1000]]
print(ans)