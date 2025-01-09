def twooddoneout(arr,size):
    xorof2=arr[0]
    x=0
    y=0
    setbit=0
    for i in range(1,size):
        xorof2=xorof2^arr[i]
    setbit=xorof2&~(xorof2-1)
    for i in range(size):
        if (arr[i]&setbit):
            x=x^arr[i]
        else:
            y=y^arr[i]
    print("the two odd elements are:",x,"&",y)
arr=[]
arrsize=int(input("Enter the size of the array:"))
for i in range(0,arrsize):
    z=int(input("Enter a number:"))
    arr.append(z)
twooddoneout(arr,arrsize)

