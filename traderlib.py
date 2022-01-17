"""Trading Bot file"""
import logging
import sys
import time

import pandas as pd
import tulipy as ti


class AlpacaTrader:
    """Implements alpaca trading API and stochastic stock analysis to determine trade entry/exit points"""

    def __init__(self, ticker):
        self.ticker = ticker
        logging.info(f"Trader initialized with {self.ticker}")

    def is_tradeable(self, ticker):
        """Check if the assset is trade-able
           INPUT: asset (ticker)
           OUTPUT: True/False (position is trade-able/not trade-able)"""

        try:
            # get asset from alpaca wrapper
            if not asset.tradeable:
                logging.info(f"{ticker} is not trade-able.")
                return False
            else:
                logging.info(f"{ticker} is trade-able.")
                return True
        except Exception as e:
            logging.error(f"{ticker} is not retrievable from the API.")
            logging.info(e)

    def set_stop_loss(self, entry_price, direction):
        """Determine the stop loss value based on stop loss margin in global variables
           INPUT: entry price, direction (long/short)
           OUTPUT: stop loss price"""

        stop_loss_margin = 0.05  # TODO change to global variables
        direction = direction.lower()
        try:
            if direction == "long":
                return entry_price - (entry_price * stop_loss_margin)
            elif direction == "short":
                return entry_price + (entry_price * stop_loss_margin)
            else:
                raise ValueError

        except Exception as e:
            logging.error(f"Error in set_stop_loss: direction is neither 'long' or 'short'. {direction}")
            logging.error(e)
            sys.exit()

    def set_take_profit(self, entry_price, direction):
        """Determine the take profit based on take profit margin in global variables
            INPUT: entry price
            OUTPUT: sets the take profit"""

        take_profit_margin = 0.1  # TODO change to global variables
        direction = direction.lower()
        try:
            if direction == "long":
                return entry_price + (entry_price * take_profit_margin)
            elif direction == "short":
                return entry_price - (entry_price * take_profit_margin)
            else:
                raise ValueError

        except Exception as e:
            logging.error(f"Error in set_stop_loss: direction is neither 'long' or 'short'. {direction}")
            logging.error(e)
            sys.exit()

    # Load historical stock data
    #   IN: ticker, interval, entries limit
    #   OUT: list with stock data OHCL
    def get_open_positions(self, assetID):
        """Get open position
            IN: assetID
            OUT: True/False (already open position vs not open)"""

        # ask alpaca wrapper for list of positions
        positions = []
        for position in positions:
            if position.symbol == assetID:
                return True
        return False

    # Submit Order, ensure order gets through API or logs error
    #   IN: order data
    #   OUT: True/False (order succeeded, order failed)

    # Cancel Order, cancels an active order
    #   IN: order data (id)
    #   OUT: True/False (cancel succeeded, cancel failed)

    def check_position(self, ticker):
        """Check position, check whether the position is open or not
            IN: ticker
            OUT: True/False (position is open/not open (not exist)"""
        max_attempts = 5
        attempts = 0

        while attempts < max_attempts:
            try:
                # position = ask alpaca wrapper based on ticker TODO get position with alpaca wrapper
                # current_price = position.current_price
                logging.info(f"Position was checked, current price is {current_price}")
                return True
            except Exception as e:
                # Wait 5s and try
                attempts += 1
                logging.info(f"Position was not found for {ticker}, waiting 5s")
                time.sleep(5)
        logging.info(f"Position for {ticker} not found, max attempts ({max_attempts}) reached.")
        return False

    def get_general_trend(self, ticker):
        """Determine the exponential moving average is generally increasing or decreasing or steady
            INPUT: ticker
            OUTPUT: LONG, SHORT, NO TREND"""
        wait_time_minutes = 15
        max_attempts = 10       # total time is max_attempts * wait_time_minutes as implemented

        #data = ask alpaca API for 30min candles

        try:
            attempts = 0
            while True:
                ema9 = ti.ema(data, 9)
                ema26 = ti.ema(data, 26)
                ema50 = ti.ema(data, 50)

                # if ema50 > ema26  and ema26 > ema9:
                logging.info(f"General Trend Analysis: {ticker}, LONG")
                return "LONG"

                # elif ema50 < ema26 and ema26 < ema9:
                logging.info(f"General Trend Analysis: {ticker}, SHORT")
                return "SHORT"

                # elif attempts < max attempts
                logging.info(f"General Trend Analysis: {ticker}, UNCLEAR, waiting {wait_time_minutes}min...")
                attempts += 1
                time.sleep(60 * wait_time_minutes)

                #else
                logging.info(f"General Trend Analysis: Timeout reached for {ticker}, NO TREND")
                return "NO TREND"

        except Exception as e:
            logging.error(f"General Trend Analysis failed on {ticker}")
            logging.error(e)
            sys.exit()

    def run(self):
        """Runs the trading algorithm to determine enter/exit points"""
        # TODO Implement run
# define asset check the current position

# LOOP
# INITIAL CHECK
#   Ask the broker if we have an open position with asset
#       INPUT: asset
#       OUTPUT: True/False  (position exists/does not exist)
#   Ask the API if if asset is trade-able
#       INPUT: asset
#       OUTPUT: True/False  (position is trade-able/not trade-able)

# GENERAL TREND
#   load the 30min data/candles: request data from API
#       INPUT: Asset/Time Range/Candle Size
#       OUTPUT: 30min Candles data
#   perform general trend analysis: (UP/DOWN/NO TREND)
#       INPUT: 30min Candles data
#       OUTPUT: UP / DOWN / NO TREND
#       If no trend, go back to beginning/next asset

#   LOOP - evaluating indicators
#       STEP 1: load 5min data/candles: request data from API
#           INPUT: Asset/Time Range/Candle Size
#           OUTPUT: 5min Candles data
#       STEP 2: perform instant trend analysis: confirm trend detected by general trend
#           INPUT: 5min Candles data, Output of general trend analysis (UP/DOWN)
#           OUTPUT: True/False (confirmed/not confirmed)
#           If failed, back to STEP 1
#       STEP 3: perform RSI analysis
#           INPUT: 5min Candles data (C), general trend
#           OUTPUT: True/False
#           If failed, back to STEP 1
#       STEP 4: perform stochastic analysis
#           INPUT: 5min Candles data (OHLC), general trend
#           OUTPUT: True/False
#           If Failed, back to STEP 1
#   LOOP until conditions to buy, or timeout to move to next asset

# SUBMIT ORDER
#   submit the order to API
#       INPUT: asset, #shares, price limit
#       OUTPUT: True/False (succeeded/not succeeded), orderID?
#       If false, abort, log error
#   check position exists
#       INPUT: asset, orderID?
#       OUTPUT: True/False (order succeeded/not succeeded)
#       If false, abort, log error

# LOOP (timeout maybe?)
#   ENTER POSITION MODE (LOOP)
#       IF take profit met -> close position (GET OUT)
#       ELIF stop-loss met -> close position (GET OUT)
#       ELIF stoch crossing met -> close position (GET OUT)
#           - Pull 5 min OHLC data
#           - Calculate stochastic data
#           - Determine stochastic crossing

# GET OUT
#   submit order
#       INPUT: asset, #shares
#       OUTPUT: True/False (succeeded/not succeeded), orderID?
#       If false, retry (timeout), abort, log error
#   check position
#       INPUT: asset, orderID?
#       OUTPUT: True/False (position exists/not exists)
#       If true, retry (timeout) (submit order), abort, log error

# wait some amount of time
# back to beginning
