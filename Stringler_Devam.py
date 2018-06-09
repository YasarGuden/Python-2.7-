#-*- coding: utf-8 -*-
"""
Created on Sun Jun 10 01:21:52 2018

@author: yasar
"""

#Evet stringlerle devam ediyoruz.
#Bu Bölümde Stringlerin  indis özellikleri,toplamı,uzunluğu konularına değinicez.

"Algoritma ve Programlama"[4]
"Algoritma ve Programlama"[10]
"Algoritma ve Programlama"[-2]
"Algoritma ve Programlama"[-8]
#Yukarıdaki işlemleri artık biliyoruz.Şimdi çıtayı bir tık daha arttırıcaz
#Harf değilde belirli bir kelimeyi veya kısmı almak istiyorsak
#Mesela algoritmayı almak istiyorsak  yardıma [:] bu ifade koşuyor.

"""   [2:5]  ifadesi 2. indisden başla 5. indise kadar olan tüm herşeyi al demektir
5. indis dahil değildir.Dikkat etmemiz gereken kısım burasıdır.
Simdi algoritmayı alalım."""


"Algoritma ve Programlama"[0:9] #Şuan algoritma kelimesini elde ettik
#Kısa yollarına geçebiliriz.
"Algoritma ve Programlama"[:9]
# : noktanın sol kısmını boş bırakırsak otomatik olarak 0. indis olarak alıcak
# : noktanın sağ kısmını boş bırakırsak da sonuna kadar alıcak

"Algoritma ve Programlama"[-11:] # programla kelimesini elde ettik
"Algoritma ve Programlama"[:] # Stringi oldugu gibi vericek

"Algoritma ve Programlama"[10:12]# ve kelimesini vericek

""" şimdi diyorusunuz bu indisleri tek tek saymak zorundamıyız.Uzun iş,sıkıcı ve 
gereksiz kelimelerini söylemeden size kurtarıcınızı takdim ediyim. Len fonksiyonu
len fonksiyonuz ingilizce length(uzunluk) kelimesinin kısaltılmışıdır.Bize stringlerin
uzunlugunu,bir sonraki veri tipimiz listelerin eleman sayısını verir."""

len("Algoritma ve Programlama")
# kullanım şekli budur. len 2 parantez arasında string veya liste yazılır
len("Sayma devri len fonksiyonu ile sona erdi.")

#son olarak stringlerin toplamına da bakalım ve diğer veri tipimiz listelere geçelim
#Evet integerlar gibi stringlerde toplana bilir.Bunun sebebi iste stringlerinde 
#birer integer olması.Doğru okudunuz stringler birer tamsayıdır bunu chr fonksiyonumuz 
#ile tespit edeliriz

chr(104) # h harfine denktir.
#toplama işlemi bildiğimiz + oparatörüdür.
"yazilim" + "muhendisligi" #bu ifade bitişik yazılarak sonuç verir
"yazilim " + "muhendisligi" # şeklilde kullanılabilir boşluğumuzu kendimiz koyduk

'P'+'y'+'t'+'h'+'o'+"n"   # python olarak cıktı vericektir.

