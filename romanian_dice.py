# Classes to import
import random
import pygame as pg

import sys

from player import Player
from die import Die
from settings import Settings
from buttons import Buttons

import rd_game_functions as gf

# Main file for romainian dice
continueGame = True
current_player = Player()
rd_settings = Settings()		

			
###############################################################################
# Start of the game 
###############################################################################

pg.init()
pg.font.init()

clock = pg.time.Clock()
screen = pg.display.set_mode((rd_settings.scrWidth, rd_settings.scrHeight))
pg.display.set_caption("Romanian Dice Simulator")

putin = pg.image.load('images/putin_8bit_final.png')

blankDie = pg.image.load('images/blankDie.png').convert()
eightBit = pg.font.Font('images/8bit.ttf', 128)

chatBit = pg.font.Font('images/8bit.ttf', 64)


start_button = Buttons(rd_settings, screen, "Start")

die_1 = Die()

###############################################################################
# Main Game Loop
###############################################################################


while continueGame:
	
	gf.checkForEvents(rd_settings, screen, start_button)
	
	screen.fill(rd_settings.bg_color)
	
	#This draws the intro screen until the user hovers over the start
	if rd_settings.start_clicked == False:
		gf.introPutin(screen, putin, blankDie, eightBit, rd_settings)

	#This starts the actual game
	else:
		screen.blit(putin, (850,175))
		
		#draw the chat area
		pg.draw.rect(screen, (0,0,0), (25,550,900,200)) 
		pg.draw.rect(screen, (255,255,255), (35,560,880,180)) 
		
		if rd_settings.playerKnowsGame == False:
			gf.doesPlayerKnowGame(screen,rd_settings, chatBit)
			
	pg.display.flip()
	
	clock.tick(rd_settings.FPS)
