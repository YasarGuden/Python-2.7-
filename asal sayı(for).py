sayi=int(raw_input("Pozitif bir sayı giriniz:"))
s=0
for i in range(2,sayi+1):
    if sayi%i==0:
        s=s+1
if s==1:
    print "Asal sayıdır."
else:
    print "Asal sayı değildir."
