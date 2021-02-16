child = [1,2,3]
cookie = [1,1]

child_i, cookie_i = 0,0
while child_i>len(child) and cookie_i>len(cookie):
  if child[child_i]<=cookie[cookie_i]:
    child_i+=1 #먹을수 있는 아이가 하나 생김
  cookie_i+=1

return child_i