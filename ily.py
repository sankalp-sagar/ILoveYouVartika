from time import sleep
def i():
	for i in range(1,8):
		if i == 1 or i == 7:
			for j in range(1,8):
				print("❤️",end='')
				
		else:
			for j in range(1,8):
				if j == 7:
					print("❤️",end='')
				else:
					print(" ",end='')
		print("")

def l():
	for i in range(1,8):
		if i == 7:
			for j in range(1,8):
				print("❤️",end='')
		else:
			print("❤️")
			
def u():
	for i in range(1,8):
		for j in range(1,8):
			if i == 7:
				print("❤️",end='')
			else:
				if j == 1 or j == 7:
					print("❤️",end='')
				else:
					print("  ",end='')
		print()

i()
print()
sleep(1)
l()
print("\n")
sleep(1)
u()