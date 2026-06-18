def calculate_sip(monthly_amount, months, return_rate):
    if  months == 0:
        return 0.0
    total_value = float(monthly_amount) * float(months) * (1 + float(return_rate) / 100)
    return round(total_value,2)
print(calculate_sip(50890, 12, 12))   # Expected: 67200.0
print(calculate_sip(5000, 0, 12))    # Expected: 0
print(calculate_sip(10000, 24, 8))   # Expected: 259200.0
