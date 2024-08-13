# cd C:\Users\tripl\28ProjectFolder\source\pythonclient\ibapi\Inner
# python3 Loop3.py
# REMEMBER TO CHANGE PERCENT OF POSSIBLESHARES

#from ibapi.wrapper import *
#import wrapper
from wrapper import EWrapper
#from ibapi.client import *
#import client
from client import EClient
#from ibapi.contract import *
#import contract 
from contract import Contract
#from ibapi.order import *
#from contract import ComboLeg
#import order
from order import Order
from ticktype import TickTypeEnum
#from order import Execution
#from order import TickerId
#from threading import Thread
import queue
import logging
#import datetime
import time
import math
#from bs4 import BeautifulSoup
#import requests
#from random import randint
#from threading import Thread
from threading import Thread
#import TagValue
import smtplib, ssl
#import email.message
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


while True:
    try:
        
        #LVHI
        #LVHD

        #EYLD
        #FYLD

        ##GAA
        ##GMOM
        ##VAMO
        ##HTUS

        ###US

        sym = 'SPY'
        exch = 'SMART'
        cur= 'USD'
        availableFunds = 0
        buyingPower = 0
        pri = 1.00
        sellpri = 1.00
        #quan = buyingPower/price
        #quan = math.ceil(5000/146.71)
        quan = 10
        #market_price = float
        #marketpri = float

        reqId = ''
        account = ''
        tag = ''
        value = ''
        currency = ''

        class TestWrapper(EWrapper):

            def __init__(self):
                self.data = {}
                self.reqID = None
                self.positions = {}
            
            #def updateMktData(self, reqId, price):
                # Update the price data when market data is received
                #self.data[reqId] = price
            
            #def tickPrice(self, reqId, tickType, price, attrib):
                #if tickType == TickTypeEnum.LAST:
                    #print(f"Last price: {price}")

            # error handling methods
            def init_error(self): 
                error_queue = queue.Queue() 
                self.my_errors_queue = error_queue

            def is_error(self): 
                error_exist = not self.my_errors_queue.empty() 
                print ("Line 81, Errors: ") 
                print(error_exist)
                return error_exist
            
            #ABDUL COMMENT, INCREASE TIMEOUT IF NEEDED
            print ("Line 86: ABDUL COMMENT, INCREASE TIMEOUT IF NEEDED")
            def get_error(self, timeout=6): 
                if self.is_error(): 
                    try: 
                        return self.my_errors_queue.get(timeout=timeout) 
                    except queue.Empty: 
                        return None
                return None
            
            #def error(self, id, errorCode, errorString): 
                ## Overrides the native method
                #errormessage = "IB returns an error with %d errorcode %d that says %s" % (id, errorCode, errorString) 
                #self.my_errors_queue.put(errormessage) 

            # time handling methods
            def init_time(self): 
                time_queue = queue.Queue() 
                self.my_time_queue = time_queue 
                return time_queue
            
            def currentTime(self, server_time): 
                ## Overriden method
                self.my_time_queue.put(server_time) 
            
            # ID handling methods
            def nextValidId(self, orderId: int): 
                super().nextValidId(orderId) 
                logging.debug("Line 113: setting nextValidOrderId: %d", orderId) 
                self.nextValidOrderId = orderId 
            
            def nextOrderId(self): 
                oid = self.nextValidOrderId 
                self.nextValidOrderId += 1
                return oid 
            
            # Account details handling methods
            def accountSummary(self, reqId: int, account: str, tag: str, value: str, currency:str): 
                super().accountSummary(reqId, account, tag, value, currency) 
                print("Line 124: Acct Summary. ReqId:", reqId, "Acct:", account, "Tag: ", tag, "Value:", value, "Currency:", currency)
                if tag == "AvailableFunds": 
                    global availableFunds 
                    availableFunds = value 
                if tag == "BuyingPower": 
                    global buyingPower 
                    buyingPower = value
                    #buyPower = buyingPower
                return buyingPower
            
            def accountSummaryEnd(self, reqId: int): 
                super().accountSummaryEnd(reqId) 
                print("Line 136: AccountSummaryEnd. Req Id: ", reqId) 

        '''Here we will call our own methods, not overriding the api methods'''
        class TestClient(EClient): 
            def __init__(self, wrapper): 
            ## Set up with a wrapper inside
                EClient.__init__(self, wrapper)
                print ("Line 143: Function has run")
            
            def server_clock(self): 
                print("Line 146: Asking server for Unix time") 
                
                # Creates a queue to store the time
                time_storage = self.wrapper.init_time() 
                
                # Sets up a request for unix time from the Eclient
                self.reqCurrentTime()

                #Specifies a max wait time if there is no connection
                max_wait_time = 10
                
                try: 
                    requested_time = time_storage.get(timeout = max_wait_time) 
                except queue.Empty: 
                    print("Line 160: The queue was empty or max time reached") 
                    requested_time = None
                
                while self.wrapper.is_error(): 
                    print("Line 164: Error:") 
                    print(self.get_error(timeout=5)) 
        
                return requested_time

            def account_update(self): 
                self.reqAccountSummary(9001, "All", "TotalCashValue, BuyingPower, AvailableFunds")

        # Below is TestApp Class 
        class TestApp(TestWrapper, TestClient):     
            #Intializes our main classes 
            def __init__(self, ipaddress, portid, clientid): 
                TestWrapper.__init__(self) 
                TestClient.__init__(self, wrapper=self) 

                #Connects to the server with the ipaddress, portid, and clientId specified in the program execution area
                self.connect(ipaddress, portid, clientid) 
        
                #Initializes the threading
                thread = Thread(target = self.run) 
                thread.start() 
                setattr(self, "_thread", thread) 

                # Initialize the request ID
                self.reqID = 0
        
                #Starts listening for errors 
                self.init_error()
                
            

            def create_sell_order(self, contract):
                #market_data = app.request_market_data(contract)
                #quan
                #print("Line 198: ")
                #print(market_data)
                #price = market_data["price"]
                # Gets the current market price of the contract
                #self.reqMktData(1, contract, "", False, False, [])
                #market_price = str(price)
                

                #quan = qua
                #print("line 207: see quantity, buyingPower, and pri (which is price) below")
                #print(quan)
                #print(buyingPower)
                #print(pri)
                market_price = pri
                #print("Line 212: see market_price below")
                #print(market_price)
                #print("Line 214: see quantity below")
                #print(quan)
                #market_price = price

                # Calculates the limit price at 1.001% higher than the market price
                limit_price = math.ceil(market_price * 1.0001 * 100) / 100
                #limit_price = market_price * 1.001

                # Creates a new sell order with the limit price and order quantity of 1
                order = Order()
                order.action = "SELL"
                order.orderType = "LMT"
                order.totalQuantity = qua
                order.lmtPrice = limit_price
                order.orderId = self.nextOrderId()
                order.transmit = True # We set this to False to prevent immediate execution
                order.outsideRth = True
                

                # Define the parameters for not allowing a short sale
                #order.algoStrategy = "Adaptive"
                #order.sweepToFill = True
                    
                time.sleep(1)    
                # Sends the sell order to the API
                self.placeOrder(order.orderId, contract, order)
                #time.sleep(1)
                #self.cancelOrder(order.orderId, "")
                #limit_price = math.ceil(market_price * 1 * 100) / 100
                #order.lmtPrice = limit_price
                #order.orderId = self.nextOrderId()
                #self.placeOrder(order.orderId, contract, order)
                time.sleep(30)
            
            def tickPrice(self, reqId, tickType, price, attrib):
                global pri
                super().tickPrice(reqId, tickType, price, attrib)
                if tickType == 2: 
                #tickType == 4:
                    #time.sleep(3)
                    pri = price
                print("Line 270: The current ask price is: ", price)
                print("Line 271: The current ask pri is: ", pri)
                #app.disconnect()
                #print("Line 256: see price below")
                
                #pri = price
                #print (price)

                
                #print("Line 262: see buyingPower and quantity below")
                #print(quan)
                #print(buyingPower)
                #quan = math.ceil(float(buyingPower))/price
                #print(quan)
                #print(pri)

                #app.disconnect()

                return pri
            
            def selltickPrice(self, reqId, tickType, sellprice, attrib):
                global sellpri
                super().tickPrice(reqId, tickType, sellprice, attrib)
                if tickType == 1: 
                #tickType == 4:
                    #time.sleep(3)
                    sellpri = sellprice
                print("Line 297: The current ask price is: ", sellprice)
                print("Line 298: The current ask pri is: ", sellpri)
                
                return sellpri

                #self.market_price = price
            
            # Override the orderStatus() method to check for errors and transmit the order

        #app = TestApp("127.0.0.1", 7497, 0) 

        #Below is the program execution
        if __name__ == '__main__': 
                
        #print("Line 116: before start") 
                
        # Specifies that we are on local host with port 7497 (paper trading port number)
        #Specifies that we are on local host with port 7496 (real trading port number)

            app = TestApp("127.0.0.1", 7496, 999) 
                
        # A printout to show the program began
        print("Line 291: The program has begun") 
                
        #assigning the return from our clock method to a variable 
        requested_time = app.server_clock() 

        #printing the return from the server
        print("Line 297: This is the current time from the server " ) 
        print(requested_time)

        def quantityCalc():

            #global possibleShares
            global qua

            # View teh buying power and price of stock 
            print("Line 306: Available Funds: " + str(availableFunds)) 
            print("Line 307: Stock Price: " + str(pri))

            # Divide the buying power by price of the share 
            possibleShares = math.ceil(float(availableFunds)) / math.ceil(pri)

            

            # Weight the value to be 1 percent of our buying power (this is an easy value to use for testing)
            quan = math.floor(possibleShares * 1)
            #quan = 170
            qua = quan
            #quan = 70
            #print("Line 315: ")
            #print(quan)
            if quan < (20000/pri):
            #if quan > 0:
                print("Line 321: port updated below ")
                #smtpObj = smtplib.SMTP( [host [, port]] ) password = "PyIB3471)"
                port = 465  # For SSL
                print("Line 324: password updated below")
                password = 'jpbzgeguaimnusfa'

                print("Line 327: context updated below ")
                # Create a secure SSL context
                context = ssl.create_default_context()
                print("Line 331: See context below")
                print(context)
                with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                    server.login("ibpy3471@gmail.com", password)
                    #Send email here
                port = 465  # For SSL
                smtp_server = "smtp.gmail.com"
                sender_email = "ibpy3471@gmail.com"  # Enter your address
                receiver_email = "ibpy3471@gmail.com"  # Enter receiver address
                password = 'jpbzgeguaimnusfa'
                message = """\
                Subject: Hi there

                This message is sent from Python."""

                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message)
                                
                message = MIMEMultipart()
                message['Subject'] = 'Test email'
                message['From'] = sender_email
                message['To'] = receiver_email
                text = "This is a test email sent using Python."
                part = MIMEText(text, "plain")
                message.attach(part)

                context = ssl.create_default_context()
                print("Line 361: see smtp_server, port, contect, sender_email, password, receiver_email, message.as_string() below")
                print(smtp_server)
                print(port)
                print(context)
                print(sender_email)
                print(password)
                print(receiver_email)
                print(message.as_string())

                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message.as_string())
                                                
                time.sleep(21600)
                exit()
                quit()
                sys.exit()

            return quan  # return the shares to buy so we can use it in orderExecution 

        #def newBP():
            
            #global newBuyingPower

            #newBuyingPower = math.ceil(float(buyingPower)) - (possibleShares * math.ceil(pri))

            #return newBuyingPower

        @staticmethod 
        def contractCreate(): 
            #! [stkcontract]
            # Fills out the contract object
            contract = Contract() 
            contract.symbol = sym
            contract.secType = "STK"
            contract.currency = cur
            # In the API side, NASDAQ is always defined as ISLAND in the exchange field
            contract.exchange = exch
            # contract1.PrimaryExch = "NYSE"
            #! [stkcontract]
            return contract

        #@staticmethod 
        #def MarketOrder(): 
            #! [market] 
            #order = Order() 
            #order.action = "BUY"
            #order.orderType = "MKT"
            #order.totalQuantity = 10
            #! [market]
            #return order

        def orderCreate(): 
            # Fills out the order object 
            order1 = Order() # Creates an order object from the import 
            order1.action = "BUY" # Sets the order action to buy
            order1.orderType = "LMT" # Sets order type to market buy
            order1.transmit = True 
            order1.totalQuantity = quan # Setting a static quantity of 10
            #limit_price = math.floor(pri * 0.99985 * 100) / 100
            order1.lmtPrice = pri
            order1.outsideRth = True
            #order1.algoStrategy = "Adaptive"
            #order1.sweepToFill = True
            #print("Line 422: Buy order about to be placed. See pri (which is price) and limit price for sell")
            #print(pri)
            #print(order1.lmtPrice)

            #print("Line 426: see pri (which is price) below")
            #print(pri)
            return order1 # Returns the order object

        def orderExecution(): 

            quan = quantityCalc()
            #quantityOfTrade = quantityCalc()
            
            #print("Line 435: see quantity of stocks to buy and sell below")
            #print(quan)
            # Places the order with the returned contract and order objects
            contractObject = contractCreate() 
            orderObject = orderCreate() 
            nextID = app.nextOrderId() 
            #nextID = 101

            orderObject.totalQuantity = quan
            
            #print("Line 445: See buyingPower and pri (which is price) below")
            #print(buyingPower)
            #print(pri)
            
            #print("Line 449: See Order Id and Account Data Below")
            #print(app.reqMarketDataType(4))
            # Print statement to confirm correct values 
            print("Line 452: The next valid id is - " + str(nextID))
            print("Line 453: Buying Power: " + str(buyingPower)) 
            print("Line 454: Available Funds: "+ str(availableFunds)) 

            #print("Line 456: Buy order about to be placed. See pri (which is price) and limit price for sell")
            #print(pri)
            #print(orderObject.lmtPrice)

            # Place order 
            app.placeOrder(nextID, contractObject, orderObject) 
            #time.sleep(2)
            #wrapper.positions
            #contract = app.contractCreate()
            app.create_sell_order(contractObject)
            #print("Line 466: Sell order is placed") 

            #return quan

        contractObject = contractCreate() 
        app.account_update()
        app.reqMarketDataType(1)
        app.reqMktData(1, contractObject, "", 1, False, [])
        #global qua
        #quan = math.ceil(buyingPower/pri)
        #print("Line 476: Right before app.tickPrice")
        #print(qua)
        price = 1.00
        sellprice = 1.00
        app.tickPrice(reqId = 1, tickType = 2, price = any, attrib = True)
        app.selltickPrice(reqId = 2, tickType = 1, sellprice = any, attrib = True)
        print(price)
        print(sellprice)
        #print("Line 481: Right before orderExecution")

        #quan = buyingPower/price
        time.sleep(1) # Wait three seconds to gather initial information 
        orderExecution()


        # Optional disconnect. If keeping an open connection to the input don't disconnet
        app.disconnect()

    except:
        continue
