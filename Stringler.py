# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 00:25:49 2018

@author: yasar
"""

#Pythonda kelimeler,sözcükler,Harfler yani String ifadelerin kullanımın
# 2 şekilde gösterilir

'Birinci kullanım' # 2 tane tek tırnak arasında

"İkinci kullanım" # 2 tane çift tırnak arasında 

#Peki şu şeklilde kullanım nasıl olurdu ?
"yaşar'
# gördüğünüz gibi hata vericek hangi tırnak ile başlıyor ise o tırnak ile bitmelidir.

#Çoğu programla dillerinde oldugu gibi Pythonda da stringleri dilimliyebiliriz
#Stringlerin herhangi bir kısmını(indis) elde etmek için köşeli parantez içinde
#istediğimiz harfin sıra numarasının 1 eksiğini yazarak buluruz.
# indisleme 0 dan başlar  ve stringin sonuna kadar devam eder. 

"Mustafa Kemal Atatürk"[0] #Bu ifade Stringin 1. Harfini vericektir.
"Mustafa Kemal Atatürk"[1] # 'u' harfini vericek
"Mustafa Kemal Atatürk"[2] # 's' harfini vericek
#Görüldüğü gibi gayet basit bir işlem ile istedğimiz harfi alabiliyoruz
#peki aşağıdaki işlem neyi vericek bize?
"Mustafa Kemal Atatürk"[8] 
# 'K' harfini vericek gibi gözüksede " " gibi bir boşluk(whitespace) vericek
#Demek ki tırnaklar arasında boşluklar dahil her ifade bir sıraya sahipmiş

#String ifadelerini en hoş özelliklerinden biri tersden indislemedir.
#Şimdi,Tersden indislemeye öğrenelim
#Bir stringin en sondaki indisini -1 olarak alabiliyoruz.
"Mustafa Kemal Atatürk"[-1]#ifadesi bize 'k' harfini veriyor 
"Mustafa Kemal Atatürk"[-2]#ifadesi bize 'r' harfini vericek
