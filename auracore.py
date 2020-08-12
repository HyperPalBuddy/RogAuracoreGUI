#!/usr/bin/env python3


from tkinter import *
import os

clrred = "ff0000"
clrgrn = "00ff00"
clrblu = "0000ff"
clrylw = "ffff00"
clrgld = "ff8c00"
clrcyn = "00ffff"
clrmgt = "ff00ff"
clrwte = "ffffff"
clrblk = "000000"


global firstbtnpress
global secondbtnpress
global thirdbtnpress


root = Tk()
root.title("Aura Core")



'''#---------------------------------------------------------------------------------------------------
Static Colour Choices
	red
   	green
   	blue
   	yellow
   	gold
   	cyan
   	magenta
   	white
   	black
'''#---------------------------------------------------------------------------------------------------


'''
	Single Colour Options
	'''
def StaticColour():
	top = Toplevel()
	top.title = "Single Colour Settings"


	Redbtn = Button(top, text="Red",width="25", command= lambda:os.system("sudo rogauracore single_static "+ clrred)).pack()
	Greenbtn = Button(top, text="Green",width="25", command= lambda:os.system("sudo rogauracore single_static "+clrgrn)).pack()
	Bluebtn = Button(top, text="Blue",width="25",command= lambda:os.system("sudo rogauracore single_static "+clrblu)).pack()
	Yellowbtn = Button(top, text="Yellow",width="25",command= lambda:os.system("sudo rogauracore single_static "+clrylw)).pack()
	Goldbtn = Button(top, text="Gold",width="25",command= lambda:os.system("sudo rogauracore single_static "+clrgld)).pack()
	Cyanbtn = Button(top, text="Cyan",width="25",command= lambda:os.system("sudo rogauracore single_static "+clrcyn)).pack()
	Magentabtn = Button(top, text="Magenta",width="25",command= lambda:os.system("sudo rogauracore single_static "+clrmgt)).pack()
	Whitebtn = Button(top, text="White",width="25",command= lambda:os.system("sudo rogauracore single_static "+clrwte)).pack()
	Offbtn = Button(top, text="Off",width="25",command= lambda:os.system("sudo rogauracore single_static "+clrblk)).pack()


'''
	Brightness Control
	'''

def BrightnessControl():

	top = Toplevel()
	top.title = "Choose Brightness Level"

	Onebtn = Button(top, text="1",width="25", command= lambda:os.system("sudo rogauracore brightness 1")).pack()
	Twobtn = Button(top, text="2",width="25", command= lambda:os.system("sudo rogauracore brightness 2")).pack()
	Threebtn = Button(top, text="3",width="25", command= lambda:os.system("sudo rogauracore brightness 3")).pack()




# First Button Presses In Multi
def FirstRed():
	global firstbtnpress
	firstbtnpress="ff0000"
def FirstGreen():
	global firstbtnpress
	firstbtnpress="00ff00"
def FirstBlue():
	global firstbtnpress
	firstbtnpress="0000ff"
def FirstYellow():
	global firstbtnpress
	firstbtnpress="ffff00"
def FirstGold():
	global firstbtnpress
	firstbtnpress="ff8c00"
def FirstCyan():
	global firstbtnpress
	firstbtnpress="00ffff"
def FirstMagenta():
	global firstbtnpress
	firstbtnpress="ff00ff"
def FirstWhite():
	global firstbtnpress
	firstbtnpress="ffffff"
def FirstOff():
	global firstbtnpress
	firstbtnpress="000000"

# Second Button Presses In Multi
def SecondRed():
	global secondbtnpress
	secondbtnpress="ff0000"
def SecondGreen():
	global secondbtnpress
	secondbtnpress="00ff00"
def SecondBlue():
	global secondbtnpress
	secondbtnpress="0000ff"
def SecondYellow():
	global secondbtnpress
	secondbtnpress="ffff00"
def SecondGold():
	global secondbtnpress
	secondbtnpress="ff8c00"
def SecondCyan():
	global secondbtnpress
	secondbtnpress="00ffff"
def SecondMagenta():
	global secondbtnpress
	secondbtnpress="ff00ff"
def SecondWhite():
	global secondbtnpress
	secondbtnpress="ffffff"
def SecondOff():
	global secondbtnpress
	secondbtnpress="000000"

# Third Button Presses AKA Speed Setting

def Speed1():
	global thirdbtnpress
	thirdbtnpress="1"
def Speed2():
	global thirdbtnpress
	thirdbtnpress="2"
def Speed3():
	global thirdbtnpress
	thirdbtnpress="3"

def GottaGo():
	finalprinter="sudo rogauracore single_breathing "+firstbtnpress+" "+secondbtnpress+" "+thirdbtnpress
	os.system(finalprinter)



'''
	Multiple Option Coontrol
	'''

def MultiColor():

	top = Toplevel()
	top.title ="Multi Colour Settings"



	fsttitle = Label(top, text="First Colour",width="25")
	fstRedbtn = Button(top, text="Red",width="25",command=FirstRed)
	fstGreenbtn = Button(top, text="Green",width="25",command=FirstGreen)
	fstBluebtn = Button(top, text="Blue",width="25",command=FirstBlue)
	fstYellowbtn = Button(top, text="Yellow",width="25",command=FirstYellow)
	fstGoldbtn = Button(top, text="Gold",width="25",command=FirstGold)
	fstCyanbtn = Button(top, text="Cyan",width="25",command=FirstCyan)
	fstMagentabtn = Button(top, text="Magenta",width="25", command=FirstMagenta)
	fstWhitebtn = Button(top, text="White",width="25",command=FirstWhite)
	fstOffbtn = Button(top, text="Off",width="25",command=FirstOff)


	sndtitle = Label(top, text="Second Colour")
	sndRedbtn = Button(top, text="Red",width="25",command=SecondRed)
	sndGreenbtn = Button(top, text="Green",width="25",command=SecondGreen)
	sndBluebtn = Button(top, text="Blue",width="25",command=SecondBlue)
	sndYellowbtn = Button(top, text="Yellow",width="25",command=SecondYellow)
	sndGoldbtn = Button(top, text="Gold",width="25",command=SecondGold)
	sndCyanbtn = Button(top, text="Cyan",width="25",command=SecondCyan)
	sndMagentabtn = Button(top, text="Magenta",width="25",command=SecondMagenta)
	sndWhitebtn = Button(top, text="White",width="25",command=SecondWhite)
	sndOffbtn = Button(top, text="Off",width="25",command=SecondOff)

	spdtitle = Label(top, text="Speed Control")
	spd1 = Button(top,text="1",width="25",command=Speed1)
	spd2 = Button(top,text="2",width="25",command=Speed2)
	spd3 = Button(top,text="3",width="25",command=Speed3)
	gobtn = Button(top,text="Go", width="25",command=GottaGo)

	fsttitle.grid(row=0,column=0)
	fstRedbtn.grid(row=1,column=0)
	fstGreenbtn.grid(row=2,column=0)
	fstBluebtn.grid(row=3,column=0)
	fstYellowbtn.grid(row=4,column=0)
	fstGoldbtn.grid(row=5,column=0)
	fstCyanbtn.grid(row=6,column=0)
	fstMagentabtn.grid(row=7,column=0)
	fstWhitebtn.grid(row=8,column=0)
	fstOffbtn.grid(row=9,column=0)


	sndtitle.grid(row=0,column=1)
	sndRedbtn.grid(row=1,column=1)
	sndGreenbtn.grid(row=2,column=1)
	sndBluebtn.grid(row=3,column=1)
	sndYellowbtn.grid(row=4,column=1)
	sndGoldbtn.grid(row=5,column=1)
	sndCyanbtn.grid(row=6,column=1)
	sndMagentabtn.grid(row=7,column=1)
	sndWhitebtn.grid(row=8,column=1)
	sndOffbtn.grid(row=9,column=1)

	spdtitle.grid(row=0,column=2)
	spd1.grid(row=1,column=2)
	spd2.grid(row=2,column=2)
	spd3.grid(row=3,column=2)
	gobtn.grid(row=9,column=2)




'''

	Initial Buttons AKA Driver Code


	'''
ButStat = Button(root, text="Static Colour", width = "25", command = StaticColour )
ButMulti = Button(root, text="Multiple Colour", width = "25", command=MultiColor)
ButBright = Button(root, text="Brightness Control", width = "25", command= BrightnessControl)
ButQuit = Button(root, text="Quit", width = "25",bg = "#a9a9a9", fg="white", command = root.quit)

ButStat.grid(row=0,column=0)
ButMulti.grid(row=1,column=0)
ButBright.grid(row=2,column=0)
ButQuit.grid(row=3,column=0)



root.mainloop()
