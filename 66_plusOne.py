def plusOne(digits):
    # From right to left (n-1 -- 0), if 1 set to 0, if o set
    # to 1 return
    n = len(digits)
    for i in reversed(xrange(n)):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
    digits.append(0)
    digits[0] = 1
    return digits

S = [9,9,9]
print plusOne(S)
