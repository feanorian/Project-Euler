def is_palindrome(num):
    return str(num) == str(num)[::-1]

def palindrome( ):
    for x in range( 100, 999 ):
        for y in range( 600, 999 ):
            if is_palindrome( x * y ):
                sup_palindrome = x * y
    return sup_palindrome