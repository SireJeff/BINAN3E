import api,csv
from binance.client import Client
client = Client(api.API_KEY, api.API_SECRET)

candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

csvfile =open('15minutes.csv','w',newline='') 
candlestick_writer=csv.writer(csvfile , delimiter=',')
accinfo= client.get_exchange_info()
symbolss=accinfo['symbols']
csvfile_symbol =open('symbols.csv','w',newline='') 
symbol_writer=csv.writer(csvfile_symbol)
for symbol in symbolss:
    symbol_writer.writerow(symbol['symbol'])
for candlestick in candles:
    print(candlestick)
    candlestick_writer.writerow(candlestick)
csvfile.close()
candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Dec, 2017", "1 MAR, 2021")

csvfileALL =open('BTCALLTIME_15M.csv','w',newline='') 
candlestick_writerALL=csv.writer(csvfileALL , delimiter=',')


for candlestick in candlesticks:
    candlestick_writerALL.writerow(candlestick)

csvfileALL.close()