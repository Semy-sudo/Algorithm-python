#연속하는 8일중 5일만 사용가능 총 16일의 휴가가 있을떄

i = 1
while (True):
  l,p,v = map(int,input().split())
  if l+p+v == 0:
    break
  ans = (v//p)*l
  ans += min((v%p),l)
  print('Case %d: %d' %(i, ans))
  i+=1