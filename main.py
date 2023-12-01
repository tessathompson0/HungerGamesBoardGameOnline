#Tessa, Callie, Kendle

#import stuff
import pygame
import random

#initialize pygame
pygame.init()

#set up constants
width, height = 1600, 1200
rows, columns = 10, 10
gameTiles = height//rows

#colors
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

#create the board
gameBoard = [[0 for i in range(columns)] for i in range(rows)]

#set up window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hunger Games Board Game Online")

#draw the board
def displayBoard():
    #make background white
    window.fill(white)
    for j in range(rows):
        for k in range(columns):
            pygame.draw.rect(window, red, (k * gameTiles, j * gameTiles, gameTiles), 1)
#display text
def displayText(text, x, y, color = black, size = 30):
    font = pygame.font.SysFont(None, size)
    text = font.render(text, True, color)
    window.blit(text, (x,y))

#display dice
def displayDice(dice1, dice2):
    pygame.draw.rect(window, black, (width - 200, height - 200, 100, 100))
    pygame.draw.rect(window, black, (width - 80, height - 200, 100, 100))
    draw_text(f"Dice 1: {dice1}",width-190,height-180)
    draw_text(f"Dice 2: {dice2}",width-190,height-180)

#ask user for number of players (7 max)
numberOfPlayers = int(input("Enter the number of players who will be playing this game (minimum of 2 players and a maximum of 7 players)"))
#if user puts less than 2 or more then 7
if numberOfPlayers < 2 or numberOfPlayers > 7:
    pygame.quit()
    exit()

nameOfPlayers = []
for i in range(numberOfPlayers):
    