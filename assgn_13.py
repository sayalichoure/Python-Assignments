#Calculate brokerage and net trade value
#A customer buys 100 units of a fund at NAV ₹112.50. Brokerage is 0.5% of trade value. 
# GST on brokerage is 18%. Calculate: trade value, brokerage amount, GST on brokerage, 
# total cost. Use round(x, 2) on all money values. Then assert total cost is greater than trade value.

# units = 100
# nav = 112.50
# Trade_value = float(units)* nav
# brokerage = round(Trade_value/0.5, 2)
# gst = brokerage/0.18
# print(round(Trade_value,2))
# print(round(brokerage,2))
# print(round(gst,2))
# assert gst > Trade_value

units = 100; nav = 112.50
brokerage_rate = 0.005; gst_rate = 0.18

trade_value = round(units * nav, 2)                       # 11250.0
brokerage = round(trade_value * brokerage_rate, 2)         # 56.25
gst = round(brokerage * gst_rate, 2)                       # 10.12
total_cost = round(trade_value + brokerage + gst, 2)      # 11316.37
assert total_cost > trade_value                            # passes

print('Trade Value:', trade_value)
print('Brokerage:', brokerage)  
print('GST on Brokerage:', gst)
print('Total Cost:', total_cost)

##hjkm;,l;.df