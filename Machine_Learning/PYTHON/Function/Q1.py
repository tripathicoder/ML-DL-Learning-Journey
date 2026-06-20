l=[1,2,3,4,5]
print(l[0],end=" ")
print(l[1])
def fun(list):
    for i in list:
        print(i,end=" ")
    return len(list)
print(fun(l))