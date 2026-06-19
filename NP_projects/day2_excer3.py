def calculate_nav(fund_value, total_units):
    try :
        NAV = float(fund_value)/float(total_units)
        return NAV
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except ValueError:
        return "Invalid input"
print(calculate_nav(5000000, 100000))  # Expected: 50.0
print(calculate_nav(5000000, 0))       # Expected: "Cannot divide by zero"
print(calculate_nav("abc", 100))       # Expected: "Invalid input"