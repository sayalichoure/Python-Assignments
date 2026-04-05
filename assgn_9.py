#You have an integer order ID order_id = 90241. Selenium needs it as a 
# string inside an XPath. Build this XPath:
#//tr[@data-order-id='90241'] using str() conversion and an f-string. Print the result and print its type.

order_id = 90241

xpath = f'//tr[@data-order-id="{str(order_id)}"]'
print(xpath)
print(type(xpath))