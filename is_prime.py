def is_prime(x):    
    if x < 2: 
        return False  
    else:
        for n in range(2,x):
            if x % n == 0: 
                return False
        else:
            return True

def factorial(x): 
    while x != 0: 
        x = x * factorial(x-1)
    else:
        1 