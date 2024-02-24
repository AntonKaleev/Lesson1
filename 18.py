#18
for i in range(3, 11, 4):
    print(i)
#19
lst = [2, 6, 43, 1, 66]
s = 0
for item in lst:
    if item % 2 == 0:
        s += 1
    else:
        continue
print(s)
#20
tol  = 1e-06
x=float(input())
v=1
c=0
i=1
while v>tol:
    v=((-1)**(i-1)*x**i)/i
    c+=((-1)**(i-1)*x**i)/i
    i+=1
print(round(c,ndigits=8))