def answer(n):
    # your code here
    base = 2
    
    while base < n:
        convertedNum = baseify(n, base)
        if is_palidrome(convertedNum, base)
            return base
        base += 1
        
    
def baseify(n, base):
    # takes an integer n and a base and returns a string representation
    # of n in the base provided
    baseValues = '0123456789ABCDEF'
    if n < base:
        return baseValues[n]
    else:
        return baseify(n//base, base) + baseValues[n%base]
    
    
    
def is_palindrome(value, base):
    result = False
    reverse_str = value[::-1]
    
    if value == reverse_str
        result = True
        
    return result
