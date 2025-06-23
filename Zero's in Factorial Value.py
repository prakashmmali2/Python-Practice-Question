def facto(n):
    fact = 1
    
    for i in range(1,n+1):
        fact *= i
    return fact
    
def count_zero(fact):
    fact = facto(n)
    
    count = 0
    
    while fact % 10 == 0:
        count += 1
        fact //= 10
    
    return count
    
n = int(input("Enter the Number: "))
print(f"Total Number of Zero's in {n} Factorial Value :",count_zero(n))

        
    