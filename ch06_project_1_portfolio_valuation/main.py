from bs4 import BeautifulSoup
import requests as r


def get_price_information(ticker, exchange):
    """
    Get the price information of a stock from Yahoo Finance.

    Parameters:
    ticker (str): The ticker of the stock.
    exchange (str): The exchange of the stock.

    Returns:
    str: The price of the stock.
    """
    
    url = f"https://finance.yahoo.com/quote/{ticker}:{exchange}"
    response = r.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    price = soup.find("div", {"data-last-price": True})

    return price["data-last-price"]


def main():
    pass


if __name__ == "__main__":
    main()
