s = input()
result = []
length = 1
max_value = float('-inf')
if len(s)==1:
    print(length)
else:
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            length+=1
        else:
            length=1
        max_value = max(length,max_value)
    print(max_value)
 
