x=int(raw_input("Ka��nc� basama�a kadar:"))
x1=1
x2=1
if x<1:
    print "Pozitif bir de�er girin."
elif x==1:
    print x1
elif x==2:
    print x1
    print x2
else:
    print x1
    print x2
    for i in range(2,x):
        x3=x1+x2
        print x3
        x1=x2
        x2=x3

    
    
    
    
