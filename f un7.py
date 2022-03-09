def fun():
    a=0
    while a<=1000:
        if a%3==0 and a%7==0:
            print("navgurukul")
        elif a%3==0:
            print("nav")
        elif a%7==0:
            print("navgurukul")
        else:
            print("nothing")
fun()