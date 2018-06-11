def F(n):
    if n == 1 or n==2:
        return 1
    else:
        return F(n-1)+F(n-2)
    
print F(7)


def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a
print fib(7)
