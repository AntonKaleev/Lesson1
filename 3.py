#3
print('x=', 36/6*2)
#4
print('4*3**2*2=',4*3**2*2)
#5
s='tomato'
t='cucumber'
print('2*s+t=',2*s+t)
#6
s='change me'
s="changE mE"
print(s)
#7
str_1 = "red"
str_2 = "white"
str_3 = "green"
print(str_1 + str_2)
print("_".join([str_1, str_2]))
print("_".join([str_1, str_2]))
print(str_3.find("a"))
print(str_2.find("e"))
print(str_3.split("r"))
#8
mass = [float(a) for a in input().split()]
max=0
index=0
for i in range(0,9):
    if max<mass[i]:
        max=mass[i]
        index=i
print('')
print(index)

