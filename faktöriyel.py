f=1
sayi=int(raw_input("Pozitif bir say� giriniz:"))
if sayi<0:
    print "Yanl�� bir giri� yapt�n�z."
else:
    for i in range(1,sayi+1):
        f=f*i
    print "Fakt�riyel sonucu=",f
