#-5 10 20
def f1(x):
    if x<0:
        print("error")
    else:
        b=1
        for i in range(1,x+1,1):
            b*=i
        print(b)
f1(10);
f1(20);
f1(-5);


