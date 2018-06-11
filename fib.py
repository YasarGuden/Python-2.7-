def F(n):
    if n == 1 or n==2:
        return 1
    else:
        return F(n-1)+F(n-2)
    
print F(7)
def yaz (son):
    for i in range (son+1):
        print F(i)

yaz(7)
