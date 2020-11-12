def NonFib(n):
    current=3     
    p=2
    q=1

    while n>0:
        q=p
        p=current
        current=p+q   

        n=n-(current-p-1)

    n=n+(current-p-1)             

    return (n+p)


n=int(input("Enter range for generating Non-fibonacci numbers : "))
res=NonFib(n)
print("The number of non-fibonacci numbers are " + str(res))







