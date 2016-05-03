import sys


def answer(n):
    # your code here
    base = 2
    
    while base < n:
        convertedNum = baseify(n, base)
        
        if is_palindrome(convertedNum, base):
            print "(" + convertedNum + ")",
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
    
    
    
def is_palindrome(value, base):
    result = False
    reverse_str = value[::-1]
    
    if value == reverse_str:
        result = True
        
    return result



if __name__ == "__main__":
    test_nums = [0, 42, 939, 554]
    i = 1

    while i <= 42:
        print str(i) + " is a palindrome in base " + str(answer(i)) + "."
        i += 1
    #for num in test_nums:
        #print str(num) + " is a palindrome in base " + str(answer(num)) + "."
