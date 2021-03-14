from flask import Flask,render_template,request,flash, redirect
import api,csv
from binance.client import Client
from binance.enums import *


app =Flask(__name__)
app.secret_key=b"dsssssssssssssssssssssssssssddsdssddssddssdsdsdsdsd"
client = Client(api.API_KEY, api.API_SECRET,tld='com')

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