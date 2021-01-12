#3과 5로 묶을수 있는 가장 효율적인 묶음 수 

def suger(N) :
  for y in range(n//3+1):
    for x in range(n//5+1):
      if((x*5+y*3)==n):
        return x+y

  return -1

n = int(input())
print(suger(n))
  

