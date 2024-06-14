from dataclasses import dataclass

from bs4 import BeautifulSoup
import requests as r


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


def main():
    apple = Stock("AAPL", "NASDAQ")
    msft = Stock("MSFT", "NASDAQ")
    google = Stock("GOOGL", "NASDAQ")

    portfolio = Portfolio([
        Position(apple, 10),
        Position(msft, 20),
        Position(google, 5),
    ])

    print(f"Total Portfolio Value: ${portfolio.get_total_value()}")


if __name__ == "__main__":
    main()
