##Q1. text 를 변형하여 문자로 바꾸기#######################
#힌트) 앞뒤공백을 없애고,중간공백도 없애고, +를1 -를 0으로, 2진법으로 int변환, 문자변환까지
text = [' + -- + - + - ',' + --- + - + ',' + -- + - + - ',' + - + - + - + ']

l = []
for i in text:
  l.append(chr(int(i.strip().replace(' ','').replace('+','1').replace('-','0'),2)))

#join => 문자열 배열을 하나로 합쳐줌
print(''.join(l))


########################################################
#1부터 10까지 짝수만 출력
print([i for i in range(10) if i%2==0])

#구구단 출력
print([f'{i}X{j}={i*j}'for i in range(2,10) for j in range(1,10)])

#replace
print('011011011'.replace('0','!').replace('!','+').replace('+','#'))

#자리수 10으로 맞추줌
print('111'.zfill(10))


s = ['1001010','1000101','1001010','1001100']
#s 2진법 적용한 int형으로 변환 -> 각숫자를 문자변환 
print(list(map(lambda x:chr(int(x,2)) ,s)))

#앞에꺼 function으로 만들어서 map에 적용하기
def f(x):
  return chr(int(x,2))

list(map(f,s)) #s에대해 f적용하기
