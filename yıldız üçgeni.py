x=int(raw_input("Deðer girin:"))
for i in range (x+1):
    for j in range (x-i):
        print " ",
    for k in range (1,2*i):
        print "*",
    print
