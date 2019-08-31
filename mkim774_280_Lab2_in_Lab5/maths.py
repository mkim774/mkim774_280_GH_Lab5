def add(first, second, optionalBase=None):
    if optionalBase == None:
        return first + second
    return convert_base(first + second, optionalBase)

def fibonacci(length):
    def internal(first, second, count):
        third = add(first, second)
        count -= 1
        if count == 0:
            return second       # Fibonacci sequence starts from the "0th" term. So for instance, if input count was 1,
                                # it should return the "1th" term in sequence, and hence after the count -= 1 happens and
                                # count becomes 0, the "1th" term should be returned which corresponds to the "second"
                                # variable. The same mechanism carries over to higher values of input "count".
                                # If for input count = 1, we returned the "third" variable, then this would be returning
                                # the "2th" term in the sequence instead of the "1th" term, so the returned value will be wrong. 
        else:
            return internal(second, third, count)

    return internal(0, 1, length)

HEX_CHARS = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}

def convert_base(num, n):
    """Change a base 10 number to a base-n number. Supports up to base 16. """
    new_num_string = ''
    current = num
    while current != 0:
        remainder = current % n
        if remainder > 9:
            remainder_string = HEX_CHARS[remainder]
        elif remainder >= 36:
            remainder_string = '('+str(remainder)+')'
        else:
            remainder_string = str(remainder)
        new_num_string = remainder_string+new_num_string
        current = current//n
    return new_num_string

def factorial(number):
    ''' Computes the Factorial of a Number. '''
    fact_result = 1
    for i in range(1, number+1):
        fact_result = fact_result * i
    return fact_result