from Mapping_for_Tkinter import Mapping_for_Tkinter
from tkinter import *
import math
import time
def cannonball():
    #create mapping object
    m=Mapping_for_Tkinter(0.0,1200.0,0.0,400.0,1200)

    #### instantiate a tkinter window 
    window = Tk() 
    canvas = Canvas(window, width=m.get_width(),height=m.get_height(),bg="white") # create a canvas width*height
    canvas.pack()

    # initial origin 
    x0=0
    y0=m.get_ymin()+4

    x=x0
    y=y0

    v=70#default velocity
    theta=(60*math.pi)/180.0
    strength=0.75
    g=9.8

   
    # strengths
    strength=0.75
    count=0
    input_str=input("Enter both theta(0,90) and strength (return for default 60 degree and 0.75):")
    if(input_str !=""):
        theta,strength=map(float,input_str.split())
    distance=x
    
    point=canvas.create_oval(m.get_i(x0)-3,m.get_j(y0)-3,m.get_i(x0)+5,m.get_j(y0)+5,fill='blue')
    x_privious=x0
    y_privious=y0
    t=0
    t_total=0
    while True:
        t=t+0.1 #real time between events- in second
        t_total=t_total+0.1 #real total time- in second
        window.update()   # update the graphic (redraw)
        #y calculate
        y=y0+v*math.sin(theta)*t-(9.8/2)*((t)**2)
        
        #x calculate
        x=v*math.cos(theta)*t
        
        #check bounced happen
        if(y<=m.get_ymin()+4):
            y=0
            canvas.coords(point,m.get_i(distance)-3,m.get_j(y)-3,m.get_i(distance)+5,m.get_j(y)+5)
            count=count+1
            t=0
            distance=distance+x
            v=v*strength          
            
            canvas.create_oval(m.get_i(distance)+1,m.get_j(y)+1,m.get_i(distance)+1,m.get_j(y)+1,fill='blue')
                   
        else:
            canvas.coords(point,m.get_i(x+distance)-3,m.get_j(y)-3,m.get_i(x+distance)+5,m.get_j(y)+5)
            canvas.create_oval(m.get_i(x+distance)+1,m.get_j(y)+1,m.get_i(x+distance)+1,m.get_j(y)+1,fill='blue')
            
        if(distance+x>=int(m.get_xmax()) or v<0.01):
            break
        time.sleep(0.02)  # wait 0.02 second (simulation time)
        x_privious=x
        y_privious=y
    canvas.itemconfig(point,fill='red')
    distance=distance+x
    print(distance)
    print('Total number of rebounds is: %s'%str(count))
    print('Total real time is: %ss'%str(t_total))
    print('Distance traveled is: %sm'%str(distance))
    window.mainloop() # wait until the window is closed
        



                                
if __name__=="__main__":
    cannonball()
