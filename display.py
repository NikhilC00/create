
from Tkinter import *

FrameX= 1000
FrameY = 500
frame.geometry("FrameXxFrameY")
frame.title("Assignment Helper")

def createFrame():
  frame.geometry("1000x500")
  frame.title("Assignment Helper")
  Title = Label(text="Welcome to Assignment Helper:")
  Title.place(x=10, y=10)
	Instr1 = Label(text="This program will help you manage your time for your assignments")
  Instr1.place(x=10, y=30)
	
	InstrStartTime = Label(text="Please enter the time you want to start working:")
	InstrStartTime.place(x=10, y=70)
	StartTime = Text(width= 10, height= 1)
	StartTime.place(x= 500, y= 70)
	
	Instr2 = Label(text="Name of the Assignment")
  Instr2.place(x=10, y=100)
	
	Instr2 = Label(text="Estimated Time to\n Complete Assignemnt")
  Instr2.place(x=10, y=100)
	
	Instr2 = Label(text="Name of the Assignment")
  Instr2.place(x=10, y=100)
	
	requestMon = Label(text="How many hours did you get Monday night?")
	requestMon.place(x=40, y=120)
	inputMon = Text(width= 10, height= 1)
	inputMon.place(x= 350, y= 120)
	
	
