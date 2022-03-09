def fun():
    a=int(input("enter a numbre"))
    i=1
    while i<=a:
        j=1
        while j<=10:
            print(i,'*',j,'=',i*j)
            j=j+1
        i=i+1
fun()