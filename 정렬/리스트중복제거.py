#리스트에서 중복된값 제거하기2가지
##<set>(집합 자료형)이용
##1.중복을 허용하지 않는다. 2.순서가 없다.

my_list = ['A','B','C','A']
my_set = set(my_list)
my_list = list(my_set)

##<for문>
my_list = ['A','B','C','A']
new_list = []
for v in my_list:
  if v not in new_list:
    new_list.append(v)
print(new_list)