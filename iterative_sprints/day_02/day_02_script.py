from common import *
blocked=(X>-1)&(X<1)
pb=np.where(blocked,0,rx_power(X)*1000)
fig,ax=plt.subplots();ax.plot(X,pb,color='red');savefig(fig,'fig_03.png')
