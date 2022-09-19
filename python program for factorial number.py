n=int(input("enter the number : "));
factorial=1
if(n<0):
    print("factorial number does not exixt")
else:
    for i in range (1,n+1):
        factorial = factorial * i
        print("the factorial is",factorial)
