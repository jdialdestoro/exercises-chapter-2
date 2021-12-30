def isprime(n):
    """Returns True or False depending on whether n is prime"""
    from math import sqrt

    if n==1:
        return False
    
    else:
        for i in range(2,int(sqrt(n))):
            if n % i == 0:
                return False
    return True
