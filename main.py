import pygame, time, random
from pygame import mixer
pygame.init()
mixer.init()
pygame.display.set_caption('Blackjack')
screen = pygame.display.set_mode((1000, 600))
cardslist = ['A', 'A', 'A', 'A', 'K', 'K', 'K', 'K', 'Q', 'Q', 'Q', 'Q', 'J', 'J', 'J', 'J', '10', '10', '10', '10', '9', '9', '9', '9', '8', '8', '8', '8', '7', '7', '7', '7', '6', '6', '6', '6', '5', '5', '5', '5', '4', '4', '4', '4', '3', '3', '3', '3', '2', '2', '2', '2', '1', '1', '1', '1']
blackjack = True

while True:
    



    
    
    
    for event in pygame.event.get():
			
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE: exit()
		#if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if event.type == pygame.QUIT: exit()

    while blackjack:
        shuffledcards = random.sample(cardslist, len(cardslist))
        playercards = [shuffledcards[0], shuffledcards[1]]
        playercount = 0
        try:
            playercount += int(shuffledcards[0])
        except:
            if shuffledcards[0] in "KQJ": playercount += 10
            elif shuffledcards[0] in "A":
                if playercount + 11 > 21: playercount += 1
                else: playercount += 11
            
        try:
            playercount += int(shuffledcards[1])
        except:
            if shuffledcards[1] in "KQJ": playercount += 10
            elif shuffledcards[1] in "A":
                if playercount + 11 > 21: playercount += 1
                else: playercount += 11
        if shuffledcards[0] == "A" and shuffledcards[1] == "A": playercount = 21
        print(str(playercards) + "" + str(playercount))
        
        

