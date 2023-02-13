import timeit
#iteratif
def deret_ajaib1(n): 
    x = 1 
    y = 1 
    # print(a,end=" ")
    for y in range(1,n):
        # print(b,end=" ")
        if ((y+1) % 5 == 0):
            print(end="")
        z = y
        y = y+x
        x = z
    
for y in range(1,101):
    start = timeit.default_timer()
    deret_ajaib1(y)  
    end = timeit.default_timer()
    print("n=",y,"iteratif ->", end-start,"second")
print()

#rekursif
def deret_ajaib2(n):
    if n <= 1:
        return n
    else:
        return (deret_ajaib2(n-1)+deret_ajaib2(n-2))

for y in range(1,101):
    start = timeit.default_timer()
    deret_ajaib2(y)  
    end = timeit.default_timer()
    print("n=",y,"rekursif ->", end-start,"second")