from common import *
p1=rx_power(X,tx_x=-2.5);p2=rx_power(X,tx_x=2.5)
comb=np.maximum(p1,p2)
fig,ax=plt.subplots();ax.plot(X,comb*1000,'k-');savefig(fig,'fig_20.png')
