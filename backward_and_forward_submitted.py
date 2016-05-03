def answer(n):
    base = 2
    
    while base < n:
        convertedNum = baseify(n, base)
        
        if is_palindrome(convertedNum):
            #print "(" + convertedNum + ")",
            return base
        base += 1
    return 2
        
    
def baseify(n, base):
    # takes an integer n and a base and returns a string representation
    # of n in the base provided
    baseValues = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if n < base:
        return baseValues[n]
    else:
        return baseify(n//base, base) + baseValues[n%base]
    
    
    
def is_palindrome(value):
    return value == value[::-1]
