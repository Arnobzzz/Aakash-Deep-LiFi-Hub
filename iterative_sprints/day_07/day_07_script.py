from common import *
t=np.linspace(0,12,240)
lifi=np.clip(50-np.cumsum(np.where(t<2,4,np.where(t<6,2.5,1.5))*(12/240)),0,None)
fig,ax=plt.subplots();ax.plot(t,lifi,'g-');savefig(fig,'fig_17.png')
