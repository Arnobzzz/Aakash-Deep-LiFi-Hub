from common import *
fig,ax=plt.subplots();ax.plot(X,rx_power(X,m=M_FOCUS)*1000);savefig(fig,'fig_04.png')
