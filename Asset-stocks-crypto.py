# This program defines Asset and its derived classes Stock and Crypto for a financial application.

class Asset:
    def __init__(self, ticker, price, high, low, volume):
        # Initialize attributes of Asset
        self.ticker = ticker
        self.price = price
        self.high = high
        self.low = low
        self.volume = volume

    def basic_info(self):
        # Print basic information about the asset
        print(self.ticker, self.price, self.high, self.low, self.volume)

class Stock(Asset):
    def __init__(self, ticker, price, high, low, volume, open_p, close_p, earnings):
        # Initialize Stock attributes using super()
        super().__init__(ticker, price, high, low, volume)
        self.open_p = open_p
        self.close_p = close_p
        self.earnings = earnings
        self.rate_return = (self.close_p / self.open_p) - 1  # Calculate initial rate of return

    def update(self, open_p, close_p):
        # Update open and close prices and recalculate rate of return
        self.open_p = open_p
        self.close_p = close_p
        self.rate_return = (self.close_p / self.open_p) - 1

    def print_return(self):
        # Print the rate of return
        print("Rate of Return is", self.rate_return)

    def p_e_ratio(self):
        # Calculate and print the P/E ratio
        if self.earnings != 0:  # Avoid division by zero
            pe_ratio = self.close_p / self.earnings
            print("The P/E ratio is", pe_ratio)
        else:
            print("Earnings per share is zero, cannot calculate P/E ratio.")

    def info(self):
        # Print all information about the stock
        print(self.ticker, self.price, self.high, self.low, self.volume, self.open_p, self.close_p, self.earnings)

class Crypto(Asset):
    def __init__(self, ticker, price, high, low, volume, circulating_supply):
        # Initialize Crypto attributes using super()
        super().__init__(ticker, price, high, low, volume)
        self.circulating_supply = circulating_supply

    def info(self):
        # Print all information about the crypto
        print(self.ticker, self.price, self.high, self.low, self.volume, self.circulating_supply)

# Driver Code:
# Create the apple object from the Asset class:
apple = Asset('AAPL', 180.5, 200.3, 168.2, 68000000)
print(apple.ticker)     # This returns: AAPL
print(apple.price)      # This returns: 180.5
apple.basic_info()      # This prints: AAPL 180.5 200.3 168.2 68000000

# Create the apple2 object from the Stock class:
apple2 = Stock(apple.ticker, apple.price, apple.high, apple.low, apple.volume, 190.3, 195.4, 6.7)
apple2.info()           # This prints: AAPL 180.5 200.3 168.2 68000000 190.3 195.4 6.7
# Call the basic_info() method of the Asset class even though apple2 is a Stock object:
apple2.basic_info()     # This prints: AAPL 180.5 200.3 168.2 68000000

apple2.update(188.8, 198.0)
apple2.print_return()   # This prints: Rate of Return is 0.048728813559322015

apple2.p_e_ratio()      # This prints: The P/E ratio is 29.55223880597015

# Create the bitcoin object from the Asset class:
bitcoin = Asset('BTC', 21548.59, 22534.78, 19879.34, 11700000000)
print(bitcoin.ticker)   # This returns: BTC
print(bitcoin.high)     # This returns: 22534.78
bitcoin.basic_info()    # This prints: BTC 21548.59 22534.78 19879.34 11700000000

# Create the bitcoin2 object from the Crypto class:
bitcoin2 = Crypto(bitcoin.ticker, bitcoin.price, bitcoin.high, bitcoin.low, bitcoin.volume, 19100000)
bitcoin2.info()         # This prints: BTC 21548.59 22534.78 19879.34 11700000000 19100000
# Call the basic_info() method of the Asset class even though bitcoin2 is a Crypto object:
bitcoin2.basic_info()   # This prints: BTC 21548.59 22534.78 19879.34 11700000000
