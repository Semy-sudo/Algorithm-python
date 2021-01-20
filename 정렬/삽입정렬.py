#삽입정렬
array = [7,5,9,0,3,1,6,2,4,8]

#기준, 기준-1 을 비교해서 자리바꾸기
for i in range(1,len(array)):
  for j in range(i,0,-1):
    if array[j]<array[j-1]:
      array[j],array[j-1] = array[j-1],array[j]
    else:
      break

print(array)