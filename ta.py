import numpy
import talib

from numpy import genfromtxt

my_data=genfromtxt('15minutes.csv',delimiter=',')
closes=my_data[:,4]
print(closes)
rsi=talib.RSI(closes)
print("\n \n"+str(rsi))