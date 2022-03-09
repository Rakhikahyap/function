
def fun():
    a=[2,4,6,8,9,10]
    b=[4,4,5,7,9,4]
    i=0
    sum=0
    n=[]
    while i<len(a):
        while i<len(b):
            c=a[i]+b[i]
            i=i+1
            n.append(c)
    print(n)
fun()