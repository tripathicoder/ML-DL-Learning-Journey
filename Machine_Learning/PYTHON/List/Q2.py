list=[1,2,3,2,1]
list_1=[1,2,3]
a=list.copy()
b=list_1.copy()
a.reverse()
b.reverse()
if(list==a):
    print("list is same")
else:
    print("list is not same")
    if(list_1==b):
        print("list_1 is same")
    else:
        print("list_1 is not same") 
