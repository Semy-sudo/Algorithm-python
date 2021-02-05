from bisect import bisect_left

n = int(input())
arr = list(map(int,input().split()))

st = []
for i in arr:
  if bisect_left(st,i)>=len(st):
    st.append(i)
  else:
    st[bisect_left(st,i)] = i

print(len(st))