#Monthly SIP = ₹5000, duration = 24 months, assumed return rate = 12% per year 
# (1% per month). Calculate total invested and use the modulus operator to check 
# if duration is exactly divisible by 12 (i.e., a whole number of years). Print both.

MonthlySIP = 5000
duration = 24
ROI = 12.00
total_invested = MonthlySIP * duration
print('The total investment is of Rs:',total_invested)
if duration %2 == 0:
    print('Duration is divisible by 12 i.e', duration)
else:
    print('It is not divisible by 12')

# without using conditional statements:
# MonthlySIP = 5000
# duration = 24
# ROI = 12.00
# total_invested = MonthlySIP * duration
# is_full_year = duration % 2 == 0
# print('The total investment is of Rs:',total_invested)
# print('Duration is divisible by 12 i.e',is_full_year)