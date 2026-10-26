from common import *
s=snr_db(rx_power(X))
smart=np.where(s>26,60,np.where(s>22,40,np.where(s>18,20,np.where(s>12,10,0))))
fig,ax=plt.subplots();ax.plot(X,smart);savefig(fig,'fig_12.png')
