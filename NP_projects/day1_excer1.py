# def validate_pan(pan):
# 	if len(pan) == 10:
# 		return True
# 	if pan[0:5].isalpha():
# 		return True
# 	if pan[6:8].isdigit():
# 		return True
# 	if pan[9].isalpha():
# 		return True
# 	else:
# 		print("invalid pan")
# 	return False

# print(validate_pan('CSOPH56789'))

def validate_pan(pan):
    if len(pan) != 10:
        return False
    if not pan[0:5].isalpha():
        return False
    if not pan[5:9].isdigit():
        return False
    if not pan[9].isalpha():
        return False
    return True

print(validate_pan('CSOPC5866H'))   # True  — valid format
print(validate_pan('CSOPC58661'))   # False — last char is digit
print(validate_pan('12345ABCDE'))   # False — first 5 are digits
print(validate_pan('CSOP5866H'))    # False — only 9 characters