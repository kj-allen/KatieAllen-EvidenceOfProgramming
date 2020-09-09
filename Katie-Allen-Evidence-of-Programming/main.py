print("Hello, earthlings.")

if 5 > 2:
  print("Five is greater than two.")

#This is a test comment

x = "Hello there. "
y = "GeNeRaL kEnObI"
z = x + y
print(z)

"""
This is a
comment written
in more than
one line
"""

a = b = c = "oranges"
print(a)
print(b)
print(c)

#This is the start of a text based game
import time

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]

required = ("\nOnly use A, B, or C\n")

def intro():
  print ("You're cosy in bed but it's time to go to work. The weather outside if frightful, and the warmth of the duvet is so delightful. Do you:")
  time.sleep(1)
  print ("""  A. Pull the duvet to your neck and snuggle back to sleep
  B. Run to the bathroom and immediately turn on the shower to warm up
  C. Embrace the cold and start getting ready for work""")
  choice = input(">>> ") #Here is your first choice.
  if choice in answer_A:
    print ("\nYou snuggle back up into the duvet like a cozy burrito. "
		"\n\nEight hours later you wake up to thirty missed calls from your manager and a text stating you're fired. "
		"\n\n\nUh-oh. Shouldn't have given in to the warmth!")
  elif choice in answer_B:
    print ("\nYour shower was too hot and you burnt your back. "
    "\n\nYou have to go to the hospital!")
  elif choice in answer_C:
    print ("\nYou're the only one who made it into the office today. "
    "\n\nYour manager was so impressed he offered you a promotion. "
		"\n\n\nCongratulations!")
  else:
    print (required)

intro()
