list1=[1,2,4,6,8,10,17,18,29,40]
list2=[1,2,4,6,8,10,17,18,29,40]
newlist=[]
for i in range(0,len(list1)):
    x=list1[i]
    if(x%2!=0):
        newlist.append(x)
for i in range(0,len(list2)):
    y=list2[i]
    if(y%2==0):
        newlist.append(y)
print(newlist)