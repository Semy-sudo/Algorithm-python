
lis = []
def d(n):
  a = 0
  for i in list(str(n)):
    a+= int(i)
  return a+int(n)

for i in range(1,10001):
  k = d(i)
  lis.append(k)

for b in range(1,10001):
  if b in lis:
    pass
  else:
    print(b)