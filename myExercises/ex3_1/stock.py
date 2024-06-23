import csv

class Stock:

    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self) -> float:
        return self.shares * self.price
    
    def sell(self, nshares: int) -> None:
        self.shares -= nshares
        
def read_portfolio(filename: str) -> list:
    list_of_stocks = []
    with open(filename) as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            stock = Stock(name = row[0], 
                          shares = int(row[1]),
                          price = float(row[2]))
            
            list_of_stocks.append(stock)
    return list_of_stocks

def print_portfolio(portfolio = list) -> None:
    print('       name      shares    price')
    print('  ---------    ---------   ---------')
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))
        
            
list_of_stocks = read_portfolio('../../Data/portfolio.csv')
print_portfolio(list_of_stocks)