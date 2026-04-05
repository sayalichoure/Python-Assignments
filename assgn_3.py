#Write: A function called is_even It takes a number Returns True if even Returns False if odd
#Then: Call it with 4 Use assert to check that result is True Write code.

def is_even(b):
    return b % 2 == 0

result = is_even(5)
assert result == True
print (result)