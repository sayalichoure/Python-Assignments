# Step 1: Create a function: def multiply(a, b):
# Step 2: Return multiplication.
# Step 3: Call the function with 3 and 4.
# Step 4: Use assert to verify the result is 12.
# Write full code.

"""
def mult(a,b):
    c = a*b
    assert c == 15    
    print(c)
mult(3,5)
"""
#this was a conceptual code, now we create designed code

def mult(a,b):
    return a*b
result = mult(3,5)
assert result == 15
print(result)
