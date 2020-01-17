import datetime
import pprint

from core.functions import Enter, Date, header, Status, metrics, closecolor, closelabel
from database.config import autotrade, ordem
from database.functions import getmyconnection, getclose, gethighlow, saveordem

pp = pprint.PrettyPrinter(indent=1)

# create the connection with  autotrade
conn = getmyconnection(autotrade)
ordemconn = getmyconnection(ordem)

candle_status = True

# get all parameters from command line
start = Enter()

# create the history of candles
dt = Date(start.history)

# set all the status
status = Status()

lastclose = 0
count = 0

# get the high and close from a history of candles
high, low = gethighlow(conn, start.symbol, dt.getstart(), dt.getend())

# print the inital info
header(start, dt)

# get all metric for fibonacci
m = metrics(high, low)
pp.pprint(m)
try:
    while True:
        l = ""
        count += 1
        # get the last close
        close = getclose(conn, start.symbol)

        if close < low:
            print("New low {}".format(close))
            m = metrics(high, close)
            low = close
            pp.pprint(m)

        if close > high:
            print("New high {}".format(close))
            m = metrics(close, low)
            high = close
            pp.pprint(m)

        if close < m[start.buy]:
            l = "Touched the line to buy {}".format(start.buy)
            status.candle_buy_touch_number = status.candle_number

        print("{} {:<23} {:>17} {:>5} {:>5}   {}".format(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            closecolor(close),
            closelabel(close, lastclose),
            status.candle_number,
            count,
            l))
        lastclose = close

        if count == start.candle:
            print("Candle Closed {}".format(close))

            if close > m[start.buy] and \
                    status.candle_number > status.candle_buy_touch_number and \
                    status.candle_buy_touch_number > 0:
                print("Over the {}".format(start.buy))
                print("Ordey buy")
                # save the ordem
                saveordem(ordemconn, {"close": close, 'symbol': start.symbol, 'profile': start.getprofile()})
                candle_status = True
                status.reset()

            status.candle_number += 1
            count = 0
finally:
    conn.close()
