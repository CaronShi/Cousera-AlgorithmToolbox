import sys

def main ():

    # better input method in terminal
    # example: echo 3 32 33 34  | python3 test2.py
    # manual input: ctrl+d for EOF
    args = sys.stdin.read () # example: "3 32 33\n 34\n\nEOF"
    args = args.split ()     # example: ['3', '32', '33', '34']
    n = args [0]             # example:  ^
    digits = args [1: ]      # example:     ^^^^^^^^^^

    # dictionary of {digit: count}
    digit_count = {}
    for digit in digits: # iterate through e.g., ['32', '33', '34']
        if digit not in digit_count: 
            digit_count [digit] = 1     # new item {'32': 1}
            # digit_count [digit] outputs the value, [digit] is the key
        else: digit_count [digit] += 1  # old item {'32': 2}
            
    # extract max digit and then append to output
    result = ''
    while len (digit_count) > 0:
        max_digit = '0'
        for digit in digit_count: # iterate through e.g., ['32', '33', '34']
            if is_greater (digit, max_digit):
                max_digit = digit
        # if we have two 32s, then result += '32'+'32'
        # result = '' 
        # result = ''+'32'+'32' = '3232'
        result += max_digit * digit_count [max_digit] 
        del digit_count [max_digit]     # O(1)

    print (result)



def is_greater (a, b):
    # test ASCII code
    # test empty string
    if len (a) == 0: return False
    if len (b) == 0: return True
    # a: 51, b: 513, result: 51513 (a+b)
    # a: 51, b: 515, result: 51551 (b+a)
    # a: 51, b: 516, result: 51651 (b+a)
    length = max (len (a), len (b)) # length = 3
    for i in range (0, length):     # iterate: 0, 1, 2
        if len (a) < i+1:
            if b [i] > a [0]: return False
            if b [i] < a [0]: return True
            else: return False # b [i] == a[0]
        if len (b) < i+1:             
            if a [i] > b [0]: return True
            if a [i] < b [0]: return False
            else: return True # a [i] == b[0]
        if a [i] > b [i]: return True
        if a [i] < b [i]: return False



if __name__ == '__main__': main ()

