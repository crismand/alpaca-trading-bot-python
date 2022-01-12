"""Trading Bot file"""

# define asset

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
