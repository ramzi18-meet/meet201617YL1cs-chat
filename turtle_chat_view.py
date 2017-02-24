#2016-2017 PERSONAL PROJECTS: TurtleChat!
'''
Ramzi Beidas
'''

#####################################################################################
#                                   IMPORTS                                         #
#####################################################################################
import turtle 
from turtle_chat_client import Client
from turtle_chat_widgets import Button, TextInput
#####################################################################################
#####################################################################################

#####################################################################################
#                                   TextBox                                         #
#####################################################################################
#Make a class called TextBox, which will be a subclass of TextInput.
class TextBox(TextInput):
    def draw_box(self):
        #print (" in draw box")
        turtle.clear()
        turtle.penup()
        turtle.goto(self.pos)
        turtle.pendown()
        turtle.goto(0, self.height)
        turtle.goto(self.width, self.height)
        turtle.goto(self.width, 0)
        turtle.goto(self.pos)
          
    
#Because TextInput is an abstract class, you must implement its abstract
#methods.  There are two:
#
#draw_box
#write_msg
    def write_msg(self):
        print ("in write message")
        self.writer.clear()
        self.writer.hideturtle()
        self.setup_listeners()
        self.writer.goto(5,self.height -10)
        self.writer.write(self.new_msg)
        

#
#Hints:
#1. in draw_box, you will draw (or stamp) the space on which the user's input
#will appear.
#
#2. All TextInput objects have an internal turtle called writer (i.e. self will
#   have something called writer).  You can write new text with it using code like
#
#   self.writer.write(a_string_variable)
#
#   and you can erase that text using
#
#   self.writer.clear()
#
#3. If you want to make a newline character (i.e. go to the next line), just add
#   \r to your string.  Test it out at the Python shell for practice
#####################################################################################
#####################################################################################

#####################################################################################
#                                  SendButton                                       #
#####################################################################################
class SendButton(Button):
    def __init__(self, my_turtle=None, shape=None, pos=(0,0), view=None):
        super(SendButton, self).__init__(my_turtle=None, shape=None, pos=(0,-150))
        self.view = view
        
    def fun(self, x=None, y=None):
        #print type(self.view)
        self.view.send_msg()



#Make a class called SendButton, which will be a subclass of Button.
#Button is an abstract class with one abstract method: fun.
#fun gets called whenever the button is clicked.  It's jobs will be to
#
# 1. send a message to the other chat participant - to do this,
#    you will need to call the send method of your Client instance
# 2. update the messages that you see on the screen
#
#HINT: You may want to override the __init__ method so that it takes one additional
#      input: view.  This will be an instance of the View class you will make next
#      That class will have methods inside of it to help
#      you send messages and update message displays.
#####################################################################################
#####################################################################################


##################################################################
#                             View                              " #
##################################################################
#Make a new class called View.  It does not need to have a parent
#class mentioned explicitly.
#
#Read the comments below for hints and directions.
##################################################################
##################################################################
class View:
    _MSG_LOG_LENGTH=5 #Number of messages to retain in view
    _SCREEN_WIDTH=300
    _SCREEN_HEIGHT=600
    _LINE_SPACING=round(_SCREEN_HEIGHT/2/(_MSG_LOG_LENGTH+1))

    def __init__(self,username='Me',partner_name='Partner'):
        '''
        :param username: the name of this chat user
        :param partner_name: the name of the user you are chatting with
        '''
        ###
        #Store the username and partner_name into the instance.
        ###
        self.username = username
        self.partner_name = partner_name
        

        #Make a new client object and store it in this i4nstance.
        self.my_client = Client()

        #Set screen dimensions using turtle.setup
        #You can get help on this function, as with other turtle functions,
        #by typing
        #4
        #   import turtle
        #   help(turtle.setup)
        #
        #at the Python shell.
        turtle.setup(width=self._SCREEN_WIDTH, height=self._SCREEN_HEIGHT)

        #This list will store all of the messages.
        #You can add strings to the front of the list using
        #   self.msg_queue.insert(0,a_msg_string)
        #or at the end of the list using
        #   self.msg_queue.append(a_msg_string)
        self.msg_queue=[]

        ###
        #Create one turtle object for each message to display.
        #You can use the clear() and write() methods to erase
        #and write messages for each
        ###
        self.last_message = turtle.clone()
        
        ###
        #Create a TextBox instance and a SendButton instance and
        #Store them inside of this instance
        ###
        self.send_button = SendButton(view=self)
        self.text_box = TextBox()

        ###
        #Call your setup_listeners() function, if you have one,
        #and any other remaining setup functions you have invented.
        ###
        self.setup_listeners()

    def send_msg(self):
        '''
        You should implement this method.  It should call the
        send() method of the Client object stored in this View
        instance.  It should also call update the list of messages,
        self.msg_queue, to include this message.  It should
        clear the textbox text display (hint: use the clear_msg method).
        It should call self.display_msg() to cause the message
        display to be updated.
        '''
        print("self.text_box.new_msg= ", self.text_box.new_msg)
        self.my_client.send(self.text_box.new_msg)
        self.msg_queue.append(self.text_box.new_msg)
        self.text_box.clear_msg()
        self.display_msg()

    def get_msg(self):
        return self.text_box.get_msg()

    def setup_listeners(self):
        '''
        Set up send button - additional listener, in addition to click,
        so that return button will send a message.
        To do this, you will use the turtle.onkeypress function.
        The function that it will take is
        self.send_btn.fun
        where send_btn is the name of your button instance

        Then, it can call turtle.listen()
        '''
        turtle.onkeypress(self.send_button.fun,'Return')
        turtle.listen()

    def msg_received(self,msg):
        '''
        This method is called when a new message is received.
        It should update the log (queue) of messages, and cause
        the view of the messages to be updated in the display.

        :param msg: a string containing the message received
                    - this should be displayed on the screen
        '''
        print("here: " + msg) #Debug - print message
        show_this_msg = self.partner_name+' says:\r'+ msg
        #Add the message to the queue either using insert (to put at the beginning)
        #or append (to put at the end).
        #
        #Then, call the display_msg method to update the display
        self.msg_queue.insert(0, show_this_msg)
        self.display_msg()

    def display_msg(self):
        '''
        This method should update the messages displayed in the screen.
        You can get the messages you want from self.msg_queue
        '''
        self.last_message.clear()
        self.last_message.write(self.msg_queue[0])

##############################################################
##############################################################


#########################################################
#Leave the code below for now - you can play around with#
#it once you have a working view, trying to run you chat#
#view in different ways.                                #
#########################################################
if __name__ == '__main__':
    my_view=View()
    _WAIT_TIME=200 #Time between check for new message, ms
    def check() :
        msg_in=my_view.my_client.receive()
        if not(msg_in is None):
            print("in name: " + msg_in)
            if msg_in==my_view.my_client._END_MSG:
                print('End message received')
                sys.exit()
            else:
                my_view.msg_received(msg_in)
        turtle.ontimer(check,_WAIT_TIME) #Check recursively
    check()
    turtle.mainloop()
