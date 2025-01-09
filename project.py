def reversebits(number):
    reverse=0
    while(number>0):
        reverse=reverse<<1
        if number&1==1:
            reverse=reverse^1
        number=number>>1
    return reverse
number=int(input("enter the number:"))
print("Number with reversed bits:",reversebits(number))
