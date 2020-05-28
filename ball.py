from Mapping_for_Tkinter import Mapping_for_Tkinter
import tkinter
import math
import time
import random

class ball:
    def __init__(self,mapping,canvas,x0,y0,velocity,angle):
        #set the main instance values using setter methods
        self.set_mapping(mapping)
        self.set_canvas(canvas)
        self.set_x0(x0)
        self.set_y0(y0)
        self.set_velocity(velocity)
        self.set_angle(angle)

        #current x, current y and circle object instant initialize
        self.set_current_x(x0)
        self.set_current_y(y0)
        self.set_circle_obj(canvas.create_oval(mapping.get_i(x0)-4,mapping.get_j(y0)-4,mapping.get_i(x0)+4,mapping.get_j(y0)+4,fill='blue'))
        
    ##### get methods for instance attributes
    def get_mapping(self):
        return self.__mapping
      
    def get_canvas(self):
        return self.__canvas
      
    def get_x0(self):
        return self.__x0
      
    def get_y0(self):
        return self.__y0

    def get_velocity(self):
        return self.__velocity
        
    def get_angle(self):
        return self.__angle

    def get_current_x(self):
        return self.__x

    def get_current_y(self):
        return self.__y

    def get_circle_obj(self):
        return self.__circle

    #### set methods for instance attributes               
    def set_mapping(self,mapping):
        self.__mapping=mapping
    
    def set_canvas(self,canvas):
        self.__canvas=canvas
    
    def set_x0(self,x0):
        self.__x0=x0

    def set_y0(self,y0):
        self.__y0=y0
    
    def set_y_position(self,y0):
        self.__y0=y0

    def set_velocity(self,velocity):
        self.__velocity=velocity

    def set_angle(self,angle):
        self.__angle=angle

    def set_current_x(self,x):
        self.__x=x

    def set_current_y(self,y):
        self.__y=y

    def set_circle_obj(self,circle):
        self.__circle=circle

    # update x y function
    def update_xy(self,t,*args):
        #update x and y
        self.set_current_x(self.get_x0()+self.get_velocity()*math.cos(self.get_angle())*t)
        self.set_current_y(self.get_y0()+self.get_velocity()*math.sin(self.get_angle())*t)
        self.get_canvas().coords(self.get_circle_obj(),self.get_mapping().get_i(self.get_current_x())-4,self.get_mapping().get_j(self.get_current_y())-4,self.get_mapping().get_i(self.get_current_x())+4,self.get_mapping().get_j(self.get_current_y())+4)
        theta_horizontal=math.pi-self.get_angle()
        theta_vertical=0-self.get_angle()
        if (len(args)==1):
            if(args[0]=='top'):
                theta_vertical=random.randrange(-170,-9)*math.pi/180.0
            else:
                theta_vertical=random.randrange(10,171)*math.pi/180.0
        #check boundaries
        if(self.get_current_x()>=self.get_mapping().get_xmax()-4):#right boundary
            self.set_angle(theta_horizontal)
            self.set_x0(self.get_current_x())
            self.set_y0(self.get_current_y())
            return 4
        elif(self.get_current_x()<=self.get_mapping().get_xmin()+4):#left boundary
            self.set_angle(theta_horizontal)
            self.set_x0(self.get_current_x())
            self.set_y0(self.get_current_y())
            return 3
        elif(self.get_current_y()>=self.get_mapping().get_ymax()-4):#top boundary
            self.set_angle(theta_vertical)
            self.set_x0(self.get_current_x())
            self.set_y0(self.get_current_y())
            return 2
        elif(self.get_current_y()<=self.get_mapping().get_ymin()+4):#bottom boundary
            self.set_angle(theta_vertical)
            self.set_x0(self.get_current_x())
            self.set_y0(self.get_current_y())
            return 1
        return 0   
  

def main():
    #create the mapping object   
    mapping=Mapping_for_Tkinter(-300,300,-300,300,600)
    
    #create window and canvas
    window = tkinter.Tk() 
    canvas = tkinter.Canvas(window, width=600,height=600,bg="white")
    canvas.pack()

    #get velocity and theta
    input_val=input("Enter velocity and theta (return for default: 500 pixel/s and 30 degree):")
    if(input_val==""):
        #assign default values
        v=500
        theta=30
    else:
        #split the string list to string
        v,theta=map(int,input_val.split())
    theta=theta*math.pi/180.0
            
    #create ball object
    ball1=ball(mapping,canvas,0,0,v,theta)
    ############################################
    ####### start simulation
    ############################################
    t=0               # real time between event
    t_total=0         # real total time
    count=0           # rebound_total=0
    
    while True:
        t=t+0.01 #real time between events- in second
        t_total=t_total+0.01 #real total time- in second
        side=ball1.update_xy(t)# Update ball position and return collision event
        window.update()   # update the graphic (redraw)
        if side!=0:
            print(t,t_total,count)
            count=count+1 # increment the number of rebounds
            t=0 # reinitialize the local time
        
        if count==10: break # stop the simulation
        time.sleep(0.01)  # wait 0.01 second (simulation time)
            
    print("Total time: %ss"%t_total)
    window.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

