sayi=int(raw_input("Pozitif bir sayı giriniz:"))
if sayi<0:
    print "Hatalı bir giriş yaptınız."
else:
    for i in range(1,sayi+1):
        if sayi%i==0:
            print "Tam sayı böleni:",i
    
