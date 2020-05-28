from Mapping_for_Tkinter import Mapping_for_Tkinter
from racket import racket
from ball import ball
import tkinter
import math      
import random
import time
def play_game2():
    #create the mapping object   
    mapping=Mapping_for_Tkinter(-300,300,-300,300,600)
    #create window and canvas
    window = tkinter.Tk() 
    canvas = tkinter.Canvas(window, width=600,height=600,bg="white")
    canvas.pack()

    # instantiate racket object
    racket_obj_top=racket(mapping,canvas,0,mapping.get_ymax()-5)
    racket_obj_bottom=racket(mapping,canvas,0,mapping.get_ymin()+5)

    # initial values for v and angle
    v=300
    angle=45*math.pi/180.0
    
    #create ball object
    ball1=ball(mapping,canvas,0,mapping.get_ymax()-14,v,angle)
    #bind the action of clicking to the mouse with corresponding action
    #canvas.bind("<Button-1>",lambda e:racket_obj.shift_left())
    #canvas.bind("<Button-3>",lambda e:racket_obj.shift_right())
       
   
    
    ############################################
    ####### start simulation
    ############################################
    t=0               # real time between event
    t_total=0         # real total time
    
    while True:
        t=t+0.01 #real time between events- in second
        t_total=t_total+0.01 #real total time- in second
        previous_y=ball1.get_current_y()#previous y value of ball
        side=ball1.update_xy(t)# Update ball position and return collision event
        window.update()   # update the graphic (redraw)
        if(side !=0):
            t=0
        if(previous_y<ball1.get_current_y()):
            racket_obj_top.deactivate_racket()
            racket_obj_bottom.activate_racket()
            canvas.bind("<Button-1>",lambda e:racket_obj_top.shift_left())
            canvas.bind("<Button-3>",lambda e:racket_obj_top.shift_right())
        else:
            racket_obj_bottom.deactivate_racket()
            racket_obj_top.activate_racket()
            canvas.bind("<Button-1>",lambda e:racket_obj_bottom.shift_left())
            canvas.bind("<Button-3>",lambda e:racket_obj_bottom.shift_right())        
        
        if(int(ball1.get_current_y())-14==int(mapping.get_ymin())):            
            if ((((racket_obj_bottom.get_x_position())-30 > (ball1.get_current_x())) or ((ball1.get_current_x())>(racket_obj_bottom.get_x_position())+30))):
                print("Game over for Racket 1!")
                window.update() 
                break
            else:
                side=ball1.update_xy(t,'top')
                
                
        if(int(ball1.get_current_y())+14==int(mapping.get_ymax())):
            if ((((racket_obj_top.get_x_position())-30 > (ball1.get_current_x())) or ((ball1.get_current_x())>(racket_obj_top.get_x_position())+30))):
                print("Game over for Racket 2!")
                window.update() 
                break
            else:
                side=ball1.update_xy(t,'bottom')
        time.sleep(0.01)  # wait 0.01 second (simulation time)
                

        time.sleep(0.01)  # wait 0.01 second (simulation time)
    window.mainloop() # wait until the window is closed

            
    
    
if __name__=="__main__":
    play_game2()
