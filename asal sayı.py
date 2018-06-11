sayi=int(raw_input("Pozitif bir tamsayý girin:"))
x=2
for x in range (x,sayi+1):
    i=2
    for i in range (i,x):
        if x%i==0:
            break
        i=i+1
    else:
        print x
    x=x+1
