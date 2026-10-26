from common import *
cats=['Speed','Cov','Energy','Sec','Lat','Rel']
ang=[n/6*2*np.pi for n in range(6)]+[0]
smart=[7,9,9,10,9,9,7]
fig=plt.figure();ax=fig.add_subplot(111,polar=True)
ax.plot(ang,smart,'g-');savefig(fig,'fig_19.png')
