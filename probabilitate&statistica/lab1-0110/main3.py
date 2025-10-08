import numpy as np
import matplotlib.pyplot as plt
# SAMPLES=10000
plt.style.use('dark_background')

ax=plt.gca()
ax.set_aspect('equal', 'box')
ax.set_xlim((-1,1))
ax.set_ylim((-1,1))
def draw_circle(ax):
    # cerc de rază 1
    circle = plt.Circle((0, 0), 1, fill=False, linewidth=2)
    ax.add_patch(circle)

draw_circle(ax)

# ax.set_title("gaura cu contur")
cntr=0
rangmax=2000
for i in range(1,2000):
    rand1= np.random.rand()*np.pi*2
    rand2= np.random.rand()*np.pi*2
    # print(rand1)
    # print(rand2)
    x1=np.cos(rand1)
    y1=np.sin(rand1)
    
    x2=np.cos(rand2)
    y2=np.sin(rand2)
    ax.plot([x1,x2],[y1,y2],linewidth=2, color='red' , alpha=0.1)
    ax.plot([0,x2],[0,y2],linewidth=2, color='blue' , alpha=0.1)
    ax.plot([x1,0],[y1,0],linewidth=2, color='blue' , alpha=0.1)
    mijx=(x1+x2)/2
    mijy=(y1+y2)/2
    ax.plot([mijx,0] , [mijy,0] , linewidth=2, color='green' , alpha=0.1)
    distance=np.hypot(x2-x1, y2-y1)
    if (distance>np.sqrt(3)):
        cntr+=1
ax.set_title(cntr/2000)
plt.show()