import turtle 
from turtle_chat_client import Client
from turtle_chat_widgets import Button, TextInput



class TextBox(TextInput):
    def draw_box(self):
        turtle.penup()
        turtle.goto(self.pos)
        turtle.pendown()
        turtle.goto(0, self.height)
        turtle.goto(self.width, self.height)
        turtle.goto(self.width, 0)
        turtle.goto(self.pos)
        turtle.mainloop()
        

        
    def write_msg(self):
        self.setup_listeners()
        print(self.new_msg)
        self.writer.goto(5,self.height -10)
        self.writer.write(self.new_msg)
tb= TextBox()



    
