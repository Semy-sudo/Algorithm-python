#sum()
result = sum([1,2,3,4,5])
print(result)

#min() max()
min_result = min(7,3,5,2)
max_result = max(7,3,5,2)
print(min_result,max_result)

#eval
result = eval("(3+5)")
print(result)

#sorted()
result = sorted([4,6,2,80,4])
print(result)
result = sorted([4,3,6,2,1],reverse=True)
print(result)

#sorted() with key
array = [('홍길동',35),('이순신',75),('아무개',50)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)