from time import sleep
import sys
import random

flower = ["love you", "need you", "want you", "want to kiss you",
 "miss you", "want to hug you", "really really love you", "respect you",
 "adore you", "can do anything for you", "can fight for you",
  "put you on my first priority", "think about you as soon as I wake up",
   "look out for you", "care for you"]


def sp(str):
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		sleep(0.1)
		
while True:
	sp("Vartika I ")
	x = random.choice(flower)
	sp(x)
	sp(" ❤️ ^_^ <3 ")
	sleep(1)
	print("\n")