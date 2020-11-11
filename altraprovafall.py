from random import randint
import pygame
import random
pygame.init()


#colori
ROSSO = (255, 0, 0)
NERO = (0, 0, 0)
VIOLA = (135, 0, 255)
GIALLO = (255, 255, 0)
VERDEFORESTA = (34,139,34)
AQUA = (0, 255, 255)

#schermo
SCHERMO = (720, 720)
schermo = pygame.display.set_mode(SCHERMO)
schermo.fill(NERO)

#fps e timer del gioco
FPS = 60
FONT = pygame.font.SysFont('Arial', 50)
FONT = pygame.font.SysFont('Comic Sans MS', 50, bold=True)

#VARIABILI: tempos ("tempo"/ movimenti), punti e timer
tempos = 1000
punti = 0
time = 0

'''
Coordinate degli oggetti (giocatore nemici e bonus)
'''
#coordinate giocatore principale                                     #info 
x = round(random.randrange(0, 720-50, 50)/50, 50)*50                 #round(random.randrange(0, 720-50, 50)/50, 50)*50 fa in modo che le posizioni delle coordinate (casuali) "cambino"di 50 pixel in 50 pixel, rendendo la giocabilità e visione migliore
y = round(random.randrange(0, 720-50, 50)/50, 50)*50

#coordinate bonus 1
randx = round(random.randrange(0, 720-50, 50)/50, 50)*50
randy = round(random.randrange(0, 720-50, 50)/50, 50)*50

#coordinate nemico 1
randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50

#coordinate bonus 2
randx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
randy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50

#coordinate nemico 2
randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50

#coordinate nemico 3
randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50

#coordinate nemico 4
randenemyx4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
randenemyy4 = round(random.randrange(0, 720-50, 50)/50, 50)*50

#coordinate nemico 5
randenemyx5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
randenemyy5 = round(random.randrange(0, 720-50, 50)/50, 50)*50

#coordinate nemico 6
randenemyx6 = round(random.randrange(0, 720-50, 50)/50, 50)*50
randenemyy6 = round(random.randrange(0, 720-50, 50)/50, 50)*50

#coordinate bonus di valore cinque (n3) "diamante"
randx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
randy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50




#lettura immagini pygame dello schermo, giocatore ecc...  del gioco
sfondo = pygame.image.load('sfondos.png')
gameover = pygame.image.load('gameover.jpg')
haivinto = pygame.image.load('haivinto.png')
giocatore = pygame.image.load('eroeufficiale.png')
nemicouno = pygame.image.load('nemicoufficiale.png')
nemicodue = pygame.image.load('nemicoufficiale.png')
nemicotre = pygame.image.load('nemicoufficiale.png')
nemicoquattro = pygame.image.load('nemicoufficiale.png')
nemicocinque = pygame.image.load('nemicoufficiale.png')
nemicosei = pygame.image.load('nemicoufficiale.png')
puntiuno = pygame.image.load('moneta.png')
puntidue = pygame.image.load('moneta.png')
specialbonus = pygame.image.load('diamante.png')


'''
definizioni per semplificare lo sviluppo del gioco:
'''

# per disegnare gli "oggetti" (sfondo, giocatore ecc...)
def disegna_oggetti():
    schermo.blit(sfondo, (0, 0))
    schermo.blit(giocatore, (x, y))
    schermo.blit(nemicouno, (randenemyx, randenemyy))
    schermo.blit(nemicodue, (randenemyx2, randenemyy2))
    schermo.blit(nemicotre, (randenemyx3, randenemyy3))
    schermo.blit(nemicoquattro, (randenemyx4, randenemyy4))
    schermo.blit(nemicocinque, (randenemyx5, randenemyy5))
    schermo.blit(nemicosei, (randenemyx6, randenemyy6))
    schermo.blit(puntiuno, (randx, randy))
    schermo.blit(puntidue, (randx2, randy2))
    schermo.blit(specialbonus, (randx3, randy3))


# def che semplifica il sistema di "refresh" del gioco
def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)


# def che fa apparire gameover e fa riiniziare il gioco 
def hai_perso():
    schermo.blit(gameover, (0, 0))
    aggiorna()
    ricominciamo = False
    while not ricominciamo:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                ricominciamo = True 
                                     
            if event.type == pygame.QUIT:
                    pygame.quit()


#def che fa apparire "you win" e fa riiniziare il gioco 
def hai_vinto():
    schermo.blit(haivinto, (0,0))
    aggiorna()
    ricominciamo = False
    while not ricominciamo:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_5:
                ricominciamo = True 
                                       
            if event.type == pygame.QUIT:
                pygame.quit()



'''
FINE impostazioni, variabili, coordinate, def ecc..... INIZIO CICLO WHILE DEL GIOCO
'''


#CICLO DEL GIOCO PRINCIPALE
while True:

 
 #segnatempo
 time_render = FONT.render(str(time), 1, ROSSO)
 schermo.blit(time_render, (610, 1))
 time += 0.02
 
 #segnapunti
 punti_render = FONT.render(str(punti), 1, (255, 255, 255))
 schermo.blit(punti_render, (600, 50))
 aggiorna()
 
 
 #sistema di movimento (progettato di 50 in 50)
 for event in pygame.event.get():
    if  event.type == pygame.KEYDOWN and event.key == pygame.K_UP:                #info
        y -= 50                                                                   #ogni "tocco" di una delle freccette la variabile tempos cala di 1
        tempos -= 1 
    if  event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
        x -= 50
        tempos -= 1
    if  event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        x += 50
        tempos -= 1
    if  event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
        y += 50
        tempos -= 1
    
    #sistema di uscita dal gioco, contatto con la parete (riavvia gioco con spazio)
    if event.type == pygame.QUIT:
        pygame.quit()
    
    if y >= 725 or y <= -5 or x >= 725 or x <= -5:
        hai_perso()
        tempos = 1000
        punti = 0
        time = 0
        x = round(random.randrange(0, 720-50, 50)/50, 50)*50
        y = round(random.randrange(0, 720-50, 50)/50, 50)*50
    
        
    # bonus 1 spostamento dopo essere stato toccato + assegnazione punto
    if x == randx and y == randy:
        randx = round(random.randrange(0, 720-50, 50)/50, 50)*50
        randy = round(random.randrange(0, 720-50, 50)/50, 50)*50
       
        punti += 1
     
    # bonus 2 spostamenti dopo essere stato toccato + assegnazione punto
    if x == randx2 and y == randy2:
        randx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
        randy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
       
        punti += 1
    
    #bonus 3 spostamento collettivo degli oggetti (tranne il player) + assegnazione triplo punto
    if x == randx3 and y == randy3:
        randx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
        randy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
        randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
        randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
        randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
        randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
        randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
        randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
        randenemyx4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
        randenemyy4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
        randenemyx5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
        randenemyy5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
        randenemyx6 = round(random.randrange(0, 720-50, 50)/50, 50)*50
        randenemyy6 = round(random.randrange(0, 720-50, 50)/50, 50)*50
        randx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
        randy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
        punti += 3
    
    
    #I NEMICI E LE LORO POSIZIONI PRIMA DI ENTRARE IN GIOCO (fuori dalla mappa) 
    
    #spawn esterno fino a 940 (tempos) nemico 3         
    if tempos > 940:
        randenemyx3 = 2000 
        randenemyy3 = 2000
    
    #spawn esterno fino a 880 nemico 4                             #info
    if tempos > 880:                                               #questo fa in modo che prima di un determinato valore di tempos i nemici/bonus non appaiano nella mappa 
        randenemyx4 = 2100
        randenemyy4 = 2100
    
    #spawn esterno fino a 750 nemico 5
    if tempos > 750:    
        randenemyx5 = 2200
        randenemyy5 = 2200
    
    #spawn esterno fino a 650 nemico 6
    if tempos > 650:    
        randenemyx6 = 2200
        randenemyy6 = 2200
    
    #spawn esterno bonus da 5
    if tempos > 750:
        randx3 = 2300
        randy3 = 2300
    
    
    
    #CONTATTO E MORTE PER "MANO DEI NEMICI
    
    # morte giocatore nemico 1
    if x == randenemyx and y == randenemyy:
        hai_perso()
        punti = 0
        time = 0   
        tempos = 1000
        x = round(random.randrange(0, 720-50, 50)/50, 50)*50
        y = round(random.randrange(0, 720-50, 50)/50, 50)*50
    
    # morte giocatore nemico 2
    if x == randenemyx2 and y == randenemyy2:
        hai_perso()
        punti = 0
        time = 0
        tempos = 1000
        x = round(random.randrange(0, 720-50, 50)/50, 50)*50
        y = round(random.randrange(0, 720-50, 50)/50, 50)*50 
    
    #morte giocatore nemico 3
    if x == randenemyx3 and y == randenemyy3:
        hai_perso()
        punti = 0
        time = 0
        tempos = 1000
        x = round(random.randrange(0, 720-50, 50)/50, 50)*50
        y = round(random.randrange(0, 720-50, 50)/50, 50)*50
    
    #morte giocatore nemico 4
    if x == randenemyx4 and y == randenemyy4:
        hai_perso()
        punti = 0
        time = 0
        tempos = 1000
        x = round(random.randrange(0, 720-50, 50)/50, 50)*50
        y = round(random.randrange(0, 720-50, 50)/50, 50)*50
    
    #morte giocatore nemico 5
    if x == randenemyx5 and y == randenemyy5:
        hai_perso()
        punti = 0
        time = 0
        tempos = 1000
        x = round(random.randrange(0, 720-50, 50)/50, 50)*50
        y = round(random.randrange(0, 720-50, 50)/50, 50)*50
    
    #morte giocatore nemico 6
    if x == randenemyx6 and y == randenemyy6:
        hai_perso()
        punti = 0
        time = 0
        tempos = 1000
        x = round(random.randrange(0, 720-50, 50)/50, 50)*50
        y = round(random.randrange(0, 720-50, 50)/50, 50)*50
    
    
    #50 punti = vittoria, + di 70 secondi = gameover
    
    #vittoria giocatore per tot. punti
    if punti >= 50:
        hai_vinto()
        punti = 0
        time = 0
        tempos = 1000
        x = round(random.randrange(0, 720-50, 50)/50, 50)*50
        y = round(random.randrange(0, 720-50, 50)/50, 50)*50
    
    #se impieghi piu di 70 secondi per fare 50 punti, hai perso
    if time >= 70.00000 :
        hai_perso()
        punti = 0
        time = 0
        tempos = 1000
        x = round(random.randrange(0, 720-50, 50)/50, 50)*50
        y = round(random.randrange(0, 720-50, 50)/50, 50)*50
    
    
    
    
    #-CODICE RIPETITIVO- spawn ogni tot. spostamenti di nuovi nemici e bonus  (fino a riga: 700/75 0 c.a)
                                        
    #spawn nemici randomico ogni tot spostamenti
    
    if tempos == 980:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50                 
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50                #nemico 1 e 2
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     
    if tempos == 960:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
    
    if tempos == 940:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50                #entrata nemico 3
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50                
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
    
    if tempos == 920:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
    
    if tempos == 900:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
    
    if tempos == 890: 
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
    
    if tempos == 880:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50                    #entrata nemico 4
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     
    
    if tempos == 860:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
    
    if tempos == 840: 
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
    
    if tempos == 820:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
    
    if tempos == 800:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
    
    if tempos == 780:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
    
    if tempos == 770:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
    
    if tempos == 760:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
    
    if tempos == 750:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy4 = round(random.randrange(0, 720-50, 50)/50, 50)*50              #entrata nemico 5 e arrivo del bonus speciale 
     randenemyx5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
    
    if tempos == 730:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randx3 = 2300
     randy3 = 2300
    
    if tempos == 710:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
    
    if tempos == 690:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randx3 = 2300
     randy3 = 2300
    
    if tempos == 680:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     
    
    if tempos == 670:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
    
    if tempos == 660:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     
    
    if tempos == 650:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50                      #nemico 6, fase conclusiva del gioco
     randenemyx4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx6 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy6 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randx3 = 2300
     randy3 = 2300
    
    if tempos == 630:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx6 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy6 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     
    if tempos == 610:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx6 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy6 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
    
    if tempos == 590:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx6 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy6 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randx3 = 2300
     randy3 = 2300
    
    if tempos == 570:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx6 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy6 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
    
    if tempos == 550:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx6 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy6 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randx3 = 2300
     randy3 = 2300
    
    if tempos == 540:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx6 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy6 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     
    if tempos == 530:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx6 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy6 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     
    if tempos == 520:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx6 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy6 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
    
    if tempos == 510:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx6 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy6 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     
    
    if tempos == 500:
     randenemyx2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy2 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy3 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy4 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy5 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyx6 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randenemyy6 = round(random.randrange(0, 720-50, 50)/50, 50)*50
     randx3 = 2300
     randy3 = 2300
    
    #fine codice ripetitivo gioco e fine movimenti/spostamenti bonus nemici
    #durata del gioco massima: 70s
    #durata codice ripetitivo: 80/120s

 
 
 
 #questa funzione come si legge fa in modo che vengano all infinito, o per lo meno fino alla fine del gioco, disegnati gli oggetti
 disegna_oggetti()
 
 
 #refresh del display
 pygame.display.update()