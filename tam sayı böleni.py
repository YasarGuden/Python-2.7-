sayi=int(raw_input("Pozitif bir say� giriniz:"))
if sayi<0:
    print "Hatal� bir giri� yapt�n�z."
else:
    for i in range(1,sayi+1):
        if sayi%i==0:
            print "Tam say� b�leni:",i
    
