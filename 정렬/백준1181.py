#단어정렬
n = int(input())
lis = []
for i in range(n):
  lis.append(input())

my_set = set(lis) #집합set으로 변환
my_list = list(my_set)

my_list = sorted(my_list,key=lambda x: (len(x),x)) #길이순+같은길이일때는 알파벳순

#같은 단어가 여러번 입력된 경우에는 한번씩만 출력


for i in range(len(my_list)):
  print(my_list[i])