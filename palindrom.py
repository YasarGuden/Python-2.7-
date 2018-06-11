def ozKontrolPal (s):
    if len (s)<=1:
        return True
    else:
        return s[0]==s[-1] and ozKontrolPal (s[1:-1])


print ozKontrolPal ('ababa')
print ozKontrolPal ('naber')
print ozKontrolPal ('ala')

def kontrolPal (s):
    a=s[::-1]
    if a==s:
        return True
    else:
        return False

print kontrolPal('ababa')
print kontrolPal('naber')
print kontrolPal('ala')
