from bs4 import BeautifulSoup
import requests as r


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

    return {
        'ticker': ticker,
        'exchange': exchange,
        "price": price,
        "currency": currency
    }


def main():
    price = get_price_information("AAPL", "NASDAQ")
    
    fx_rate = get_fx_to_usd('COP')
    print('fx_rate:', fx_rate)


if __name__ == "__main__":
    main()
