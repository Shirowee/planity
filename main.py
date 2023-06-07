import pygame, sys, random, csv
from planetMaker import generateImage
from dataRecup import randomPlanet

#initialise le module pygame
pygame.init()

#on défini la taille l'écran
SCREEN = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Menu")

#on défini le background
BG = pygame.image.load("assets/image/background.png")



class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
        #actualise l'affichage du boutton
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
        #vérifie s'il est appuyé
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
        #fait en sorte qu'il change de couleur quand on passe oar dessus
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

def get_font(size): 
    '''
    retourne une police dans la taille demandée
    '''
    return pygame.font.Font("assets/font.ttf", size)

def fade(width, height): 
    '''
    crée un fondu au noir
    @entree: integer
    @sortie: none
    '''
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        SCREEN.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)

def planet_type_stats():
    '''
    renvoie  le pourcentage de géante gazeuse, neptune-like et autres
    @entrée: None
    @sortie: un tuple
    '''

    #on ouvre le fichier
    f = open('assets/data.csv', "r", encoding = 'utf-8')
    donnees = csv.DictReader(f)
    planet = []
    for ligne in donnees:
        planet.append(dict(ligne))
    f.close()

    #on initialise les compteurs
    neptune_counter = 0
    gas_giant_counter = 0
    other_counter = 0

    #fait le compte
    for i in range(len(planet)):
        if planet[i]['planet_type'] == 'Neptune-like':
            neptune_counter += 1
        elif planet[i]['planet_type'] == 'Gas Giant':
            gas_giant_counter += 1
        else:
            other_counter += 1

    #transforme en pourcentage
    neptune_counter = neptune_counter*100/len(planet)
    gas_giant_counter = gas_giant_counter*100/len(planet)
    other_counter = other_counter*100/len(planet)

    return((neptune_counter,gas_giant_counter,other_counter))

def mass_stats():
    '''
    renvoie  le pourcentage de terre, jupiter et autres en terme de référence pour le poids
    @entrée: None
    @sortie: un tuple
    '''

    #on ouvre le fichier
    f = open('assets/data.csv', "r", encoding = 'utf-8')
    donnees = csv.DictReader(f)
    planet = []
    for ligne in donnees:
        planet.append(dict(ligne))
    f.close()

    #on initialise les compteurs
    earth_counter = 0
    jupiter_counter = 0
    other_counter = 0

    #fait le compte
    for i in range(len(planet)):
        if planet[i]['mass_wrt'] == 'Earth':
            earth_counter += 1
        elif planet[i]['mass_wrt'] == 'Jupiter':
            jupiter_counter += 1
        else:
            other_counter += 1

    #transforme en pourcentage
    earth_counter = earth_counter*100/len(planet)
    jupiter_counter = jupiter_counter*100/len(planet)
    other_counter = other_counter*100/len(planet)
    return((earth_counter,jupiter_counter,other_counter))

def radius_stats():
    '''
    renvoie  le pourcentage de terre, jupiter et autres en terme de référence pour le rayon
    @entrée: None
    @sortie: un tuple
    '''

    #on ouvre le fichier
    f = open('assets/data.csv', "r", encoding = 'utf-8')
    donnees = csv.DictReader(f)
    planet = []
    for ligne in donnees:
        planet.append(dict(ligne))
    f.close()

    #on initialise les compteurs
    earth_counter = 0
    jupiter_counter = 0
    other_counter = 0

    #fait le compte
    for i in range(len(planet)):
        if planet[i]['radius_wrt'] == 'Earth':
            earth_counter += 1
        elif planet[i]['radius_wrt'] == 'Jupiter':
            jupiter_counter += 1
        else:
            other_counter += 1

    #transforme en pourcentage
    earth_counter = earth_counter*100/len(planet)
    jupiter_counter = jupiter_counter*100/len(planet)
    other_counter = other_counter*100/len(planet)

    return((earth_counter,jupiter_counter,other_counter))

def detection_stats():    
    '''
    renvoie  le pourcentage de transit, vitesse radiale et autres en terme de méthode de détection
    @entrée: None
    @sortie: un tuple
    '''
    
    #on ouvre le fichier
    f = open('assets/data.csv', "r", encoding = 'utf-8')
    donnees = csv.DictReader(f)
    planet = []
    for ligne in donnees:
        planet.append(dict(ligne))
    f.close()

    #on initialise les compteurs
    transit_counter = 0
    radial_counter = 0
    other_counter = 0

    #fait le compte
    for i in range(len(planet)):
        if planet[i]['detection_method'] == 'Transit':
            transit_counter += 1
        elif planet[i]['detection_method'] == 'Radial Velocity':
            radial_counter += 1
        else:
            other_counter += 1

    #transforme en pourcentage
    transit_counter = transit_counter*100/len(planet)
    radial_counter = radial_counter*100/len(planet)
    other_counter = other_counter*100/len(planet)

    return((transit_counter,radial_counter,other_counter))

####################
#differents screens#
####################


def play():
    '''
    fonction pour afficher l'écran 'play'
    @entree: None
    @sortie: None
    '''
    #on initialise tout ce qui est génération de planète et infos de celle-ci
    steps = ['step_1/'+ str(random.randint(1,4)) +'.png', 'step_2/'+ str(random.randint(1,4)) +'.png','step_3/'+ str(random.randint(1,4)) +'.png','step_4/'
             + str(random.randint(1,4)) +'.png', 'step_5/'+ str(random.randint(1,4)) +'.png','step_6/'+ str(random.randint(1,4)) +'.png', 'step_7'] # step_1, step_2, step_3, step_4, step_5

    generateImage(steps)
    PLANET = pygame.image.load("assets/planets/stock/s5/1.png").convert_alpha()
    INFO = randomPlanet()

    while True:

        #quoi qu'il se passe on affiche le background
        SCREEN.blit(BG, (0, 0))

        #on cherche la position de la souris
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        #on initialise les boutons
        PLAY_BUTTON = Button(image=pygame.image.load("assets/image/100x30.png"), pos=(75, 30), 
                            text_input="PLAY", font=get_font(30), base_color="#00a896", hovering_color="White")
        MENU_BUTTON = Button(image=pygame.image.load("assets/image/100x30.png"), pos=(200, 30), 
                            text_input="MENU", font=get_font(30), base_color="#00a896", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/image/100x30.png"), pos=(325, 30), 
                            text_input="QUIT", font=get_font(30), base_color="#00a896", hovering_color="White")

        


        #Texte pour les infos
        PLANET_NAME_TEXT = get_font(100).render(INFO['name'], True, '#b68f40')
        PLANET_NAME_RECT = PLANET_NAME_TEXT.get_rect(center=(1400,100))

        PLANET_DISTANCE_TEXT = get_font(30).render('Distance (en AL): ' + INFO['stellar_magnitude'], True, '#FFC300')
        PLANET_DISTANCE_RECT = PLANET_DISTANCE_TEXT.get_rect(center=(1500,250))

        PLANET_TYPE_TEXT = get_font(30).render('Type de planète: ' + INFO['planet_type'], True, '#FFC300')
        PLANET_TYPE_RECT = PLANET_TYPE_TEXT.get_rect(center=(1500,350))

        DISCOVERY_YEAR_TEXT = get_font(30).render('Année de découverte: ' + INFO['discovery_year'], True, '#FFC300')
        DISCOVERY_YEAR_RECT = DISCOVERY_YEAR_TEXT.get_rect(center=(1500,450))

        if float(INFO['mass_multiplier']) < 1:
            MASS_MULTIPLIER_TEXT = get_font(30).render('Elle est ' + INFO['mass_multiplier'] +' fois plus légère que ' + INFO['mass_wrt'], True, '#FFC300')
        else:
            MASS_MULTIPLIER_TEXT = get_font(30).render('Elle est ' + INFO['mass_multiplier'] +' fois plus lourde que ' + INFO['mass_wrt'], True, '#FFC300')
        MASS_MULTIPLIER_RECT = MASS_MULTIPLIER_TEXT.get_rect(center=(1400,550))

        if float(INFO['radius_multiplier']) < 1:
            RADIUS_MULTIPLIER_TEXT = get_font(30).render('Elle a un rayon ' + INFO['radius_multiplier'] +' fois plus petit que ' + INFO['radius_wrt'], True, '#FFC300')
        else:
            RADIUS_MULTIPLIER_TEXT = get_font(30).render('Elle a un rayon ' + INFO['radius_multiplier'] +' fois plus grand que ' + INFO['radius_wrt'], True, '#FFC300')  
        RADIUS_MULTIPLIER_RECT = RADIUS_MULTIPLIER_TEXT.get_rect(center=(1400,650))

        ORBITAL_TEXT = get_font(30).render('Elle a une orbite de ' + INFO['orbital_radius'] +' Unités Astronomiques (UA) ', True, '#FFC300')
        ORBITAL_RECT = ORBITAL_TEXT.get_rect(center=(1400,750))

        ORBITAL_PERIOD_TEXT = get_font(30).render('Elle met ' + INFO['orbital_period'] +' ans a faire une orbite complète ', True, '#FFC300')
        ORBITAL_PERDIOD_RECT = ORBITAL_TEXT.get_rect(center=(1400,850))

        DETECTION_METHOD_TEXT = get_font(30).render('Elle a été découverte grâce à la méthode : ' + INFO['detection_method'], True, '#FFC300')
        DETECTION_METHOD_RECT = DETECTION_METHOD_TEXT.get_rect(center=(1300,950))

        #affiche les textes
        SCREEN.blit(PLANET_NAME_TEXT, PLANET_NAME_RECT)
        SCREEN.blit(PLANET_DISTANCE_TEXT, PLANET_DISTANCE_RECT)
        SCREEN.blit(PLANET_TYPE_TEXT, PLANET_TYPE_RECT)
        SCREEN.blit(DISCOVERY_YEAR_TEXT, DISCOVERY_YEAR_RECT)
        SCREEN.blit(MASS_MULTIPLIER_TEXT, MASS_MULTIPLIER_RECT)
        SCREEN.blit(RADIUS_MULTIPLIER_TEXT, RADIUS_MULTIPLIER_RECT)
        SCREEN.blit(ORBITAL_TEXT, ORBITAL_RECT)
        SCREEN.blit(ORBITAL_PERIOD_TEXT, ORBITAL_PERDIOD_RECT)
        SCREEN.blit(DETECTION_METHOD_TEXT, DETECTION_METHOD_RECT)
        SCREEN.blit(pygame.transform.scale(PLANET, (1000, 1000)), (0,60))
        
        #permet les fonctionnalités supplémentaires des boutons
        for button in [PLAY_BUTTON, MENU_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        #tous les évenements : quitter et clicker sur un bouton
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    fade(1920, 1080)
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    fade(1920, 1080)
                    main_menu()

        #on met tout à jour
        pygame.display.update()
    


def stats():
    '''
    fonction pour afficher l'écran 'stats'
    @entree: None
    @sortie: None
    '''
    while True:
        
        #quoi qu'il se passe on affiche le background
        SCREEN.blit(BG, (0, 0))

        #on cherche la position de la souris
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        #on initialise les boutons
        PLAY_BUTTON = Button(image=pygame.image.load("assets/image/100x30.png"), pos=(75, 30), 
                            text_input="PLAY", font=get_font(30), base_color="#00a896", hovering_color="White")
        MENU_BUTTON = Button(image=pygame.image.load("assets/image/100x30.png"), pos=(200, 30), 
                            text_input="MENU", font=get_font(30), base_color="#00a896", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/image/100x30.png"), pos=(325, 30), 
                            text_input="QUIT", font=get_font(30), base_color="#00a896", hovering_color="White")


        #Texte
        STATS_TEXT = get_font(100).render("Statistiques", True, "#ffb627")
        STATS_RECT = STATS_TEXT.get_rect(center=(1920/2, 200))

        #appel des fonctions de recherche
        TYPE_STATS = planet_type_stats()
        MASS_STATS = mass_stats()
        RADIUS_STATS = radius_stats()
        DETECTION_STATS = detection_stats()
        
        #Texte
        PLANET_TYPE_TEXT = get_font(30).render(str(round(TYPE_STATS[0])) + "% des planètes découvertes sont un équivalent à neptune, " + str(round(TYPE_STATS[1])) + 
                                               "% sont des géantes gazeuses", True, '#FFC300')
        PLANET_TYPE_RECT = STATS_TEXT.get_rect(center=(500, 500))

        MASS_TEXT = get_font(30).render(str(round(MASS_STATS[0])) + "% des planètes découvertes ont un équivalent de poids à la Terre, " + str(round(MASS_STATS[1])) + 
                                               "% sont un équivalent à Jupiter", True, '#FFC300')
        MASS_RECT = MASS_TEXT.get_rect(center=(950, 600))

        RADIUS_TEXT = get_font(30).render(str(round(RADIUS_STATS[0])) + "% des planètes découvertes ont un équivalent de rayon à la Terre, " + str(round(RADIUS_STATS[1])) + 
                                               "% sont un équivalent à Jupiter", True, '#FFC300')
        RADIUS_RECT = RADIUS_TEXT.get_rect(center=(950, 750))

        DETECTION_TEXT = get_font(30).render(str(round(DETECTION_STATS[0])) + "% des planètes ont été découvertes grâce à la méthode transit, " + str(round(DETECTION_STATS[1])) + 
                                               "% grâce à la vitesse radiale", True, '#FFC300')
        DETECTION_RECT = DETECTION_TEXT.get_rect(center=(950, 900))

        #affiche les textes
        SCREEN.blit(STATS_TEXT, STATS_RECT)
        SCREEN.blit(PLANET_TYPE_TEXT, PLANET_TYPE_RECT)
        SCREEN.blit(MASS_TEXT, MASS_RECT)
        SCREEN.blit(RADIUS_TEXT, RADIUS_RECT)
        SCREEN.blit(DETECTION_TEXT, DETECTION_RECT)

        #permet les fonctionnalités supplémentaires des boutons
        for button in [PLAY_BUTTON, MENU_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        #tous les évenements : quitter et clicker sur un bouton
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    fade(1920, 1080)
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    fade(1920, 1080)
                    main_menu()
        
        #on met tout à jour
        pygame.display.update()



def main_menu():
    '''
    fonction pour afficher l'écran de menu
    @entree: None
    @sortie: None
    '''
    while True:
        #quoi qu'il se passe on affiche le background
        SCREEN.blit(BG, (0, 0))

        #on cherche la position de la souris
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        #on initialise les boutons
        PLAY_BUTTON = Button(image=pygame.image.load("assets/image/button.png"), pos=(1920/2, 650), 
                            text_input="PLAY", font=get_font(75), base_color="#00a896", hovering_color="White")
        STATS_BUTTON = Button(image=pygame.image.load("assets/image/button.png"), pos=(1920/2, 800), 
                            text_input="STATS", font=get_font(75), base_color="#00a896", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/image/button.png"), pos=(1920/2, 950), 
                            text_input="QUIT", font=get_font(75), base_color="#00a896", hovering_color="White")
 

        #texte
        MENU_TEXT = get_font(300).render("Planity", True, "#ffb627")
        MENU_RECT = MENU_TEXT.get_rect(center=(1920/2, 200))

        CRED_TEXT = get_font(20).render("Créé par Axel", True, "#03071e")
        CRED_RECT = CRED_TEXT.get_rect(center=(1800, 1050))
        
        #on affiche le texte
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        SCREEN.blit(CRED_TEXT, CRED_RECT)

        #permet les fonctionnalités supplémentaires des boutons
        for button in [PLAY_BUTTON, STATS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        #tous les évenements : quitter et clicker sur un bouton
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    fade(1920, 1080)
                    play()
                if STATS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    stats()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        #on met tout à jour
        pygame.display.update()


#on commence le 'jeu' sur le menu principal
main_menu()