f=1
sayi=int(raw_input("Pozitif bir sayı giriniz:"))
if sayi<0:
    print "Yanlış bir giriş yaptınız."
else:
    for i in range(1,sayi+1):
        f=f*i
    print "Faktöriyel sonucu=",f
