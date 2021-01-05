#1541
str = input().split('-')
print(str)
#입력받은 문자열을 - 기준으로 쪼개기
ary = []
#덧셈이 껴있는 문자열 리스트를 계산해서 정수형 리스트로 변환
for i in str:
  lst = i.split('+')
  sum = 0
  for i in lst:
    sum += int(i)
  ary.append(sum)
print(ary)