
import sys
from time import *

print(sys.version)

print ("This is a quiz that will sort you into your Hogwart's house.")
sleep(3)
print ("Please answer each question truthfully, so we can give you the most accurate answer.")
sleep(4)
print ("Which path do you take: ")
sleep(2)
print ("A) A path by the river ")
sleep(1)
print ("B) A path in the forest ")
sleep(1)
print ("C) A path in the desert ")
sleep(1)
print ("D) A path in the meadow ")
sleep(1)
Q1A = input("Please type A, B, C, or D here: ")

if (Q1A == "A" or Q1A == "a"):
    print ("Great, A! Next question.")
    sleep(1)
if (Q1A == "B" or Q1A == "b"):
    print ("Great, B! Next question.")
    sleep(1)
if (Q1A == "C" or Q1A == "c"):
	print ("Great, C! Next question.")
	sleep(1)
if (Q1A == "D" or Q1A == "d"):
	print ("Great, D! Next question.")
	sleep(1)


print ("You are given four potions. Which do you pick?")
sleep(2)
print ("A) A potion to make you know everything ")
sleep(1.3)
print ("B) A potion to help as many people as possible ")
sleep(1.5)
print ("C) A potion that gives you infinate power ")
sleep(1.3)
print ("D) A potion that lets you do what you want to do ")
sleep(1.4)
Q2A = input("Which do you pick? Answer here using A, B, C, or D: ")

if (Q2A == "A" or Q2A == "a"):
	print ("Nice choice! Next question. ")
	sleep(1)
if (Q2A == "B" or Q2A == "b"):
	print ("Nice choice! Next question. ")
	sleep(1)
if (Q2A == "C" or Q2A == "c"):
    print ("Nice choice! Next question. ")
    sleep(1)
if (Q2A == "D" or Q2A == "d"):
    print ("Nice choice! Next question.")  
    sleep(1)


print ("If you could do one of the following, which would you do?")
sleep(2)
print ("A) Read a book for four hours, completely uninterrupted ")
sleep(1.5)
print ("B) Go on a survival skill building camping trip ")
sleep(1.5)
print("C) Gossip with your friends ")
sleep(1.5)
print ("D) Study for your upcoming test ")
Q3A = input("A, B, C, or D: ")

if (Q3A == "A" or Q3A == "a"):
	print ("A is a good answer. Next! ")
	sleep(1)
if (Q3A == "B" or Q3A == "b"):
	print ("B is a good answer. Next! ")
	sleep(1)
if (Q3A == "C" or Q3A == "c"):
	print ("C is a good answer. Next! ")
	sleep(1)
if (Q3A == "D" or Q3A == "d"):
	print ("D is a good answer. Next! ")
	sleep(1)


