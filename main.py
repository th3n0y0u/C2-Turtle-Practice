import turtle, time

# Ask the user how many sides they want
while(True):
  userInput = int(input("How many sides do you want noob"))
  if(userInput >= 3 and userInput <= 10):
    for i in range(userInput):
      turtle.forward(50)
      turtle.right(360 / userInput)
    time.sleep(3)
    turtle.clear()
  else:
    print("shut you nerd")