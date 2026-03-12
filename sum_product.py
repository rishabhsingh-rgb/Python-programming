def rational(p1,q1,p2,q2):

    if q1==q2:
        sum_num=p1+p2
        sum_den=q1
    else:      
        sum_num=p1*q2+p2*q1
        sum_den=q1*q2

    prod_num=p1*p2
    prod_den=q1*q2

    print("Sum =",sum_num,"/",sum_den)
    print("Product =",prod_num,"/",prod_den)

p1=int(input("Enter p1: "))
q1=int(input("Enter q1: "))
p2=int(input("Enter p2: "))
q2=int(input("Enter q2: "))

rational(p1,q1,p2,q2)
