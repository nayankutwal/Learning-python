def fun (arr, len):
    a=0
    if (len==1):
        return arr[0]
    else:
        a=fun (arr,len-1)
    if(a<arr[len-1]):
        return a
    else:
        return arr[len-1]

print(fun([24,20,40,60],4))
    
# recursion
#def recursion(x):
#    if(x < 1):
#        return
#    else:
#        recursion(x-1)

#recursion(5)