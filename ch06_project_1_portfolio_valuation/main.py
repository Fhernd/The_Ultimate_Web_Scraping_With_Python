from dataclasses import dataclass

from bs4 import BeautifulSoup
import requests as r
from tabulate import tabulate


@dataclass
class Stock:
    ticker: str
    exchange: str
    price: float = 0
    currency: str = "USD"
    usd_price: float = 0

    def __post_init__(self):
        price_info = get_price_information(self.ticker, self.exchange)

        if price_info['ticker'] == self.ticker:
            self.price = price_info['price']
            self.currency = price_info['currency']
            self.usd_price = price_info['usd_price']

@dataclass
class Position:
    stock: Stock
    quantity: int

@dataclass
class Portfolio:
    positions: list[Position]

    def get_total_value(self):
        total_value = 0
        for position in self.positions:
            total_value += position.stock.usd_price * position.quantity
        return total_value


def get_fx_to_usd(currency):
    """
    Get the exchange rate of a currency to USD.

    Parameters:
    currency (str): The currency to convert to USD.

    Returns:
    float: The exchange rate of the currency to USD.
    """
    url = f"https://www.google.com/finance/quote/{currency}-USD"
    response = r.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    fx_rate = soup.find("div", attrs={"data-last-price": True})

    return float(fx_rate['data-last-price'])


def get_price_information(ticker, exchange):
    """
    Get the price information of a stock from Yahoo Finance.

    Parameters:
    ticker (str): The ticker of the stock.
    exchange (str): The exchange of the stock.

    Returns:
    dict: A dictionary containing the ticker, exchange, price, and currency of the stock.
    """
    url = f"https://www.google.com/finance/quote/{ticker}:{exchange}"
    response = r.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    price_div = soup.find("div", attrs={"data-last-price": True})
    price = float(price_div['data-last-price'])
    currency = price_div['data-currency-code']

    usd_price = price
    if currency != 'USD':
        fx = get_fx_to_usd(currency)
        usd_price = round(price * fx, 2)

    return {
        'ticker': ticker,
        'exchange': exchange,
        "price": price,
        "currency": currency,
        'usd_price': usd_price,
    }


def display_portfolio_summary(portfolio):
    """
    Display a summary of the portfolio.

    Parameters:
    portfolio (Portfolio): The portfolio to display.
    """
    if not isinstance(portfolio, Portfolio):
        raise ValueError("The portfolio must be an instance of Portfolio.")
    
    portfolio_value = portfolio.get_total_value()

    position_data = []
    
    for position in sorted(portfolio.positions, key=lambda x: x.quantity * x.stock.usd_price, reverse=True):
        position_data.append([
            position.stock.ticker,
            position.stock.exchange,
            position.quantity,
            position.stock.usd_price,
            position.stock.price,
            position.quantity * position.stock.usd_price,
            position.quantity * position.stock.usd_price / portfolio_value * 100,
        ])

    print(tabulate(position_data, headers=[
        "Ticker", "Exchange", "Quantity", "USD Price", "Price", "Value", "% of Allocation"
    ], tablefmt='psql', floatfmt=".2f"))

    print("\nTotal Portfolio Value: ${:.2f}".format(portfolio_value))


def main():
    apple = Stock("AAPL", "NASDAQ")
    msft = Stock("MSFT", "NASDAQ")
    google = Stock("GOOGL", "NASDAQ")

    portfolio = Portfolio([
        Position(apple, 10),
        Position(msft, 20),
        Position(google, 5),
    ])

    display_portfolio_summary(portfolio)


if __name__ == "__main__":
    main()
