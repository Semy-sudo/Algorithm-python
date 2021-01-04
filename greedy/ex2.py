#공포도가 x인 모험가는 반드시 x명 이상 그룹에 참여
#N명에 대한 모험가 정보 주어졌을때 여행떠날수 있는 그룹 수
# 5명 -> [2,3,1,1,2] -> 3

#내림차순 정렬 1 2 2 3 4 

#[공포도 입력받기]
data = list(map(int,input().split()))
data.sort()
count = 0
result = 0

for i in data:
  count += 1
  if count>=i:
    result +=1
    count = 0

print(result)