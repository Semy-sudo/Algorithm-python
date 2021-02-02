#문제. 어떤 배열에서 특정 수가 몇개 포함되어있는지 찾아보기
from bisect import bisect_left,bisect_right
import sys
input = sys.stdin.readline

def count_number(array,left_num,right_num):
  left_index = bisect_left(array,left_num)
  right_index = bisect_right(array,right_num)
  return right_index - left_index

n,x = map(int,input().split())
array = list(map(int,input().split()))

count = count_number(array,x,x) 
if count ==0:
  print(-1)
else:
  print(count)