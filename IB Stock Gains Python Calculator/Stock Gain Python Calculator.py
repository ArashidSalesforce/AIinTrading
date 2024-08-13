# cd C:\Users\tripl\28ProjectFolder\source\pythonclient\ibapi\Inner
# python3 GainsCalc.py
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

inivalue = 25000
almoinivalue= 100000.00

# use of range() to define a range of values
values = range(30*16)

Day = 1

# iterate from i = 0 to i = 3
for i in values:
  #print("Starting Initial Value: ")
  #print (inivalue)
  valuestwo = range(60*6)
    # iterate from i = 0 to i = 3
  inivalue = inivalue*4.00
  marginminus = inivalue*0.75
  for itwo in valuestwo:
    #print("Order Began :")
    #print(inivalue)
    inivalue = (inivalue*1.0001) - ( (0.0066*(inivalue/185.00)) +  (0.005*(inivalue/185.00)) ) 
    #print("Order Change :")
    #print(inivalue)
  #print("EOD Initial Value: ")
  #print(inivalue)
  #print("EOD Initial Value - Margin: ")
  inivalue = inivalue - marginminus
  #print(inivalue)
  Day = Day+1
  
if Day > (30*16):
  print("16 Month")
  print(inivalue)  