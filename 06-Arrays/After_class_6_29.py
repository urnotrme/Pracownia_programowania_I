ar1=[8, 5, 6, 10, 3, 24, 45, 34, 18]
ar2=[5, 6, 3, 24, 45, 18, 11]
n=0
for i in ar1:
    for x in ar2:
        if i==x:
            n+=1
if n==len(ar2):
    print("YES")
else:
    print("NO")
            











































