list=[1,2,4,6,9,10,11,14,21,40]
s = 0
for i in range(0, len(list)):
    if(i%2)==0:
        s = s+list[i]
print("Sum of the even index:",s)