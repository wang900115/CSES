n = int(input())
m = list(map(int,input().split()))

move = 0
pre = m[0]

for i in range(n):
  curr = m[i]
  if pre>curr:
    move+=1
  else:
    pre = curr
print(move)
    
  
