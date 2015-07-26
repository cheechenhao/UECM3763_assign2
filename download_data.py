% Download data of TNB and KLSE 
from pandas.io.data import DataReader as DR
from datetime import datetime as dt

start = dt(2012,1,1)
end = dt(2015,1,1)
tenaga = DR("5347.KL",'yahoo',start,end)
klse = DR("^KLSE",'yahoo',start,end)
import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pylab as pl

%Generate 5 days moving average 
fig=plt.figure()
fig.patch.set_facecolor('white')
ax1=fig.add_subplot()
tenaga['Close'].plot(ax=ax1,color='b',lw=1,label='TNB Stock Price')
ax2=fig.add_subplot()
pd.rolling_mean(tenaga['Close'],5).plot(ax=ax2,color='r',lw=1,label='5DaysMA')

%Plot moving average on TNB stock price graph
plt.ylabel('Stock Price,RM')
plt.legend(loc='upper left')

from pandas.io.data import DataReader as DR
from datetime import datetime as dt
start1 = dt(2012,1,1)
end1 = dt(2015,1,1)
start2 = dt(2011,10,27)
end2 = dt(2015,1,1)
tenaga = DR("5347.KL",'yahoo',start1,end1)
klse = DR("^KLSE",'yahoo',start2,end2)

import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pylab as pl

%Find the correlation between KLSE and TNB
x=tenaga['Close']
y=klse['Close']
z=np.corrcoef(x,y)
print('Correlation bwtween KLSE and TNB ' + str(z))
    
    