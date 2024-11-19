list=[1,2,5,-6,-7,43,0,36,22]
i=0
n=[]
while i < len(list):
    if list[i] > 0:
        n.append(list[i]) #n.append()
        i += 1
    elif list[i] == 0 or list[i] < 0:
        pass
        i += 1
        continue
print(n)


