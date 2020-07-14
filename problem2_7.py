def problem2_7():
    a=float(input('Enter length of side one: '))
    b=float(input('Enter length of side two: '))
    c=float(input('Enter length of side three: '))
    s=.5*(a+b+c)
    s1=(s*(s-a)*(s-b)*(s-c))**.5
    print('Area of a triangle with sides',a,b,c,'is',s1)
    