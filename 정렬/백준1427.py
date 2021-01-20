nums = input() #숫자 입력받고
nums = [int(n) for n in nums]#각 숫자 쪼개서 리스트에 넣고

ordered_num = sorted(nums,reverse=True)#내림차순정렬

for i in ordered_num:
  print(i,end="")