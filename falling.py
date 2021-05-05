import sys
import time
import os

def Sankalp(n):
	me = [[" ", "O"], [" ", "|"], ["\\", " ", "/"], [" ", "|"], [" ", "|"], ["/", " ", "\\"]]
	
	for i in me:
		print("".join(i))
		time.sleep(n)
		
def sp(str):
	for letter in str:
		print(letter, end ="")
		sys.stdout.flush()
		time.sleep(0.1)
		
def Sankalpp(n):
	me = [[" ", "O"], [" ", "|"], ["\\", " ", "/"], [" ", "|"], [" ", "|"], ["/", " ", "\\"]]
	
	for i in me:
		print("".join(i), end = "")
		time.sleep(n)
		
print("\033[1;32;40m", end ="")
sp("This is Sankalp")
print("\033[1;33;40m")
time.sleep(0.1)
Sankalp(0.1)
time.sleep(1)


print("\033[1;31;40m\n"*35)
for i in range(1,8):
	sp("VARTIKA ")

time.sleep(0.1)

os.system('cls')

print("\n"*20)
print("\033[1;34;40m "*8, end = "")
sp("NOW SANKALP STARTS FALLING TOWARDS VARTIKA")
time.sleep(1)

os.system('cls')

for i in range(1,35):
	print("\033[1;33;40m", end = "")
	print("\n"*i)
	Sankalp(0.1)
	print("\033[1;31;40m\n"*(34-i))
	print("VARTIKA "*7)
	time.sleep(1)
	if i == 34:
		time.sleep(2)
	os.system('cls')
	
print("\033[1;34;40m", end ="")
print("\n"*18)
print(" "*12, end = "")
sp("THIS IS HOW HE MADE HER LIKE HIM")
print()
print(" "*6, end = "")
sp("SHE FELL FOR HIM AND LOVING HIM SINCE THAT DAY")
print()
print(" "*6, end = "")
sp("ALSO SANKALP LOVES VARTIKA VERY MUCH EVERYDAY")
time.sleep(3)
print("\033[1;37;40m\n"*30)