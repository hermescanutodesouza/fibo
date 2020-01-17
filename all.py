import os

stream = os.popen('echo Returned output')
output = stream.read()

coins = ['ADA/BTC', 'BCH/BTC', 'BNB/BTC',
         'DASH/BTC', 'EOS/BTC', 'ETC/BTC',
         'ETH/BTC', 'LINK/BTC', 'LTC/BTC',
         'NEO/BTC', 'TRX/BTC', 'XLM/BTC',
         'XMR/BTC', 'XRP/BTC', 'ZEC/BTC']
candles = [1, 3, 5, 10, 15, 30, 60]
lines = [1, 2]

cmd = "nohup python3 main.py {} {} {} {} {} &"


def checkprocess(profile):
    cmd = "ps -fe |grep {} | grep -v grep | wc -l".format(profile)
    stream = os.popen(cmd)
    output = stream.read()
    return int(output)


for coin in coins:
    for candle in candles:
        for line in lines:
            profile = "at-fibo-{}-{}-{}".format(coin, candle, line)
            if checkprocess(profile) == 0:
                e = cmd.format(profile, coin, candle, line, 4)
                print(e)
                os.system(e)
            else:
                print("Rodando {}".format(profile))
                # print(cmd.format(profile, item, c))
                # aloha070
