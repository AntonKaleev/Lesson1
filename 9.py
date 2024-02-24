#9
x = [2, 4, 6, 8, 10, 12]
print(x[-1:2:-2])
print(x[::-2])
print(x[0:0])
print(x[1::3])
print(x[0])
print('')
#10
a = (2, "1", 1, 10, 1)
print( a.index(1))
#11
melt = {'Sn': 232, 'Zn': 420, 'Fe': 1539, 'Ni':
1455,'Si': 1415, 'Be': 1287}
elem=input().split()
elem1=melt[elem[0]]
elem2=melt[elem[1]]
print(elem1-elem2)


