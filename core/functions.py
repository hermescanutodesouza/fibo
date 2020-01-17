import datetime
import sys

from colored import fg, attr
from slugify import slugify


class Enter:
    profile: str = sys.argv[1]
    symbol: str = sys.argv[2]
    cndl: str = sys.argv[3]

    candle: int = int(cndl) * 60
    history: int = int(cndl) * 200

    buy = "line" + sys.argv[4]
    sell = "line" + sys.argv[5]

    def getprofile(self) -> str:
        return slugify("at-fibo-{}_{}_{}_{}".format(self.symbol, self.cndl, self.buy, self.sell))


class Date():
    # start = datetime.datetime.now() - datetime.timedelta(hours=3)
    start = datetime.datetime.now()
    end = None
    now = None
    end = None
    history = None

    def __init__(self, history: int):
        self.history = history
        self.end = self.start - datetime.timedelta(minutes=self.history)

    def getstart(self):
        return "{}".format(self.start)[:19]

    def getend(self):
        return "{}".format(self.end)[:19]


class Status:
    candle_number = 1
    candle_verification_number = 0
    candle_buy_touch = False
    candle_buy_touch_confirmation_below = False
    candle_buy_touch_confirmation_over = False
    candle_buy_touch_number = 0
    candle_sell_touch = False
    candle_sell_touch_confirmation = False
    candle_sell_touch_number = 0
    candle_status = 0
    recalculation = False

    def reset(self):
        self.candle_number = 1
        self.candle_verification_number = 0
        self.candle_buy_touch = False
        self.candle_buy_touch_confirmation_below = False
        self.candle_buy_touch_confirmation_over = False
        self.candle_buy_touch_number = 0
        self.candle_sell_touch = False
        self.candle_sell_touch_confirmation = False
        self.candle_sell_touch_number = 0
        self.candle_status = 0
        self.recalculation = False


def header(enter: object, dt: object):
    print("-" * 100)
    print("Profile {}".format(enter.getprofile()))
    print("Candle {} = {} sec(s)".format(enter.cndl, enter.candle))
    print("Symbol {}".format(enter.symbol))
    print("Buy {}  Sell {}".format(enter.buy, enter.sell))
    print("History   {} - {}".format(dt.getstart(), dt.getend()))
    print("-" * 100)


def closelabel(close: float, lastclose: float) -> str:
    reset = attr('reset')
    if close > lastclose:
        r = fg('green') + "UP"
    elif close < lastclose:
        r = fg('red') + "DOWN"
    else:
        r = fg('blue') + "SAME"
    return r + reset


def closecolor(close: float):
    return "{}{}{}".format(fg('navajo_white_1'), close, attr('reset'))


def metrics(high: float, low: float):
    line = {
        'line6': 1,
        'line5': 0.788,
        'line4': 0.618,
        'line3': 0.5,
        'line2': 0.382,
        'line1': 0.236,
        'line0': 0
    }
    factor = high - low
    return {'line6': high,
            'line5': round(factor * line['line5'] + low, 8),
            'line4': round(factor * line['line4'] + low, 8),
            'line3': round(factor * line['line3'] + low, 8),
            'line2': round(factor * line['line2'] + low, 8),
            'line1': round(factor * line['line1'] + low, 8),
            'line0': low
            }
