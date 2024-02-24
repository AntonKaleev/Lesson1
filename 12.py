s1 = {'Рентген','Лоренц','Зееман','Кюри','Милликен', 'Сигбан', 'Франк', 'Герц'}
s2 = {'Фишер','Резерфорд','Кюри','Прегль'}
print(s1.intersection(s2))
if 2**2 > 4:
    print("yes")
if 10 > 100:
    print('yes')
else:
    print('nope')
a = 4
if a/2 > 0:
    print('1')
elif a==4:
    print('2')
elif a < 0:
    print('3')
else:
    print('4')
#16
x=1
y=0
#x,y = map(float, input().split())
if abs(x-4)<2 and abs(y-2)<3 and ((x-1)**2+(y)**2<2**2 and (x-1)**2+y**2>1):
    print('yes yes')
elif  abs(x-4)<2 and abs(y-2)<3 and ((x-1)**2+(y)**2<2**2 and (x-1)**2+y**2>1):
    print('yes no')
elif (abs(x-4)<2  and abs(y-2)<3) and not ((x-1)**2+(y)**2<2**2 and (x-1)**2+y**2>1):
    print('no yes')
elif not (abs(x-4)<2 and abs(y-2)<3) and not ((x-1)**2+(y)**2<2**2 and (x-1)**2+y**2>1):
    print('no no')
#17
pol = input()
abc={1: 'a',2: 'b', 3: 'c',4: 'd',5: 'e',6: 'f',7: 'g',8: 'h'}
pr=0
for i in range(0,7):
    for j in range(0,7):
        if pol==abc[j+1]+str(i+1):
            pr=i+j
            if pr%2==0:
                print('black')
            else:
                print('white')
