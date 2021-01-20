#선택정렬
array = [7,5,9,0,3,1,6,2,4,8]

#최솟값 앞으로 뺴기
for i in range(len(array)):
  min = i
  for j in range(i+1,len(array)):
    if array[min]>array[j]:
      array[min], array[j] = array[j],array[min]

print(array)