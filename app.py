from flask import Flask,render_template

app =Flask(__name__)
@app.route('/')
def index():
    return render_template('INDEX.HTML')
    
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