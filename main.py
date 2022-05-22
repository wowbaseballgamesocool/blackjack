import pygame, time, random
from pygame import mixer
pygame.init()
mixer.init()
pygame.display.set_caption('Blackjack')
screen = pygame.display.set_mode((1000, 600))
cards = ['AD', 'AS', 'AC', 'AH', 'KD', 'KS', 'KC', 'KH', 'QS', 'QC', 'QH', 'QD', 'JD', 'JS', 'JC', 'JH', '10D', '10S', '10C', '10H', '9D', '9S', '9C', '9H', '8D', '8S', '8C', '8H', '7D', '7S', '7C', '7H', '6D', '6S', '6C', '6H', '5D', '5S', '5C', '5H', '4D', '4S', '4C', '4H', '3D', '3S', '3C', '3H', '2D', '2S', '2C', '2H', '1D', '1S', '1C', '1H']


while True:
    



    
    
    
    for event in pygame.event.get():
			
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE: exit()
		#if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if event.type == pygame.QUIT: exit()

    while blackjack: pass

