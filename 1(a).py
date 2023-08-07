m1=int(input("enter the marks for test 1:"))
m2=int(input("enter the marks for test 2:"))
m3=int(input("enter the marks for test 3:"))
if m1<=m2 and m1<=m3:
    avgmarks=(m2+m3)/2
elif m2<=m1 and m2<=m3:
    avgmarks=(m1+m3)/2
else:
    angmarks=(m1+m2)/2
print("avg of best two marks out of three test marks is",avgmarks)    