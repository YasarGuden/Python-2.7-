dizi=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
maxsatir=len(dizi)
maxsutun=len(dizi)
sutun=[[]for i in range(maxsutun)]
satir=[[]for i in range(maxsatir)]
kose=[[]for i in range(maxsatir+maxsutun-1)]
minkose=-maxsatir+1
for x in range(maxsatir):
    for y in range(maxsutun):
        satir[x].append(dizi[x][y])
        sutun[y].append(dizi[x][y])
        kose[-minkose+y-x].append(dizi[x][y])
print satir
print sutun
print kose
