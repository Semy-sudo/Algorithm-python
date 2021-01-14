#어떤 문자열이 들어왔을때, 최소값을 구하기
arr = input().split('-')

s=0
for i in arr[0].split('+'):
  s+=int(i)
for i in arr[1:]:
  for j in i.split('+'):
    s-=int(j)
print(s)