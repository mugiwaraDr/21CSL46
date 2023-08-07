num=int(input("enter a number"))
val=str(num)
if val==val[::-1]:
    print("the number is palindrome")
else:
    print("the number is not a palindrome")
for i in range(10):
    if val.count(str(i))>0:
        print(str(i),"appears",val.count(str(i)),"times")