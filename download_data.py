from pandas.io.data import DataReader as DR
from datetime import datetime as dt

import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pylab as pl

%Download data of tenaga nasional and klse
start = dt(2012,1,1)  
end = dt(2015,1,1)
tenaga = DR("5347.KL",'yahoo',start,end)
klse = DR("^KLSE",'yahoo',start,end)

%Draw tenaga nasional stock chart
fig=plt.figure()
fig.patch.set_facecolor('white')
ax1=fig.add_subplot()
tenaga['Close'].plot(ax=ax1,color='b',lw=1,label='TNB Stock Price')
ax2=fig.add_subplot()

%Find moving average and draw the moving average graph
pd.rolling_mean(tenaga['Close'],5).plot(ax=ax2,color='r',lw=1,label='5DaysMA')
plt.ylabel('Stock Price,RM')
plt.legend(loc='upper left')

