gun=int(raw_input("Gün:"))
ay=int(raw_input("Ay:"))
yil=int(raw_input("Yýl:"))
yiltop=yil*365+1
guntop=yiltop+gun
g=guntop%7
if ay==1:
    g=guntop%7;
elif ay==2:
    g=(guntop+31)%7
elif ay==3:
    g=(guntop+59)%7
elif ay==4:
    g=(guntop+90)%7
elif ay==5:
    g=(guntop+121)%7
elif ay==6:
    g=(guntop+151)%7
elif ay==7:
    g=(guntop+181)%7
elif ay==8:
    g=(guntop+212)%7
elif ay==9:
    g=(guntop+242)%7
elif ay==10:
    g=(guntop+273)%7
elif ay==11:
    g=(guntop+303)%7
elif ay==12:
    g=(guntop+332)%7
if g==0:
    g="Cumartesi"
elif g==1:
    g="Pazar"
elif g==2:
    g="Pazartesi"
elif g==3:
    g="Salý"
elif g==4:
    g="Çarþamba"
elif g==5:
    g="Perþembe"
else:
    g="Cuma"
print g
    
