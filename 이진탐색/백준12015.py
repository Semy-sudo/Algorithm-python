from bisect import bisect_left

N = int(input())
S = list(map(int,input().split()))
db = []

for i in S:
  wh = bisect_left(db,i) #현원소가 db에 들어갈 위치
  if len(db)<=wh:
    db.append(i)
  else:
    db[wh] = i

print(len(db))