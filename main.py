# bot.py in the course...

# import needed libraries
import sys

from traderlib import *
from mylogger import *



# initialize API/account
#   - check account credentials and ability to log in
def initialize_account_connection():
    """Initialize Alpaca API account connection and get account information"""
    try:
        # get account information
    except Exception as e:
        logging.error("Could not get account information.")
        logging.error(str(e))
        sys.exit()

# clean/close our current orders (modify to account for overnight orders)
def clean_open_orders():
    """Close any open orders on the account"""
    # Get list of open orders
    open_orders = [] # TODO Get actual list of open orders
    logging.info("List of open orders:")
    logging.info(str(open_orders))

    for order in open_orders:
        # Close the order
        logging.info(f"Order {order.id} closed.")

    logging.info("All open orders closed.")

# get the list of assets (start with one...)
# TODO: implement a real list of tickers/assets
def get_ticker():
    return input("Write the ticker you want to operate with: ")

if __name__ == "__main__":
    # initialize the logger
    initialize_logger()

    #intialize the connection to ALPACA platform
    initialize_account_connection()

    #clean/close open orders remaining
    clean_open_orders()

    #get asset
    ticker = get_ticker()

    #execute the trading bot with ticker
    alpaca_bot = AlpacaTrader(ticker)
    alpaca_bot.run()
