import tkinter
from Mapping_for_Tkinter import Mapping_for_Tkinter

#testing the animation
class racket:
  def __init__(self,mapping,canvas,x_position,y_position):
    #set the main instance values using setter methods
    self.set_mapping(mapping)
    self.set_canvas(canvas)
    self.set_x_position(x_position)
    self.set_y_position(y_position)
    self.set_rectangle_obj(canvas.create_rectangle(mapping.get_i(x_position-30),mapping.get_j(y_position+5),mapping.get_i(x_position+30),mapping.get_j(y_position-5),fill="black"))
    
  ##### get methods for instance attributes
  def get_mapping(self):
    return self.__mapping
  
  def get_canvas(self):
    return self.__canvas
  
  def get_x_position(self):
    return self.__x_position
  
  def get_y_position(self):
    return self.__y_position

  def get_rectangle_obj(self):
    return self.__rectangle_obj

  #### set methods for instance attributes
  def set_mapping(self,mapping):
    self.__mapping=mapping
    
  def set_canvas(self,canvas):
    self.__canvas=canvas
    
  def set_x_position(self,x_position):
    self.__x_position=x_position
    
  def set_y_position(self,y_position):
    self.__y_position=y_position

  def set_rectangle_obj(self,rectangle_obj):
    self.__rectangle_obj=rectangle_obj

  # shift left function
  def shift_left(self):        
    if(self.get_x_position()>-270):
      self.set_x_position(self.get_x_position()-30)
      self.get_canvas().move(self.get_rectangle_obj(),-30,0)  

  # shift right function 
  def shift_right(self):    
    if(self.get_x_position()<270):
      self.set_x_position(self.get_x_position()+30)
      self.get_canvas().move(self.get_rectangle_obj(),+30,0)

  #activate the racket
  def activate_racket(self):
    self.get_canvas().itemconfig(self.get_rectangle_obj(),fill='black')

  #deactivate the racket
  def deactivate_racket(self):
    self.get_canvas().itemconfig(self.get_rectangle_obj(),fill='red')
    
def main():
  
  #create the mapping object   
  mapping=Mapping_for_Tkinter(-300,300,-300,300,600)

  #create window and canvas
  window = tkinter.Tk() 
  canvas = tkinter.Canvas(window, width=600,height=600,bg="white")
  canvas.pack()

  # instantiate racket object
  racket_obj=racket(mapping,canvas,0,-295)

  #bind the action of clicking to the mouse with corresponding action
  canvas.bind("<Button-1>",lambda e:racket_obj.shift_left())
  canvas.bind("<Button-3>",lambda e:racket_obj.shift_right())
  window.mainloop()

if __name__=="__main__":
  main()

