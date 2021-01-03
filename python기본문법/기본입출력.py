# #데이터의 개수 입력
# n = int(input())
# print(n)
# #각 데이터를 공백을 기준으로 잘라 문자열로으로 입력받기
# data = input().split()
# #공백을 기준으로 잘라 int형으로 입력받기
# print(data)
# data = list(map(int,input().split()))
# print(data)

# a, b, c = map(int,input().split())

# print(a,b,c)

#빠르게 입력받기
import sys
data = sys.stdin.readline().rstrip()
print(data)

#출력
a = 1
b = 2
print(a,b)
print(7, end=" ")
print(8, end=" ")
answer = 7
print("정답은"+str(answer)+"입니다.")

#f-string 
answer = 7
print(f"정답은 {answer}입니다")