## Tick Tock ###################################################################
## gotta check that HCM ########################################################
################################################################################

from Tkinter import *
import time

import datetime

from sys import argv
	
	
def printHeading(title):
	print "==" + title + "=="	
	
def secondsOnTheDay():
	secs = datetime.datetime.now().time().second
	secs += datetime.datetime.now().time().minute*60
	secs += datetime.datetime.now().time().hour*3600		
	return secs	
		
def sendReminder(prompt):
	root = Tk()
	w = Label(root, text=prompt)
	w.pack()
	root.wm_attributes("-topmost", 1)	
	root.mainloop()
	return
		
def formatTime(h, m, s):
	output = "foo"
	## better not reach the end like this
	if(m <= 9):
		if(s <= 9):
			output = "%i:0%i:0%i" % (h, m, s);
		else:
			output = "%i:0%i:%i" % (h, m, s);			
	else:
		if(s <= 9):
			output = "%i:%i:0%i" % (h, m, s);
		else:
			output = "%i:%i:%i" % (h, m, s);
		
	return output;
	## that wasnt too bad
		

def weekDay():
	output = datetime.datetime.today().weekday();
	return output;
	## 0 to 7, 0 is monday I guess?
	
def Focus():
	root = Tk()
	root.wm_attributes("-topmost", 1)	
	root.after(1000, lambda: root.focus_force())
	root.mainloop()
	
def Startup(title, message):
	sys.stdout.write("\x1b[2J\x1b[H");
	print ("==" + title + "==\n");
	print (message);
	return

def percentageOf(value , in_range):
	## look Im busy, not all code is going to make sense
	return 100*value/in_range

def upTime(start_time, uptime, downtime):
	sys.stdout.write("\x1b[2J\x1b[H");
	secondTicked = 1
	while(secondsOnTheDay() < (start_time + uptime)):
		delta = secondsOnTheDay() - start_time
		if(delta > secondTicked):

			secondTicked += 1
			sys.stdout.write("\x1b[2J\x1b[H");
			printHeading("upTime")
			print "\nUP   -", formatTime(datetime.datetime.now().time().hour,\
							datetime.datetime.now().time().minute, \
							datetime.datetime.now().time().second)
			percent = percentageOf(delta, uptime)
			print "[","*"*(percent), " "*(100-percent),"]"
		
	downTime(secondsOnTheDay(), uptime, downtime)
	
def downTime(start_time, uptime, downtime):
	sys.stdout.write("\x1b[2J\x1b[H");
	secondTicked = 1
	while(secondsOnTheDay() < (start_time + downtime)):
		delta = secondsOnTheDay() - start_time
		if(delta > secondTicked):

			secondTicked += 1
			sys.stdout.write("\x1b[2J\x1b[H");
			printHeading("downTime")
			print "\nDOWN -", formatTime(datetime.datetime.now().time().hour,\
							datetime.datetime.now().time().minute, \
							datetime.datetime.now().time().second)
			percent = percentageOf(delta, uptime)
			print "[","*"*(percent), " "*(100-percent),"]"
		
	upTime(secondsOnTheDay(), uptime, downtime)		

if(__name__ == "__main__"):
	script, minutes_up, minutes_down = argv
	startingIn = 5
	Startup("TickTock", "Running TickTock with arguments %d minutes up, %d minutes down starting in %d seconds" % (int(minutes_up), int(minutes_down), int(startingIn)))


	
	goTime = secondsOnTheDay()
	secondTicked = 1
	while(secondsOnTheDay() < goTime + startingIn):
		delta = secondsOnTheDay() - goTime
		##print delta, secondTicked
		if(delta > secondTicked):

			secondTicked += 1
			sys.stdout.write("\x1b[2J\x1b[H");
			Startup("TickTock", "Running TickTock with arguments %d minutes up, %d minutes down starting in %d seconds" % (int(minutes_up), int(minutes_down), int(startingIn)))
			print "*"*secondTicked
	upTime(secondsOnTheDay(), int(minutes_up)*60, int(minutes_down)*60)
