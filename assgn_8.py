#NAV scraped from the page is "52.30" (a string, as Selenium would give you). 
# Convert it to float. Then write a boolean check: is the NAV above 50? Store the
#  result in is_above_threshold and print both the value and its type.

Nav = '52.30'
nav_org = float(Nav)
is_above_threshold = nav_org > 50
print(type(is_above_threshold))
print('is the NAV above 50?', is_above_threshold)