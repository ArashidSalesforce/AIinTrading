from client import EClient
from wrapper import EWrapper
from contract import Contract
from order import *

class InteractiveBrokerAPI(EWrapper, EClient):
    def __init__(self, host, port, client_id):
        EClient.__init__(self, self)
        self.connect(host, port, client_id)
        self.reqId = 0
        self.dollar_to_euro_ratio = 0.0
        self.position = 0
        
    def nextOrderId(self):
        oid = self.nextValidOrderId
        self.nextValidOrderId += 1
        return oid
        
    def historicalData(self, reqId, bar):
        if reqId == self.reqId:
            # Update dollar to euro ratio
            self.dollar_to_euro_ratio = bar.close
            
            # Check if we need to trade
            if self.position == 0 and self.dollar_to_euro_ratio < 1.0:
                # Buy euros
                self.placeOrder(self.nextOrderId(), self.createForexContract("EUR", "USD"), self.createOrder("BUY", 10000))
                self.position = 10000
            elif self.position > 0 and self.dollar_to_euro_ratio > 1.0:
                # Sell euros
                self.placeOrder(self.nextOrderId(), self.createForexContract("EUR", "USD"), self.createOrder("SELL", 10000))
                self.position = 0
                
    def createForexContract(self, symbol, currency):
        contract = Contract()
        contract.symbol = symbol
        contract.secType = "CASH"
        contract.currency = currency
        contract.exchange = "IDEALPRO"
        return contract
    
    def createOrder(self, action, quantity):
        order = Order()
        order.action = action
        order.orderType = "MKT"
        order.totalQuantity = quantity
        return order

    def start(self):
        self.reqHistoricalData(self.reqId, self.createForexContract("EUR", "USD"), "", "1 D", "1 hour", "MIDPOINT", 1, 1, False, [])
        self.run()