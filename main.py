import pygame, time, random, spritesheethelper
from spritesheethelper import SpriteStripAnim
from playsound import playsound
from pygame import mixer
pygame.init()
mixer.init()
cardslist = ['A', 'A', 'A', 'A', 'K', 'K', 'K', 'K', 'Q', 'Q', 'Q', 'Q', 'J', 'J', 'J', 'J', '10', '10', '10', '10', '9', '9', '9', '9', '8', '8', '8', '8', '7', '7', '7', '7', '6', '6', '6', '6', '5', '5', '5', '5', '4', '4', '4', '4', '3', '3', '3', '3', '2', '2', '2', '2']
deadcards = []
area = 1
minutes = 5
seconds = 0
pygame.display.set_caption('Blackjack')
screen = pygame.display.set_mode((1000, 675))
# = pygame.transform.scale(, (95, 30))
med_font = pygame.font.SysFont("Mochiy Pop One", 30)
font_style = pygame.font.SysFont("Mochiy Pop One", 50)
small_font = pygame.font.SysFont("Mochiy Pop One", 20)
big_font = pygame.font.SysFont("Mochiy Pop One", 145)
verybig_font = pygame.font.SysFont("Algerian", 70)
huge_font = pygame.font.SysFont("Algerian", 175)
menustarttext = verybig_font.render("START", True, [0, 0, 0])
menuoptionstext = verybig_font.render("OPTIONS", True, [0, 0, 0])
menuexittext = verybig_font.render("EXIT", True, [0, 0, 0])


secondevent = pygame.USEREVENT + 1
pygame.time.set_timer(secondevent, 1000)


strips = [
    SpriteStripAnim('assets/jumpscares/spritesheet.png', (0,0,50,34), 5, None, False, 350),
    SpriteStripAnim('assets/jumpscares/spritesheet.png', (0,0,50,34), 5, None, False, 1000),
    SpriteStripAnim('assets/jumpscares/spritesheet.png', (0,0,50,34), 5, None, False, 2000),
    SpriteStripAnim('assets/jumpscares/spritesheet.png', (0,0,50,34), 5, None, False, 3000),
    SpriteStripAnim('assets/jumpscares/spritesheet.png', (0,0,50,34), 5, None, False, 1000),
    SpriteStripAnim('assets/jumpscares/spritesheet.png', (0,0,50,34), 5, None, False, 10)
]
fadestrips = [
    SpriteStripAnim('assets/jumpscares/fadespritesheet.png', (0,0,1000,675), 4, None, False, 500),
    SpriteStripAnim('assets/jumpscares/fadespritesheet.png', (0,0,1000,675), 4, None, False, 500),
    SpriteStripAnim('assets/jumpscares/fadespritesheet.png', (0,0,1000,675), 4, None, False, 500),
    SpriteStripAnim('assets/jumpscares/fadespritesheet.png', (0,0,1000,675), 4, None, False, 500)
]

pixintrostrips = [
    SpriteStripAnim('assets/jumpscares/pixintrospritesheet.png', (0,0,1000,675), 4, None, False, 1000),
    SpriteStripAnim('assets/jumpscares/pixintrospritesheet.png', (0,0,1000,675), 4, None, False, 1000),
    SpriteStripAnim('assets/jumpscares/pixintrospritesheet.png', (0,0,1000,675), 4, None, False, 8000),
    SpriteStripAnim('assets/jumpscares/pixintrospritesheet.png', (0,0,1000,675), 4, None, False, 1000),
    #SpriteStripAnim('assets/jumpscares/pixintrospritesheet.png', (0,0,1000,675), 8, None, False, 1500),
    #SpriteStripAnim('assets/jumpscares/pixintrospritesheet.png', (0,0,1000,675), 8, None, False, 1000),
    #SpriteStripAnim('assets/jumpscares/pixintrospritesheet.png', (0,0,1000,675), 8, None, False, 1000),
    #SpriteStripAnim('assets/jumpscares/pixintrospritesheet.png', (0,0,1000,675), 8, None, False, 1000)
    #SpriteStripAnim('assets/jumpscares/pixintrospritesheet.png', (0,0,1000,675), 8, None, False, 1000)
]
n = 0
f = 0
g = 0
strips[n].iter()
pixintrostrips[g].iter()
image = strips[n].next()
pixintroimage = pixintrostrips[g].next()
#while True:
    #for e in pygame.event.get():
        #if e.type == pygame.KEYDOWN:
            #if e.key == pygame.K_ESCAPE:
                #exit()
            #elif e.key == pygame.K_RETURN:
                #n += 1
                #if n >= len(strips):
                    #n = 0
                #strips[n].iter()
    #screen.fill(0, 0, 0)

    #screen.blit(pygame.transform.scale(image, (0,0)), [1000, 675])
    


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

def jumpscare(what, image, introimage="sus"):
    # what is a cookie clicker reference
    x = 0
    for i in range(0, 3):
        screen.fill((255, 255, 255))
        #pygame.event.get()
        #screen.blit(fadeimage, (0, 0))
        pygame.display.update()
        time.sleep(0.1)
        screen.fill((0, 0, 0))
        pygame.display.update()
        time.sleep(0.1)

    if what == "pix":
        pixintroimage = introimage
        while True:
            pygame.event.get()
            screen.blit(pixintroimage, (0, 0))
            pygame.display.update()
            try: pixintroimage = pixintrostrips[g].next()
            except Exception as e:
                while True:
                    pygame.event.get()
                    x += 1
                    if x == 1700: 
                        playsound('assets/audio/vannscream.mp3')
                    image = pygame.transform.scale(image, [1000, 675])
                    screen.blit(image, (0, 0))
                    pygame.display.update()
                    try: image = strips[n].next()
                    except Exception as e: exit()



def placecards(card, x, y):
    try:
        screen.blit(cards[int(card)], [x, y])
    except: 
        if card == "A": screen.blit(cards[0], [x, y])
        elif card == "K": screen.blit(cards[1], [x, y])
        elif card == "Q": screen.blit(cards[11], [x, y])
        elif card == "J": screen.blit(cards[12], [x, y])
        else: raise Exception("Could not display unknown card")


def cardvalue(card):
    playercount = 0
    try:
        playercount += int(card)
    except:
        if card in "KQJ": playercount += 10
        elif card in "A":
            if playercount + 11 > 21: playercount += 1
            else: playercount += 11
    return playercount





while True:
    screen.blit(menu, [0, 0])
    screen.blit(menustarttext, [20, 100])
    screen.blit(menuoptionstext, [20, 190])
    screen.blit(menuexittext, [20, 280])
    
    start = True
    
    
    pygame.display.update()
    

    time.sleep(2)
    
    shuffledcards = random.sample(cardslist, len(cardslist))
    playercards = [shuffledcards[0], shuffledcards[1]]
    playercount = 0
    playercardnumber = 0
    dealercount = 0
    dealercardnumber = 0
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE: exit()
		#if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if event.type == pygame.QUIT: exit()

    while start:
        
        
        
        playercount += cardvalue(shuffledcards[0])
        playercount += cardvalue(shuffledcards[1])
        dealercount += cardvalue(shuffledcards[2])
        dealercount += cardvalue(shuffledcards[3])
        #print(str(playercards) + " " + str(playercount))
        for event in pygame.event.get():
            if event.type == secondevent: 
                        seconds -= 1
                        if seconds == -1: 
                            if minutes != 0:
                               minutes -= 1; seconds = 59
                            else:
                                jumpscare("pix", image, pixintroimage)


        #time.sleep(2)
        if area == -1: area = 1
        while area == 1:
            screen.fill([20, 20, 20])
            if len(str(seconds)) == 1:
                displayseconds = "0" + str(seconds)
            else: displayseconds = str(seconds)
            bgtimertext = huge_font.render(str(minutes) + ":" + str(displayseconds), True, [50, 50, 50])
            playercounttext = big_font.render(str(playercount), True, [50, 50, 50])
            dealercounttext = big_font.render(str(dealercount), True, [50, 50, 50])
            screen.blit(bgtimertext, (250, 210))
            screen.blit(playercounttext, (210, 330))
            screen.blit(dealercounttext, (240, 80))

            placecards(shuffledcards[0], 400, 400)
            placecards(shuffledcards[1], 500, 415)

            placecards(shuffledcards[2], 360, 10)
            placecards(shuffledcards[3], 470, 45)

            for event in pygame.event.get():
                if event.type == secondevent: 
                    seconds -= 1
                    if seconds == -1: 
                        if minutes != 0:
                            minutes -= 1; seconds = 59
                        else:
                            jumpscare("pix", image, pixintroimage)
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_ESCAPE: exit()
                    if event.key == pygame.K_1:
                        playercardnumber += 1; placecards(shuffledcards[3 + playercardnumber], 500 + (110 * playercardnumber), 415 + (35 * playercardnumber)); playercount += cardvalue(shuffledcards[3 + playercardnumber]); print(playercount); 
                        pygame.display.update()
                    if event.key == pygame.K_2:
                        while dealercount < 17:
                            dealercardnumber += 1; placecards(shuffledcards[10 + dealercardnumber], 470 + (100 * dealercardnumber), 45 + (15 * dealercardnumber)); dealercount += cardvalue(shuffledcards[10 + dealercardnumber])
                            if shuffledcards[10 + dealercardnumber] == "A":
                                if dealercount - 10 <= 21: dealercount -= 10
                            #playercounttext = big_font.render(str(playercount), True, [50, 50, 50])
                            #dealercounttext = big_font.render(str(dealercount), True, [50, 50, 50])
                            #screen.blit(dealercounttext, (240, 80))
                            #screen.blit(playercounttext, (210, 330))
                            pygame.display.update()
                            time.sleep(0.8)
                        print(playercount)
                        print(dealercount) 
                        while playercount > 21 or dealercount > playercount and dealercount <= 21: 
                            jumpscare("pix", image, pixintroimage)
                            
                        if playercount == 21 or playercount > dealercount or dealercount > 21: print("win"); exit()
                        else: print("prose")
                #if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if event.type == pygame.QUIT: exit()
            while playercount > 21: 
               jumpscare("pix", image, pixintroimage)
            pygame.display.update()
        

