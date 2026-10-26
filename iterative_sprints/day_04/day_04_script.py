from common import *
s=snr_db(rx_power(X))
fig,ax=plt.subplots();ax.plot(X,rate_mbps(s));savefig(fig,'fig_10.png')
