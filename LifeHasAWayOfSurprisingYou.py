import turtle 
from random import getrandbits as lifeHappens
from turtle import circle as lifeGoesOn
turtle.hideturtle()
turtle.speed(0)
turtle.bgcolor("black")
turtle.color("white")



######################################
#                                    #
#  Life has a way of surprising you  #
#  by Andie Labgold                  #
#                                    #
######################################


alive = True
youKnowWhatLifeHasInStore = False

while (alive):
    if youKnowWhatLifeHasInStore == True:
        lifeGoesOn(-7, 30, 100)
        youKnowWhatLifeHasInStore = False
    else:
        lifeGoesOn(7, 30, 100)
        youKnowWhatLifeHasInStore = lifeHappens(1)
        
