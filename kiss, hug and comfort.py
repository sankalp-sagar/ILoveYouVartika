import random
import sys
import time
import threading
import itertools
import webbrowser
from twilio.rest import Client

#This is a game for my girlfriend Vartika
#Created by : Sankalp Sagar
#Facebook : facebook.com/sankalp.sagar.315
#Instagram : instagram.com/sankalp_sagar_

#Get yourself registered on twilio.com and get a free phone number and then get your own ssid and auth token from there, mine currently doesn't work now and change the names

sid = 'your twilio ssid here'
token = 'your twilio auth'

tome = Client(sid, token)

def sp(stri):
	for letter in stri:
		print(letter, end="")
		sys.stdout.flush()
		time.sleep(0.1)
		
players = ["Sankalp", "Vartika"]
sscore = 0
vscore = 0

def animate():
	for c in itertools.cycle(['|', '/', '-', '\\']):
		if done:
			break
		sys.stdout.write('\rSankalp is Thinking :  ' + c)
		sys.stdout.flush()
		time.sleep(0.1)
	
def anim():
	global done
	done = False
	t = threading.Thread(target=animate)
	t.start()
	time.sleep(1)
	done = True
	
def whowon(vturn, sturn, playerslist):
	print("\033[1;31;40m", end = "")
	if vturn == "kiss" and sturn == "hug":
		sp("Kiss defeats Hug, Vartika won")
		print()
		sp("Now Sankalp is Hugging Vartika ^_^ <3")
		print("\033[1;33;41m\n")
		sp("Sankalp : Vartika tumko Hug kr rha hu paas me aao (⊃｡•́‿•̀｡)⊃")
		print("\n")
		
	if vturn == "kiss" and sturn == "comfort":
		sp("Comfort defeats Kiss, Sankalp won")
		print()
		sp("Now Vartika is Kissing Sankalp ^_^ <3")
		print("\033[1;33;41m\n")
		sp("Vartika : Sankalp mai tumko Kiss kr rhi hu 😘😘😘")
		webbrowser.open("http://wa.me/91yournumber?text=😘😘😘I+kiss+you+baby", new = 0)
		print("\n")
		
	if vturn == "kiss" and sturn == "kiss":
		sp("Both selected Kiss..!!")
		print()
		sp("Now both are kissing each other ^_^ <3")
		print("\033[1;33;41m\n")
		sp("Their Kissing Sound : Mmmmwwwwwwwaaaaaaaaahhhhhhhhhhhhh😘")
		print("\n")
		
	if vturn == "hug" and sturn == "kiss":
		sp("Kiss defeats Hug, Sankalp won")
		print()
		sp("Now Vartika is Hugging Sankalp <3")
		print("\033[1;33;41m\n")
		sp("Vartika : Sankalp tumko Hug kr rhi hu paas me aao (⊃｡•́‿•̀｡)⊃")
		webbrowser.open("http://wa.me/91yournumber?text=😘😘😘I+hug+you+baby", new = 0)
		print("\n")
		
	if vturn == "hug" and sturn == "hug":
		sp("Both selected Hug!")
		print()
		sp("Now Both are hugging each other ^_^ <3")
		print("\033[1;33;41m\n")
		sp("Both be like : (⊃｡•́‿•̀｡)⊃ ⊂(｡•́‿•̀｡⊂)")
		print("\n")
		
	if vturn == "hug" and sturn == "comfort":
		sp("Hug defeats Comfort, Vartika won")
		print()
		sp("Now Sankalp is Comforting Vartika ^_^ <3")
		print("\033[1;33;41m\n")
		sp("Sankalp : Vartika tum mere liye bht mayene rkhti ho Ilysm! =]")
		print("\n")
		
	if vturn == "comfort" and sturn == "kiss":
		sp("Comfort defeats Kiss, Vartika won")
		print()
		sp("Now Sankalp is Kissing Vartika ^_^ <3")
		print("\033[1;33;41m\n")
		sp("Sankalp : Vartika tumko slowly Kiss kr rha hu close aao(っ＾3＾)っ～♡")
		print("\n")
		
	if vturn == "comfort" and sturn == "hug":
		sp("Hug defeats Comfort, Sankalp won")
		print()
		sp("Now Vartika is Comforting Sankalp ^_^ <3")
		print("\033[1;33;41m\n")
		sp("Vartika : Sankalp tum mere liye sb kuch ho I love you (✿ ♡‿♡)")
		webbrowser.open("http://wa.me/91yournumber?text=😘😘😘I+love+you+so+much+baby+I+will+love+you+forever", new = 0)
		print("\n")
		
	if vturn == "comfort" and sturn == "comfort":
		sp("Both chose to Comfort!")
		print()
		sp("Now they both are Comforting each other ^_^ <3")
		print("\033[1;33;41m\n")
		sp("They both are holding each other's hands and promising to love each other till eternity (✿ ♡‿♡)")
		print("\n")


def fixwon(vturn, sturn, playerlist):
	score = []
	if vturn == "kiss" and sturn == "hug":
		score = [1,0]
		
	if vturn == "kiss" and sturn == "comfort":
		score = [0,1]
		
	if vturn == "kiss" and sturn == "kiss":
		score = [0,0]
		
	if vturn == "hug" and sturn == "kiss":
		score = [0,1]
		
	if vturn == "hug" and sturn == "hug":
		score = [0,0]
		
	if vturn == "hug" and sturn == "comfort":
		score = [1,0]
		
	if vturn == "comfort" and sturn == "kiss":
		score = [1,0]
		
	if vturn == "comfort" and sturn == "hug":
		score = [0,1]
		
	if vturn == "comfort" and sturn == "comfort":
		score = [0,0]
		
	return score
		
def vchoice(list):
		x = input().lower()
		if x == "sex":
			print("\033[0;31;47m")
			tome.messages.create(body="Hurray! Vartika just chosen to have the process with you! The best part is, she chose all by herself! Ab to Sankalp k balle balle hogye kyuki lipta lipti hogi ab!", from_="twilionumber", to="+91yournumber") #Replace twilio number and yournumber
			sp("Wooowwww😍😍😍itne saare options me se 🥰🥰 tumne sex chuna jo ki diya bhi nahii hua tha😍😍 Hayeeee I Loveee youu soo Much ❣️❣️🤭 Haan mjhe bhi krna hai tumhaare sath sex 😘😘😍 Hard vala krna haii☺️☺️🤭 Ab game chhodo🤭 chalo saath me kahi lipta lipti krne 😍😍🥰")
			print("\n")
			sp("VARTIKA AND SANKALP BOTH WON! GAME OVER")
			print("\033[1;37;40m\n")
			webbrowser.open("http://wa.me/91yournumber?text=Sankalp🤭🤭+mai+tumhaare+saath+hard+vala+sex+krna+chahti+hu😍+ye+mere+man+ki+bhaavnayein+hai+asli🤭🤭😘😘😘", new = 0)
			exit(0)
		while x not in list:
			sp("Darling! It's a wrong choice! Enter Again : ")
			print()
			x = input()
		return x
		
	
print("\033[1;33;40m", end = "")
sp("Hey Vartika do you wanna play Kiss, Hug and Comfort?")
print("\033[1;32;40m")
sp("[+] Press 1 for Yes")
print("\033[1;31;40m")
sp("[+] Press 2 for No")
print("\033[1;34;40m")
c = int(input())
if c == 1:
	pass
if c == 2:
	sp("Vartika don't want to play with me! I am hurt and going to cry now")
	exit(1)
if c > 2 or c < 1:
	sp("Wrong choice baby! Run the program again!")
	exit(1)
	
sp("Okay you want to play <3 so here are the rules:")
print()
print()
sp("This is a game in which we have 3 choices, namely Kiss, Hug and Comfort and we have to choose one for the other.")
print()
print("\033[1;31;40m")
sp("Kiss defeats Hug <3")
print()
sp("Hug defeats Comfort =D")
print()
sp("Comfort defeats Kiss ^_^")
print()
print("\033[1;33;40m")
sp("If one defeats the other then the loser will have give what he/she chose to the winner and if they choose the same, they have to do it")
print("\n")
sp("The one who scores 10 points 1st will win")
print()
sp("[+] Enter 'start' to play the game")
print("\033[1;31;40m")
star = input()

while star != "start":
	sp("Hey baby! Its's a wrong choice, please enter again!")
	print()
	star = input()
	
moves = ["kiss", "hug", "comfort"]

run = True
print()
sp("Here we go....!!")
print("\n\n")
print()

while run:
	print("\033[1;36;40m", end = "")
	sp("Vartika : Kiss, Hugs or Comfort? : ")
	var = vchoice(moves)
	schoice = random.choice(moves)
	print("\033[1;32;40m\n")
	sp("Vartika chose : ")
	sp(var.title())
	print("\033[1;33;40m")
	anim()
	print("\n")
	sp("Sankalp chose : ")
	sp(schoice.title())
	print("\n")
	whowon(var, schoice, players)
	sco = fixwon(var, schoice, players)
	vscore += sco[0]
	sscore += sco[1]
	print("\033[1;35;40m")
	sp("Vartika's Score : ")
	sp(str(vscore))
	print("\n")
	sp("Sankalp's Score : ")
	sp(str(sscore))
	print("\n\n")
	if vscore >= 10:
		print("\033[0;31;47m")
		sp("Baabbbyyy tum jeet gayiii, haha mjhe pata tha tum hi jeetogi jaan <3 accha vse sach batau to mjhe kiss ka zyaada man tha. Ab krne do tumhaare lips par softly or slowly tumhaari breathing rhythm me dhalte hue 😘😘😘")
		print("\n\n")
		sp("VARTIKA WON! GAME OVER")
		run = False
		
	if sscore >= 10:
		print("\033[0;31;47m")
		sp("Baabbbyyy dekho dekho mai jeet gaya hu! Haha vse chahta tha ki tum jeeto lekin ab mai jeet gya to fayeda utha leta hu zra, jaldi se ek deep vali kiss send krdo mere whatsapp par explain krke 😘😘😘")
		webbrowser.open("http://wa.me/91yournumber?text=Sankalp+mai+tumko+paas+me🥰+apne+hontho+k+bht+kareeb+tumko+laa+kar😍😍+tumhaare+hontho+ko+softly+apne+hontho+se+touch☺️+kr+rhi+hu+lagataar🤭+bht+der+tak😘😘", new = 0)
		print("\n\n")
		sp("SANKALP WON! GAME OVER")
		run = False
		
print("\033[1;37;40m\n")
