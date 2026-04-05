#PAN format: always 10 characters, first 5 uppercase letters, next 4
#  digits, last 1 uppercase letter. Given pan = "ABCDE1234F" — use len(), .isupper(), 
# .isdigit() and logical operators to check: (a) length is 10, (b) first 5 chars are all alpha, 
# (c) middle 4 are digits. Print each check as a bool.


# Given_pan = "ABCDE1234F"
# is_length = str.__len__(Given_pan)
# bool_check = is_length == 10
# print(bool_check)
# print('The length is:',is_length, 'characters')

# is_upper = str.upper(Given_pan)
# bool_check_upper = is_upper == Given_pan
# print(bool_check_upper)
# print('The uppercase is', is_upper)

# is_digit = Given_pan[5:8]
# bool_check_Digit = is_digit == Given_pan[5:8]
# print(bool_check_Digit)
# print('The Digit format is', bool_check_Digit)

Given_pan = "ABCDE1234F"

is_len_pan = len(Given_pan) == 10

is_upper_pan = Given_pan[:5].isalpha()
is_digit_pan = Given_pan[5:9].isdigit()

is_valid = is_len_pan and is_upper_pan and is_digit_pan
print('Is the PAN Valid?', is_valid)