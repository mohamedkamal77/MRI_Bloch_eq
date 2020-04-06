
import matplotlib
matplotlib.use('Tkagg')
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
global t ,x ,y , z,h2
t=0
global B,T1,T2,gy,flip_angle
def update_line(hl,h2, new_data,de=False):
	xdata, ydata, zdata = hl._verts3d
	if de == False :

		hl.set_xdata(list(np.append(xdata, new_data[0])))
		hl.set_ydata(list(np.append(ydata, new_data[1])))
		hl.set_3d_properties(list(np.append(zdata, new_data[2])))
        #  	xdata1, ydata1, zdata1 = h2._verts3d
		h2.set_xdata(list([0, new_data[0]]))
		h2.set_ydata(list([0,new_data[1]]))
		h2.set_3d_properties(list([0, new_data[2]]))
		plt.draw()


def excitation():
    global t ,x ,y , z,h2
    x = 0
    y = 0
    z= 1*( np.exp(-1*(0/T1)))
    hl, = map_ax.plot3D([x], [y], [z])
    h2, = map_ax.plot3D([0], [0], [0],'r') 
    end_exitation_z =   (np.cos((flip_angle/180)*3.1415))**2  + 0.019

    while (z > end_exitation_z):
        #MX
        x = 1*(1 -np.exp(-1*(t/T2))) *np.sin(B*gy*t)
        
        #My
        y = 1*(1- np.exp(-1*(t/T2)))*np.cos(B*gy*t)
        
        #Mz 
        z= 1*( np.exp(-1*(t/T1))) 
        
        update_line(hl,h2, (x,y, z))
        t= t + 0.001
        plt.show(block=False)
        plt.pause(0.000001)

def relaxation():
    global t ,x ,y , z,h2
    t = -1*np.log(1 -(z))*T1
    #Mx
    x = 1*(np.exp(-1*(t/T2))) *np.sin(B*gy*t)    
    #My 
    y = 1*(np.exp(-1*(t/T2)))*np.cos(B*gy*t)    
    #Mz 
    z= 1*(1- np.exp(-1*(t/T1))) 
    h3, = map_ax.plot3D([x], [y], [z],color='green')
    #h2, = map_ax.plot3D([0], [0], [0],color= 'r') 
    while (z < 1):        
        #Mx = 2*np.exp(t/T2) np.sin(W*t)
        x = 1*(np.exp(-1*(t/T2))) *np.sin(B*gy*t)
        
        #My = 2*np.exp(t/T2) np.cos(W*t)
        y =1*(np.exp(-1*(t/T2)))*np.cos(B*gy*t)
        
        #Mz = 10*(1 -np.exp(t/T1))
        z= 1*(1- np.exp(-1*(t/T1))) 
        
        #ax.plot([0,1],[0,1] ,[0,1], zdir='z')
        update_line(h3,h2, (x,y, z))
        t= t + 0.001
        plt.show(block=False)
        plt.pause(0.000001)
 
def get_param():
    global B,T1,T2,gy,flip_angle
    B = float(input("Enter B in Micro: "  )) 
    T1 = float(input("Enter T1 in sec: "))
    T2 = float(input("Enter T2 sec: "))
    gy = float(input("Enter gyromagnetic Miga: "))
    flip_angle = float(input("Float angle Degree:  "))
 
map = plt.figure()
map_ax = Axes3D(map)
map_ax.autoscale(enable=True, axis='both', tight=True)
 
# # # Setting the axes properties
map_ax.set_xlim3d([-1.0, 1.0])
map_ax.set_ylim3d([-1.0, 1.0])
map_ax.set_zlim3d([-1.0, 1.0])

red_patch = mpatches.Patch(color='red', label='Bulk Vector')
#plt.legend(handles=[red_patch])
blue_patch = mpatches.Patch(color='blue', label='Excitation')
#plt.legend(handles=[blue_patch])
green_patch = mpatches.Patch(color='g', label='Relaxation')
plt.legend(handles=[red_patch,blue_patch,green_patch])

plt.show()
#get parameters by console
get_param()
#Excitation
excitation()
# Relaxiation
relaxation()
 
plt.show(block=True)