import sys
import time

def sp(str):
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.1)
	
def decision():
	x=True
	while x == True:
		dec=input()
		dec=int(dec)
		if dec == 1 or dec == 2:
			sp("Alright!")
			x=False
			return dec
		else:
			sp("Sorry babe wrong choice! Enter again!")
			print()
			
def statement():
	print("\n")
	sp("Vartika do you still love Sankalp? :")
	print()
	sp("Enter 1 for Yes and 2 for No")
	print()
	
sp("Vartika do you love Sankalp? :")
print()
sp("[+] 1 Yes.")
print()
sp("[+] 2 No.")
print()
sp("$ Only Enter 1 or 2")
print()

i=1
run=True
while run==True:
	a=decision()
	if a == 1:
		i+=1
		print("\n")
		sp("Aww that's cute but Sankalp loves you ")
		print(i, end ='')
		sp(" times more than you!")
		statement()
	
	if a == 2:
		print("\n")
		sp("Huhh!! That's not an option you must Enter 1! :( But as you say so, this program is going to terminate :'( but you can always run it again")
		print("\n")
		sp("Btw Sankalp loved you ")
		print(i, end='')
		sp(" times more than you. Bye I'm gonna cry now, Vartika don't love me anymore")
		print("\n\n")
		run=False