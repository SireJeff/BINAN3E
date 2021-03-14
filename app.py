from flask import Flask,render_template
import api,csv
from binance.client import Client
from binance.enums import *

app =Flask(__name__)

client = Client(api.API_KEY, api.API_SECRET,tld='com')




@app.route('/')
def index():
    title="BINAMOOSE VIEW"
    account=client.get_account()
    balances=account['balances']
    info= client.get_exchange_info()
    symbols=info['symbols']
    print(balances)
    return render_template('INDEX.HTML',title=title, my_balances=balances,symbols=symbols)
   
    
@app.route('/buy')
def buy():
    order = client.create_order(
    symbol='BNBBTC',
    side=SIDE_BUY,
    type=ORDER_TYPE_LIMIT,
    timeInForce=TIME_IN_FORCE_GTC,
    quantity=100,
    price='0.00001')
    return'buy'

@app.route('/sell')
def sell():
    return'sell'

@app.route('/settings')
def settings():
    return'settings'
print("shut the fuck up about moon man")
print("this should be fun")
cvsfiles= open("data/fuck.txt","w")