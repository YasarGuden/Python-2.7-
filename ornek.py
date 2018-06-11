def ozyinelemeUst(a,n):
    if n==0:
        return 1
    else:
        return a*ozyinelemeUst(a,n-1)

def UstAlma (a,n):
    sonuc=1
    for i in range(n):
        sonuc=sonuc*a
    return sonuc

print ozyinelemeUst (2,5)
print UstAlma(2,5)
