n = int(input())
word = [list(map(lambda x: ord(x)-65, input().rstrip())) for _ in range(n)]

alpha = [0]*26

for i in range(n):
  k = 0
  for j in word[i][::-1]:
    alpha[j] += 10**k
    k+=1


alpha.sort(reverse = True) #해당 알파벳을 내림차순으로 정렬

ans = 0
t = 9
for i in range(26):
  if alpha[i]==0:
    break
  ans += t*alpha[i]
  t-=1

print(ans)
