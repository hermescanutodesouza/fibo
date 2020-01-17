import datetime
import time

import pymysql.cursors


def getmyconnection(cred: dict):
    connection = pymysql.connect(host=cred['host'],
                                 user=cred['user'],
                                 password=cred['password'],
                                 db=cred['database'],
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    connection.autocommit(True)
    return connection


def getclose(conn: object, symbol: str) -> float:
    time.sleep(1)
    sql = "select * from autotrade.historical_double_value where symbol='{}'" \
          " order by id desc limit 1;".format(symbol)
    with conn.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchone()
    return float(result['value'])


def gethighlow(conn: object, symbol, startDate, endDate) -> (float, float):
    sql = "select max(High) as high, min(low) as low " \
          "from autotrade.vw_data " \
          "where symbol='{}' and `timestamp` <= '{}' and `timestamp` >= '{}'".format(symbol, startDate, endDate)
    with conn.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchone()
    return float(result['high']), float(result['low'])


def saveordem(conn: object, data: dict):
    now = "{}".format(datetime.datetime.now())
    now = now[:19]
    a = data['symbol'].split('/')
    sql = "insert into dados(moeda_compra,moeda_base,origem,data_msg,exc1,id,buy0) " \
          "values( '{}','{}','{}','{}','{}','{}','{}')".format(a[0], a[1],
                                                               data['profile'],
                                                               now,
                                                               'binance',
                                                               "{}".format(datetime.datetime.now()),
                                                               "{}".format(data['close']))
    with conn.cursor() as cursor:
        cursor.execute(sql)
