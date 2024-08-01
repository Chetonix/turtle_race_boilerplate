from turtle import Turtle, Screen
import random

#define a list of 7 colors
colors = []
y_positions = [90, 60, 30, 0, -30, -60, -90]
all_turtles = []
game_on = False

screen = Screen()
screen.setup(500, 400)

user_bet = screen.textinput(title="Make a bet",
                            prompt="Whick turtle is gonna win the race?: ")

if user_bet:
  game_on = True

#Start a for loop and inititate each turtle object, lift pen up and make them goto (-230, y_positions[index]), then assign a color from colors array and append each turtle in all_turtles empty list
#code below:

while game_on:
  #for each turtle in all_turtles:
  
    #if turtle.xcor() > 230
    
      #game_on = False
      #assign winnig_turtle the pen color of the turtle
      

      #if winning_turtle == user_bet:
      if winning_turtle == user_bet:
        #print a winning message
        
      #else:
        #print a lost message
        
    #move turtle forward by 0 to 10 
    
