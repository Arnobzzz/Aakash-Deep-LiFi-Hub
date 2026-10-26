from common import *
xe=np.linspace(5.1,10,100)
pe=rx_power(xe)*1000
fig,ax=plt.subplots();ax.plot(xe,pe,'r-x');savefig(fig,'fig_16.png')
