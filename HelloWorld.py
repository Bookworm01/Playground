
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
if (Q1A == "B" or Q1A == "b"):
    print ("Great, B! Next question.")
if (Q1A == "C" or Q1A == "c"):
	print ("Great, C! Next question.")
if (Q1A == "D" or Q1A == "d"):
	print ("Great, D! Next question.")






