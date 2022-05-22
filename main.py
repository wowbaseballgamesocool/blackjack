import pygame, time, random
from pygame import mixer
pygame.init()
mixer.init()
cardslist = ['A', 'A', 'A', 'A', 'K', 'K', 'K', 'K', 'Q', 'Q', 'Q', 'Q', 'J', 'J', 'J', 'J', '10', '10', '10', '10', '9', '9', '9', '9', '8', '8', '8', '8', '7', '7', '7', '7', '6', '6', '6', '6', '5', '5', '5', '5', '4', '4', '4', '4', '3', '3', '3', '3', '2', '2', '2', '2']
deadcards = []
blackjack = True
pygame.display.set_caption('Blackjack')
screen = pygame.display.set_mode((1000, 675))
# = pygame.transform.scale(, (95, 30))
med_font = pygame.font.SysFont("Mochiy Pop One", 30)
font_style = pygame.font.SysFont("Mochiy Pop One", 50)
small_font = pygame.font.SysFont("Mochiy Pop One", 20)
big_font = pygame.font.SysFont("Mochiy Pop One", 40)
verybig_font = pygame.font.SysFont("Algerian", 70)
menustarttext = verybig_font.render("START", True, [0, 0, 0])
menuoptionstext = verybig_font.render("OPTIONS", True, [0, 0, 0])
menuexittext = verybig_font.render("EXIT", True, [0, 0, 0])




cards = [
    pygame.transform.scale(pygame.image.load('assets/cards/A.png').convert_alpha(), (121, 199)),
    pygame.transform.scale(pygame.image.load('assets/cards/K.png').convert_alpha(), (121, 199)),
    pygame.transform.scale(pygame.image.load('assets/cards/2.png').convert_alpha(), (121, 199)),
    pygame.transform.scale(pygame.image.load('assets/cards/3.png').convert_alpha(), (121, 199)),
    pygame.transform.scale(pygame.image.load('assets/cards/4.png').convert_alpha(), (121, 199)),
    pygame.transform.scale(pygame.image.load('assets/cards/5.png').convert_alpha(), (121, 199)),
    pygame.transform.scale(pygame.image.load('assets/cards/6.png').convert_alpha(), (121, 199)),
    pygame.transform.scale(pygame.image.load('assets/cards/7.png').convert_alpha(), (121, 199)),
    pygame.transform.scale(pygame.image.load('assets/cards/8.png').convert_alpha(), (121, 199)),
    pygame.transform.scale(pygame.image.load('assets/cards/9.png').convert_alpha(), (121, 199)),
    pygame.transform.scale(pygame.image.load('assets/cards/10.png').convert_alpha(), (121, 199)),
    pygame.transform.scale(pygame.image.load('assets/cards/Q.png').convert_alpha(), (121, 199)),
    pygame.transform.scale(pygame.image.load('assets/cards/J.png').convert_alpha(), (121, 199))
]

menu = pygame.image.load('assets/menu.png').convert_alpha()





def placecards(card, x, y):
    try:
        screen.blit(cards[int(card)], [x, y])
    except: 
        if card == "A": screen.blit(cards[0], [x, y])
        elif card == "K": screen.blit(cards[1], [x, y])
        elif card == "Q": screen.blit(cards[11], [x, y])
        elif card == "J": screen.blit(cards[12], [x, y])
        else: raise Exception("Could not display unknown card")


def totalcards(card1, card2, card3, card4, card5):
    playercount = 0
    try:
        playercount += int(card1)
    except:
        if card1 in "KQJ": playercount += 10
        elif card1 in "A":
            if playercount + 11 > 21: playercount += 1
            else: playercount += 11
    try:
        playercount += int(card2)
    except:
        if card2 in "KQJ": playercount += 10
        elif card2 in "A":
            if playercount + 11 > 21: playercount += 1
            else: playercount += 11
    try:
        playercount += int(card3)
    except:
        if card3 in "KQJ": playercount += 10
        elif card3 in "A":
            if playercount + 11 > 21: playercount += 1
            else: playercount += 11
    try:
        playercount += int(card3)
    except:
        if card3 in "KQJ": playercount += 10
        elif card3 in "A":
            if playercount + 11 > 21: playercount += 1
            else: playercount += 11
    try:
        playercount += int(card4)
    except:
        if card4 in "KQJ": playercount += 10
        elif card4 in "A":
            if playercount + 11 > 21: playercount += 1
            else: playercount += 11
    try:
        playercount += int(card5)
    except:
        if card5 in "KQJ": playercount += 10
        elif card5 in "A":
            if playercount + 11 > 21: playercount += 1
            else: playercount += 11
        

    if shuffledcards[0] == "A" and shuffledcards[1] == "A": playercount = 21
    return playercount





while True:
    screen.blit(menu, [0, 0])
    screen.blit(menustarttext, [20, 100])
    screen.blit(menuoptionstext, [20, 190])
    screen.blit(menuexittext, [20, 280])
    
    
    
    pygame.display.update()
    time.sleep(9)


    
    
    
    for event in pygame.event.get():
			
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE: exit()
		#if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if event.type == pygame.QUIT: exit()

    while blackjack:
        screen.fill([0, 0, 0])
        shuffledcards = random.sample(cardslist, len(cardslist))
        playercards = [shuffledcards[0], shuffledcards[1]]
        playercount = 0
        
        playercount = totalcards(shuffledcards[0], shuffledcards[1], 0, 0, 0)
        dealercount = totalcards(shuffledcards[2], shuffledcards[3], 0, 0, 0)
        #print(str(playercards) + " " + str(playercount))
        placecards(shuffledcards[0], 400, 400)
        placecards(shuffledcards[1], 510, 440)

        placecards(shuffledcards[2], 360, 10)
        placecards(shuffledcards[3], 470, 45)
        #time.sleep(2)


        for event in pygame.event.get():
			
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE: exit()
            #if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if event.type == pygame.QUIT: exit()
        #time.sleep(111)

        pygame.display.update()
        

