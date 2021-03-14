from flask import Flask,render_template
import api,csv
from binance.client import Client
app =Flask(__name__)

client = Client(api.API_KEY, api.API_SECRET,tld='com')




@app.route('/')
def index():
    title="BINAMOOSE VIEW"
    info=client.get_account()
    balances=info['balances']
    print(balances)
    return render_template('templates/INDEX.HTML',title=title, my_balances=balances)
   
    
@app.route('/buy')
def buy():
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