import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime as dt

np.random.seed(1)

N = 14
y = np.random.rand(N)

now = dt.datetime.now()
then = now + dt.timedelta(days=N)
days = mdates.drange(now,then,dt.timedelta(days=1))

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
plt.plot(days,y)
plt.gcf().autofmt_xdate()
plt.show()