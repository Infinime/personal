import mplfinance as mpf
import yfinance as yf
import datetime
import time
import sys
yf.pdr_override()

arguments = sys.argv[1:]
for x in range(len(arguments)):
    if arguments[x] == "-t":
        period = int(arguments[x+1])
    if arguments[x] == "-s":
        stock = arguments[x+1]

try:
    period+1
except NameError:
    period = 1

try:
    stock+"d"
except NameError:
    print("Usage: py stockrunner.py -t 1 -s GOOG")
    quit()

print(f"Calculating stock VWAP for {stock} every {period} minute(s)")

# Variables
tpv_arr = []
vol_arr = []
vwap_arr = []
stockprice_arr = []
index_name = '^GSPC'  # S&P 500
start_date = datetime.datetime.now() - datetime.timedelta(days=1)
end_date = datetime.date.today()
timern = datetime.datetime.now()
returns_multiples = []
df = yf.download(stock, period='1d', interval="1m")
typical_price = (df["High"][-2]+df["Close"][-2]+df["Low"][-2])/3
turns = 0

while turns < 60/period:
    df = yf.download(stock, period='1d', interval="1m")
    tpv = typical_price*df["Volume"][-2]
    tpv_arr += [tpv]
    vol_arr += [df["Volume"][-2]]
    cumulative_tpv = sum(tpv_arr)
    cumulative_vol = sum(vol_arr)
    vwap = cumulative_tpv/cumulative_vol
    time.sleep(period*60)
    turns += 1

graph = mpf.plot(df, type='candle',  style='charles', volume=True)
print(f"VWAP for {stock} is {vwap}")
