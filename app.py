from flask import Flask,render_template,request,flash, redirect , jsonify
import api,csv
from binance.client import Client
from binance.enums import *
import websocket, json, pprint, talib, numpy
import config


Client.getorder


app =Flask(__name__)

app.secret_key=b"dsssssssssssssssssssssssssssddsdssddssddssdsdsdsdsd"

client = Client(api.API_KEY, api.API_SECRET,tld='com')

kk=client.get_historical_klines("BTCUSDT",client.KLINE_INTERVAL_1DAY,"1 Jul,2020","12 Jan,2021")
print(kk)
""" try:
    print(client.get_trade_fee())
except Exception as e:
    print(e.message) """
@app.route('/')
def index():
    title="BINAMOOSE VIEW"
    account=client.get_account()
    balances=account['balances']
    accinfo= client.get_exchange_info()
    symbols=accinfo['symbols']
    print(balances)
    return render_template('INDEX.HTML',title=title, my_balances=balances,symbols=symbols)
if __name__ == '__main__':
    app.run(debug=True)
   
   
""" @app.route('/orders', methods=['POST'])
def ger_orders():
    try:
        orders=client.get_trade_fee()
        flash(orders,"info")
       
    except Exception as e:
        print(e.mesaage)
     return redirect('/') """

@app.route('/buy', methods=['POST'])
def buy():
    try:
        order = client.create_order(
        symbol=request.form['symbol'],
        side=SIDE_BUY,
        type=ORDER_TYPE_LIMIT,
        timeInForce=TIME_IN_FORCE_GTC,
        quantity=request.form['quantity'],
        price=request.form['limit'])
    except Exception as e:
        flash(e.message,"error")

    return redirect('/')


@app.route('/sell')
def sell():
    return'sell'

@app.route('/settings')
def settings():
    return'settings'
print("shut the fuck up about moon man")
print("this should be fun")
cvsfiles= open("data/fuck.txt","w")

@app.route('/history')
def history():
    candelsticks=client.get_historical_klines("BTCUSDT",client.KLINE_INTERVAL_1DAY,"1 Jul,2020","16 Mar,2021")
    proccessed_candlesticks=[]
    for data in candelsticks:
        candelstick={
            "time": data[0]/1000,
            "open": data[1], 
            "high": data[2],
            "low": data[3],
            "close": data[4]
           
        }
        proccessed_candlesticks.append(candelstick)
        
    return jsonify(proccessed_candlesticks)



SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1h"

""" RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
TRADE_SYMBOL = 'ETHUSD'
TRADE_QUANTITY = 0.05 """

closes = []
in_position = False
buy_orders=[]
initiated_buy_orders=[]
client = Client(api.API_KEY, api.API_SECRET, tld='com')

funds_USDT=client.get_asset_balance(asset='USDT')
shares=funds_USDT/4
def order(side, quantity, symbol,order_type=ORDER_TYPE_LIMIT):
    try:
        print("sending order")
        order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=shares)
        print(order)
    except Exception as e:
        print("an exception occured - {}".format(e))
        return False

    return True
    
def on_open(ws):
    print('opened connection')

def on_close(ws):
    print('closed connection')

def on_message(ws, message):
    global closes, in_position
    
    print('received message')
    json_message = json.loads(message)
    pprint.pprint(json_message)

    candle = json_message['k']

    is_candle_closed = candle['x']
    close = candle['c']

    if is_candle_closed:
        print("candle closed at {}".format(close))
        closes.append(float(close))
        print("closes")
        print(closes)

        if len(closes) > RSI_PERIOD:
            np_closes = numpy.array(closes)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            print("all rsis calculated so far")
            print(rsi)
            last_rsi = rsi[-1]
            print("the current rsi is {}".format(last_rsi))

            if last_rsi > RSI_OVERBOUGHT:
                if in_position:
                    print("Overbought! Sell! Sell! Sell!")
                    # put binance sell logic here
                    order_succeeded = order(SIDE_SELL, TRADE_QUANTITY, TRADE_SYMBOL)
                    if order_succeeded:
                        in_position = False
                else:
                    print("It is overbought, but we don't own any. Nothing to do.")
            
            if last_rsi < RSI_OVERSOLD:
                if in_position:
                    print("It is oversold, but you already own it, nothing to do.")
                else:
                    print("Oversold! Buy! Buy! Buy!")
                    # put binance buy order logic here
                    order_succeeded = order(SIDE_BUY, TRADE_QUANTITY, TRADE_SYMBOL)
                    if order_succeeded:
                        in_position = True

                
ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()