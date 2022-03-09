def even():
    a=[1,2,4,5,6,100,16,18,19]
    i=0
    while i<len(a):
        if(a[i]%2==0):
            print("even",a[i])
        else:
            print("odd",a[i])
        i=i+1
even()
