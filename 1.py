room=int(input())
s=[]
for i in range(0,4):
    for j in range(0,8):
        s.append([j+1,i+1])
print(s[room-1][0], s[room-1][1])




