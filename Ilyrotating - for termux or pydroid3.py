import os
from time import sleep

def start():
	i=1
	while i<40:
	   print("I love you Vartika")
	   i+=1
	   sleep(0.1)
	   os.system('clear')
	   print("\n"*i)
	   
	j=1
	while j<40:
	   print("I love you Vartika")
	   j+=1
	   sleep(0.1)
	   os.system('clear')
	   print("\n"*i)
	   print(" "*j,end="")
	   
	k=1
	t=40
	while k<40:
	   print("I love you Vartika")
	   k+=1
	   sleep(0.1)
	   os.system('clear')
	   print("\n"*t)
	   t-=1
	   print(" "*j,end="")
	   
	x=1
	y=40
	while x<40:
	   print("I love you Vartika")
	   x+=1
	   sleep(0.1)
	   os.system('clear')
	   print(" "*y,end="")
	   y-=1
	   

while True:
	start()
	os.system('clear')
	print("\n"*20)
	print(" "*20,end="")
	print("Baby I really love you!")
	sleep(2)
	os.system('clear')