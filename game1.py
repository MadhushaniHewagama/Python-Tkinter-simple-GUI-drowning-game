from Mapping_for_Tkinter import Mapping_for_Tkinter
from racket import racket
from ball import ball
import tkinter
import math      
import random
import time
def play_game1():
    #create the mapping object   
    mapping=Mapping_for_Tkinter(-300,300,-300,300,600)
    #create window and canvas
    window = tkinter.Tk() 
    canvas = tkinter.Canvas(window, width=600,height=600,bg="white")
    canvas.pack()

    # instantiate racket object
    racket_obj=racket(mapping,canvas,0,mapping.get_ymin()+5)
    #bind the action of clicking to the mouse with corresponding action
    canvas.bind("<Button-1>",lambda e:racket_obj.shift_left())
    canvas.bind("<Button-3>",lambda e:racket_obj.shift_right())
       

    # initial values for v and angle
    v=200
    angle=53*math.pi/180.0
    
    #create ball object
    ball1=ball(mapping,canvas,0,mapping.get_ymin()+14,v,angle)
    
    ############################################
    ####### start simulation
    ############################################
    t=0               # real time between event
    t_total=0         # real total time

    while True:
        t=t+0.01 #real time between events- in second
        t_total=t_total+0.01 #real total time- in second
        side=ball1.update_xy(t)# Update ball position and return collision event        
        window.update()   # update the graphic (redraw)
        
        if side!=0:
            t=0
            if(side==2):#top boundaries
                v=v*125/100.0#increase velocity by 25%
                angle=random.randrange(-170,-9)*math.pi/180.0
                ball1.set_velocity(v)
                ball1.set_angle(angle)
                     
        if(ball1.get_current_y()-14<=mapping.get_ymin()):
            
            if (((racket_obj.get_x_position())-30 > (ball1.get_current_x()+4)) or ((ball1.get_current_x()-4)>(racket_obj.get_x_position())+30)):
                print("Game over! Total time: %ss"%t_total)
                window.update() 
                break
            else:
                angle=0-angle
                ball1.set_angle(angle)
                ball1.set_x0(ball1.get_current_x())
                ball1.set_y0(ball1.get_current_y())
                window.update()
                t=0
                

        time.sleep(0.01)  # wait 0.01 second (simulation time)
    window.mainloop() # wait until the window is closed

            
    
    
if __name__=="__main__":
    play_game1()
