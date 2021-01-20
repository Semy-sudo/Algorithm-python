#퀵정렬
#기준 데이터를 설정하고, 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꿈
#Pivot 으로 기준데이터 설정
array =  [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
  if start>=end:
    return 
  pivot = start
  right = end
  left = start+1
  while(left<=right):#전복될때 까지 반복
    while(left<=end and array[left]<=array[pivot]):
      left += 1
    while(right>start and array[right]>=array[pivot]):
      right -=1
    if(left>right):
      array[pivot],array[right] = array[right],array[pivot]
    else:
      array[left], array[right] = array[right], array[left]
  quick_sort(array,start,right-1)
  quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)