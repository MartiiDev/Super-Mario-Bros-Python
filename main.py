# -*- coding: utf-8 -*-
"""
@author: Edgar Caudron

Bug connu : Pas de collision avec le haut du corps
"""

import pygame
import time
import random
import sys
import os

## Variables
gameName = "Super Mario Bros"
quitGame = False
inGame = False
muteGame = False
tileWidth = 32
playLuigi = False


## Niveaux
def setLevels():
    global niveaux
    niveaux = { # 25x10 blocs
        1: 	[[		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		10,		11,		12,		0,		0,		0,		0,		0,		0,		0,		1],
    		[		0,		10,		11,		12,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		13,		14,		15,		0,		0,		6,		0,		0,		0,		0,		1],
    		[		0,		13,		14,		15,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1],
    		[		0,		0,		0,		0,		0,		0,		0,		10,		11,		12,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1],
    		[		0,		0,		0,		0,		0,		0,		7,		13,		14,		15,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1,		0,		0,		0,		1],
    		[		0,		0,		0,		0,		0,		0,		1,		1,		1,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1,		1,		0,		0,		0,		1],
    		[		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1,		1,		1,		0,		24,		25,		1],
    		[		0,		22,		23,		1,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1,		1,		1,		1,		0,		26,		27,		1],
    		[		9,		9,		9,		9,		9,		0,   	0,		9,		9,		0,		22,		23,		100,    7,      0,		0,		9,		9,		9,		9,		9,		9,		9,		9,		9,		1],
    		[		9,		9,		9,		9,		9,		0,		0,		9,		9,		9,		9,		9,		9,		9,		9,		9,		9,		9,		9,		9,		9,		9,		9,		9,		9,		1],
    		[		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1],
    		],

    	2:	[[		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1],
            [		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1],
    		[		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		18,		18,		18,		18,		18,		1],
    		[		0,		0,		0,		0,		0,		0,		0,		0,		18,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		18,		4,		0,		0,		18,		1],
    		[		0,		0,		0,		16,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		16,		16,		16,		0,		28,   	18,		5,		0,		0,		18,		1],
    		[		0,		0,		18,		18,		18,		18,		0,		0,		0,		0,		0,		18,		0,		0,		18,		18,		18,		18,		18,		18,		18,		18,		0,		0,		18,		1],
    		[		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		18,		1],
    		[		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		18,		18,		1],
    		[		0,		0,		0,		0,		0,		0,		0,		18,		18,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		18,		18,		18,		1],
    		[		42,		43,		18,		18,		18,		18,		18,		18,		18,		0,		0,		18,		18,		18,		18,		18,		18,		18,		18,		18,		18,		18,		18,		18,		18,		1],
    		[		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1],
            ],
        
    	3:	[[		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		6,		0,		1],
            [		0,		0,		0,		0,		10,		11,		12,		0,		0,		0,		0,		0,		0,		0,		0,		6,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1],
            [		0,		0,		0,		0,		13,		14,		15,		0,   	0,     	0,	    0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1],
            [		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		10,		11,		12,		0,		0,		0,		0,		0,		6,		0,		0,		0,		0,		0,		1],
            [		11,		12,		0,		0,		0,		0,		0,		0,		6,		0,		0,		13,		14,		15,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1],
            [		14,		15,		0,		0,		0,		7,		0,		0,		0,		0,		0,		0,		0,		0,		0,		44,		45,		45,		45,		46,		0,		0,		0,		10,		11,		1],
            [		0,		0,		0,		0,		44,		45,		46,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		4,		0,		0,		0,		0,		0,		13,		14,		1],
            [		0,		0,		0,		0,		0,		0,		0,		0,		7,		0,		0,		0,		7,		0,		0,		0,		0,		5,		0,		0,		0,		0,		0,		0,		0,		1],
            [		0,		0,		0,		0,   	0,		0,		0,		0,		3,		3,		0,		0,		47,		0,		0,		44,		45,		45,		45,		46,		0,		0,		0,		0,		0,		1],
            [		3,		3,		3,		3,		3,		3,		3,		3,		2,		2,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1],
    		[		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1],
            ],
        
    	4:	[[		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		10,		11,		12,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1],
             [		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		13,		14,		15,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1],
             [		0,		0,		4,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1],
             [		0,		0,		5,		0,		0,		1,		0,		101,	0,		0,		0,		0,		1,		0,		0,		47,		0,		1,		0,		0,		7,		0,		0,		0,		0,		1],
             [		0,		0,		9,		0,		0,		1,		1,		1,		1,		1,		1,		1,		1,		0,		0,		0,		0,		1,		1,		1,		1,		1,		0,		0,		0,		1],
             [		11,		12,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		9,		1],
             [		14,		15,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		10,		11,		12,		0,		9,		9,		1],
             [		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		9,		0,		0,		13,		14,		15,		9,		9,		9,		1],
             [		0,		0,		0,		0,		0,		0,		0,		9,		0,		0,		0,		0,  	0,		0,		0,		0,		0,		0,		0,		7,		0,		9,		9,		9,		9,		1],
             [		9,		9,		9,		9,		9,		0,		0,		9,		9,		9,		9,		9,		9,		9,		0,		0,		0,		9,		9,		9,		9,		9,		9,		9,		9,		1],
             [		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1],
            ],
        
        5:	[[		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1],
    		[		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1],
    		[		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1],
    		[		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		9,		0,		7,		0,		0,		0,		0,		29,		29,		29,		0,		0,		0,		1],
    		[		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		9,		9,		0,		0,		0,		0,		0,		0,		30,		30,		30,		0,		0,		0,		1],
    		[		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		9,		9,		9,		0,		0,		0,		0,		0,		0,		41,		30,		30,		0,		0,		0,		1],
    		[		0,		0,		0,		0,		0,		0,		0,		0,		0,		9,		9,		9,		9,		0,		0,		0,		0,		0,		0,		41,		20,		30,		0,		0,		0,		1],
    		[		0,		0,		0,		0,		0,		0,		0,		0,		9,		9,		9,		9,		9,		0,		0,		0,		0,		0,		0,		41,		31,		30,		0,		0,		0,		1],
    		[		0,		0,		0,		0,		0,		0,		0,		9,		9,		9,		9,		9,		9,		0,		0,		0,		0,		0,		0,		41,		21,		30,		0,		0,		0,		1],
    		[		3,		3,		3,		3,		3,		3,		3,		3,		3,		3,		3,		3,		3,		0,		0,		0,		3,		3,		3,		3,		3,		3,		3,		3,		3,		1],
    		[		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1],
            ],
        
    	6:	[[		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1],
             [		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1],
             [		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1],
             [		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1],
             [		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1],
             [		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		37,		1],
             [		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		38,		1],
             [		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		32,		34, 	0,		39,		1],
             [		0,		0,		0,		0,		0,		0,		0,		9,		0,  	0,		100,	0,		0,    	9,		0,		0,		0,		0,		0,		0,		0,		35,		36, 	0,		0,    	1],
             [		9,		9,		9,		9,		9,		0,		0,		9,		9,		9,		9,		9,		9,		9,		9,		9,		9,		9,		9,		9,		9,		9,		9,		9,		9,		1],
             [		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		0,		1],
            ],
    }
setLevels()
lvlNumber = 1
niveauxBackup = niveaux
niveauActuel = niveaux[1]


## Système
pygame.init()
taille_fenetre = (len(niveauActuel[0])*32-32, len(niveauActuel)*32-32)
fenetre_rect = pygame.Rect((0, 0), taille_fenetre)
screen_surface = pygame.display.set_mode(taille_fenetre)
policeS = pygame.font.SysFont('Arial', 20)
policeL = pygame.font.SysFont('Arial', 21)
policeXL = pygame.font.SysFont('Arial', 40)
pygame.display.set_caption(gameName)
clock = pygame.time.Clock()
music = pygame.mixer.music

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


## Assets
mario = {
    "normal": pygame.transform.scale(pygame.image.load(resource_path(resource_path("fichiers/images/character/mario/stand.png"))), (30, 60)).convert_alpha(),
    "normalJump": pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/character/mario/right_jump.png")), (30, 60)).convert_alpha(),
    "left": pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/character/mario/left.png")), (30, 60)).convert_alpha(),
    "leftJump": pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/character/mario/left_jump.png")), (30, 60)).convert_alpha(),
    "right": pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/character/mario/right.png")), (30, 60)).convert_alpha(),
    "rightJump": pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/character/mario/right_jump.png")), (30, 60)).convert_alpha(),
    "crouched": pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/character/mario/crouched.png")), (30, 60)).convert_alpha(),
}
luigi = {
    "normal": pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/character/luigi/stand.png")), (30, 60)).convert_alpha(),
    "normalJump": pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/character/luigi/right_jump.png")), (30, 60)).convert_alpha(),
    "left": pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/character/luigi/left.png")), (30, 60)).convert_alpha(),
    "leftJump": pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/character/luigi/left_jump.png")), (30, 60)).convert_alpha(),
    "right": pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/character/luigi/right.png")), (30, 60)).convert_alpha(),
    "rightJump": pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/character/luigi/right_jump.png")), (30, 60)).convert_alpha(),
    "crouched": pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/character/luigi/crouched.png")), (30, 60)).convert_alpha(),
}
blocs = {
    ## Blocs
    1: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/brick.png")), (tileWidth, tileWidth)).convert_alpha(),
    2: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/dirt.png")), (tileWidth, tileWidth)).convert_alpha(),
    3: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/grass.png")), (tileWidth, tileWidth)).convert_alpha(),
    4: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/drapeau.png")), (tileWidth, tileWidth)).convert_alpha(),
    5: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/tige_drapeau.png")), (tileWidth, tileWidth)).convert_alpha(),
    6: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/nuage.png")), (tileWidth, tileWidth)).convert_alpha(),
    7: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/piece.png")), (tileWidth, tileWidth)).convert_alpha(),
    8: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/piece-cote.png")), (tileWidth, tileWidth)).convert_alpha(),
    9: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/ground.png")), (tileWidth, tileWidth)).convert_alpha(),
    10: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/nuage-tl.png")), (tileWidth, tileWidth)).convert_alpha(),
    11: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/nuage-tc.png")), (tileWidth, tileWidth)).convert_alpha(),
    12: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/nuage-tr.png")), (tileWidth, tileWidth)).convert_alpha(),
    13: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/nuage-bl.png")), (tileWidth, tileWidth)).convert_alpha(),
    14: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/nuage-bc.png")), (tileWidth, tileWidth)).convert_alpha(),
    15: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/nuage-br.png")), (tileWidth, tileWidth)).convert_alpha(),
    16: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/cave/piece.png")), (tileWidth, tileWidth)).convert_alpha(),
    17: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/cave/piece-cote.png")), (tileWidth, tileWidth)).convert_alpha(),
    18: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/cave/brick.png")), (tileWidth, tileWidth)).convert_alpha(),
    19: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/cave/ground.png")), (tileWidth, tileWidth)).convert_alpha(),
    20: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/porte-haut.png")), (tileWidth, tileWidth)).convert_alpha(),
    21: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/porte-bas.png")), (tileWidth, tileWidth)).convert_alpha(),
    22: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/buisson-l.png")), (tileWidth, tileWidth)).convert_alpha(),
    23: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/buisson-r.png")), (tileWidth, tileWidth)).convert_alpha(),
    24: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/tuyau-tl.png")), (tileWidth, tileWidth)).convert_alpha(),
    25: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/tuyau-tr.png")), (tileWidth, tileWidth)).convert_alpha(),
    26: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/tuyau-bl.png")), (tileWidth, tileWidth)).convert_alpha(),
    27: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/tuyau-br.png")), (tileWidth, tileWidth)).convert_alpha(),
    28: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/misc/greenChampi.png")), (tileWidth, tileWidth)).convert_alpha(),
    29: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/creneau.png")), (tileWidth, tileWidth)).convert_alpha(),
    30: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/brick2.png")), (tileWidth, tileWidth)).convert_alpha(),
    31: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/porte-centre.png")), (tileWidth, tileWidth)).convert_alpha(),
    32: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/ennemies/bowser-tl.png")), (tileWidth, tileWidth)).convert_alpha(),
    33: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/ennemies/bowser-tl-open.png")), (tileWidth, tileWidth)).convert_alpha(),
    34: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/ennemies/bowser-tr.png")), (tileWidth, tileWidth)).convert_alpha(),
    35: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/ennemies/bowser-bl.png")), (tileWidth, tileWidth)).convert_alpha(),
    36: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/ennemies/bowser-br.png")), (tileWidth, tileWidth)).convert_alpha(),
    37: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/misc/peach-haut.png")), (tileWidth, tileWidth)).convert_alpha(),
    38: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/misc/peach-bas.png")), (tileWidth, tileWidth)).convert_alpha(),
    39: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/plateforme.png")), (tileWidth, tileWidth)).convert_alpha(),
    40: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/lave.png")), (tileWidth, tileWidth)).convert_alpha(),
    41: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/brick2.png")), (tileWidth, tileWidth)).convert_alpha(),
    42: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/tuyau-tl.png")), (tileWidth, tileWidth)).convert_alpha(),
    43: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/tuyau-tr.png")), (tileWidth, tileWidth)).convert_alpha(),
    44: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/plateforme-l.png")), (tileWidth, tileWidth)).convert_alpha(),
    45: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/plateforme-c.png")), (tileWidth, tileWidth)).convert_alpha(),
    46: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/plateforme-r.png")), (tileWidth, tileWidth)).convert_alpha(),
    47: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/nuage-smile.png")), (tileWidth, tileWidth)).convert_alpha(),

    100: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/ennemies/champi-left.png")), (tileWidth, tileWidth)).convert_alpha(),
    101: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/ennemies/champi-right.png")), (tileWidth, tileWidth)).convert_alpha(),
    106: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/nuage-l.png")), (tileWidth, tileWidth)).convert_alpha(),
    107: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/nuage-c.png")), (tileWidth, tileWidth)).convert_alpha(),
    108: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/nuage-r.png")), (tileWidth, tileWidth)).convert_alpha(),
    109: pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/tiles/nuage-smile.png")), (tileWidth, tileWidth)).convert_alpha(),
}
blocsSpeciaux = [0,4,5,6,7,8,10,11,12,13,14,15,16,17,20,21,22,23,28,37,38,41]
divers = {
    "menu": pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/misc/menu.png")), taille_fenetre),
    "greenChampi": pygame.transform.scale(pygame.image.load(resource_path("fichiers/images/misc/greenChampi.png")), (tileWidth, tileWidth)).convert_alpha(),
}


## Fonctions
def getSpawnPoint(niveau):
    """Retourne le Y le plus haut pour spawn dessus"""
    ni=0 # Y
    for i in niveau:
        if niveau[ni][0] != 0:
            ni -= 1
            global spawnPoint
            spawnPoint = 0, ni*32
            return spawnPoint
        ni+=1
marioX, marioY = getSpawnPoint(niveauActuel)

def dessiner_niveau(surface, niveau):
    """Dessine la map grace aux matrices"""
    ni=0 # Y
    for i in niveau:
        nj=0 # X
        for j in niveau[ni]:
            if j != 0:
                if j >= 100:
                    if not any(j in i for i in mobList):
                        moveSpeed = round(random.uniform(1.8,2.4), 2)
                        moveSide = [-1,1][random.randrange(2)]
                        mobList.append([blocs[j], [nj*tileWidth, ni*tileWidth], [0,0], [0,0], moveSpeed, moveSide, j, [nj,ni]]) 
                else:
                    surface.blit(blocs[j], (nj*tileWidth, ni*tileWidth))
            nj+=1
        ni+=1

def from_coord_to_grid(pos):
    """Retourne la position de mario dans la grille"""
    x, y = pos
    i = max(0, int(x // tileWidth))
    j = max(0, int(y // tileWidth))
    return i, j
 
def get_neighbour_blocks(i_start, j_start):
    """Retourne les rectangles autour de mario"""
    blocks = list()
    for j in range(j_start, j_start+2):
        for i in range(i_start, i_start+2):
            if niveauActuel[j][i] not in blocsSpeciaux and niveauActuel[j][i] < 100: # Pas de collisions avec les blocs spéciaux
                topleft = i*tileWidth, j*tileWidth
                blocks.append(pygame.Rect((topleft), (tileWidth, tileWidth)))
    return blocks
 
def bloque_sur_collision(old_pos, new_pos, vx, vy):
    """Verifier si collision"""
    old_rect = pygame.Rect(old_pos, (tileWidth, tileWidth-2))
    new_rect = pygame.Rect(new_pos, (tileWidth, tileWidth-2))
    # 30, tileWidth-2
    i, j = from_coord_to_grid(new_pos)
    collide_later = list()
    blocks = get_neighbour_blocks(i, j)
    for block in blocks:
        if not new_rect.colliderect(block):
            continue
        dx_correction, dy_correction = compute_penetration(block, old_rect, new_rect)
        if dx_correction == 0.0:
            new_rect.top += dy_correction
            vy = 0.0
        elif dy_correction == 0.0:
            new_rect.left += dx_correction
            vx = 0.0
        else:
            collide_later.append(block)
 
    for block in collide_later:
        dx_correction, dy_correction = compute_penetration(block, old_rect, new_rect)
        if dx_correction == dy_correction == 0.0:
            continue
        if abs(dx_correction) < abs(dy_correction):
            dy_correction = 0.0
        elif abs(dy_correction) < abs(dx_correction):
            dx_correction = 0.0
        if dy_correction != 0.0:
            new_rect.top += dy_correction
            vy = 0.0
        elif dx_correction != 0.0:
            new_rect.left += dx_correction
            vx = 0.0
 
    x, y = new_rect.topleft
    return x, y, vx, vy
 
def compute_penetration(block, old_rect, new_rect):
    """Calcule a quel point mario est entré dans un bloc pour le repousser autant"""
    dx_correction = dy_correction = 0.0
    if old_rect.bottom <= block.top < new_rect.bottom:
        dy_correction = block.top  - new_rect.bottom
    elif old_rect.top >= block.bottom > new_rect.top:
        dy_correction = block.bottom - new_rect.top
    if old_rect.right <= block.left < new_rect.right:
        dx_correction = block.left - new_rect.right
    elif old_rect.left >= block.right > new_rect.left:
        dx_correction = block.right - new_rect.left
    return dx_correction, dy_correction

def fade(color, duration, txt=None):
    fade = pygame.Surface(taille_fenetre)
    fade.fill(color)
    for alpha in range(0, 255):
        fade.set_alpha(alpha)
        screen_surface.blit(fade, (0,0))
        if txt:
            texte = policeXL.render(txt, False, (255, 255, 255))
            texte.set_alpha(alpha)
            texte_rect = texte.get_rect(center=(taille_fenetre[0]/2, taille_fenetre[1]/2))
            screen_surface.blit(texte, texte_rect)
        pygame.display.update()
        pygame.time.delay(duration)
    
def themeMusic(musique):
    music.load(musique)
    music.play(-1)
    music.set_volume(0.75)

def mute():
    global muteGame
    pygame.event.clear()
    if muteGame:
        muteGame = False
        music.set_volume(0.75)
    else:
        muteGame = True
        music.set_volume(0)
     
def endLevel():
    global mobList, lvlNumber, score, scoreHighlight, inGame, marioX, marioY, previousScore
    mobList = []
    setLevels()
    lvlNumber += 1
    music.fadeout(1500)
    if lvlNumber in niveaux:
        score += 50
        fade((0,0,0), 10, "1 - " + str(lvlNumber))
        music.load(resource_path("fichiers/music/stage_clear.wav"))
        music.play()
        while music.get_busy() == True:
            continue
        marioX, marioY = getSpawnPoint(niveauActuel)
        scoreHighlight = 25
        previousScore = score
    else:
        score += 100
        fade((0,0,0), 10, "World Cleared")
        music.load(resource_path("fichiers/music/world_clear.wav"))
        music.play()
        while music.get_busy() == True:
            continue
        pygame.mixer.Sound(resource_path('fichiers/sound/congratulation.wav')).play().set_volume(0.6)
        inGame = False

def death():
    global lifeCount, niveauActuel, inGame, marioX, marioY, score, previousScore
    setLevels()
    lifeCount -= 1
    score = previousScore
    marioX, marioY = getSpawnPoint(niveauActuel)
    if lifeCount < 0:
        music.stop()
        music.load(resource_path('fichiers/music/game_over.ogg'))
        music.play()
        music.set_volume(0.7)
        fade((0,0,0), 12, "Game Over")
        inGame = False
    else:
        music.stop()
        music.load(resource_path('fichiers/music/death.wav'))
        music.play()
        music.set_volume(0.7)
        fade((0,0,0), 10)


## Menu principal
themeMusic(resource_path("fichiers/music/menu_theme.mp3"))
pygame.mixer.Sound(resource_path('fichiers/sound/itsmemario.mp3')).play().set_volume(0.6)
while not quitGame:
    # Variables à reset à chaque partie
    isDead = False
    isJumping = False
    score = 0
    previousScore = 0
    scoreHighlight = 0
    lvlNumber = 1
    lifeCount = 3
    mobList = []
    marioSide = "normal"
    marioVX, marioVY = 0, 0
    baseGravity = 3.5
    gravity = baseGravity
    
    clock.tick(30)
    KeysPressed = pygame.key.get_pressed()
    event = pygame.event.Event(pygame.USEREVENT)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame = True
    pygame.event.clear()
    
    screen_surface.blit(divers["menu"], (0,0))
    scoreTxt = policeS.render('Appuyer sur Espace pour commencer', False, (0, 0, 0))
    screen_surface.blit(scoreTxt,(taille_fenetre[0]/3, taille_fenetre[1]/1.5))

    optionTxt = policeS.render('(M) Play as Mario', False, (0, 0, 0))
    screen_surface.blit(optionTxt,(10, taille_fenetre[1]/4))
    optionTxt2 = policeS.render('(L) Play as Luigi', False, (0, 0, 0))
    screen_surface.blit(optionTxt2,(10, taille_fenetre[1]/3))
    optionTxt3 = policeS.render('(S) Mute music', False, (0, 0, 0))
    screen_surface.blit(optionTxt3,(10, taille_fenetre[1]/2.4))
    if (KeysPressed[pygame.K_SPACE] or KeysPressed[pygame.K_RETURN]):
        setLevels()
        niveauActuel = niveaux[1]
            
        music.fadeout(2400)
        fade((0,0,0), 8, "1 - " + str(lvlNumber))

        inGame = True
        marioX, marioY = getSpawnPoint(niveauActuel)
        
    elif KeysPressed[pygame.K_s]:
        mute()

    elif KeysPressed[pygame.K_l]:
        if not pygame.mixer.get_busy():
            pygame.mixer.Sound(resource_path('fichiers/sound/luigi-herewego.wav')).play()
        playLuigi = True
    elif KeysPressed[pygame.K_m]:
        if not pygame.mixer.get_busy():
            pygame.mixer.Sound(resource_path('fichiers/sound/mario-letsago.wav')).play()
        playLuigi = False

    ## Fenetre de jeu #########################################################
    if inGame:
        while inGame:
            clock.tick(30)
            KeysPressed = pygame.key.get_pressed()
            event = pygame.event.Event(pygame.USEREVENT)
            if lvlNumber == 2 or lvlNumber == 6:
                screen_surface.fill([1,9,38])
            else:
                screen_surface.fill([160,172,254])
            niveauActuel = niveaux[lvlNumber]
            dessiner_niveau(screen_surface, niveauActuel)

            if not muteGame and music.get_busy() != True:
                if lvlNumber == 6:
                    music.load(resource_path("fichiers/music/castle_theme.mp3"))
                else:
                    music.load(resource_path("fichiers/music/main_theme.ogg"))
                music.play(-1)

            if KeysPressed[pygame.K_m]:
                mute()
            
            if scoreHighlight > 0:
                scoreColor = (255,215,0)
                scoreHighlight -= 1
                police = policeL
            else:
                if lvlNumber == 2 or lvlNumber == 6:
                    scoreColor = (255, 255, 255)
                else:
                    scoreColor = (0,0,0)
                police = policeS
                
            lifeX = 5
            for i in range(lifeCount): # Compteur de vies
                screen_surface.blit(pygame.transform.scale(divers["greenChampi"], (20, 20)), (lifeX, 50))
                lifeX += 25

            scoreTxt = police.render('Score : ' + str(score), False, scoreColor)
            if lvlNumber == 2 or lvlNumber == 6:
                levelTxt = policeS.render('Level : ' + str(lvlNumber), False, (255, 255, 255))
            else:
                levelTxt = policeS.render('Level : ' + str(lvlNumber), False, (0, 0, 0))
            screen_surface.blit(scoreTxt,(5, 5))
            screen_surface.blit(levelTxt,(5, 25))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    inGame = False
                    
                elif event.type == pygame.KEYDOWN:
                    if marioVY == 0 and (event.key == pygame.K_z or event.key == pygame.K_UP or event.key == pygame.K_SPACE):
                        isJumping = True
                        pygame.mixer.Sound(resource_path('fichiers/sound/small_jump.ogg')).play().set_volume(0.5)
                    if (event.key == pygame.K_s or event.key == pygame.K_DOWN or event.key == pygame.K_LCTRL):
                        gravity *= 20
                        
                elif event.type == pygame.KEYUP:
                    if (event.key == pygame.K_s or event.key == pygame.K_DOWN or event.key == pygame.K_LCTRL):
                        gravity = baseGravity
        
            if isJumping:
                marioVY = -(tileWidth-4)
                isJumping = False
        
            if (KeysPressed[pygame.K_s] or KeysPressed[pygame.K_DOWN] or KeysPressed[pygame.K_LCTRL]):
                    marioSide = "crouched"
                    marioVX = 0
            elif (KeysPressed[pygame.K_q] or KeysPressed[pygame.K_LEFT]):
                if (KeysPressed[pygame.K_z] or KeysPressed[pygame.K_UP] or KeysPressed[pygame.K_SPACE]):
                    marioSide = "leftJump"
                else:
                    marioSide = "left"
            elif (KeysPressed[pygame.K_d] or KeysPressed[pygame.K_RIGHT]):
                if (KeysPressed[pygame.K_z] or KeysPressed[pygame.K_UP] or KeysPressed[pygame.K_SPACE]):
                    marioSide = "rightJump"
                else:
                    marioSide = "right"
            else:
                if (KeysPressed[pygame.K_z] or KeysPressed[pygame.K_UP] or KeysPressed[pygame.K_SPACE]):
                    marioSide = "normalJump"
                else:
                    marioSide = "normal"
            
            gridX,gridY=from_coord_to_grid((marioX, marioY))
            if gridY > len(niveauActuel)-3: # Retour au menu principal en cas de mort
                death()
            elif marioX < 0: # Empecher de sortir par la gauche
                marioX *= -1
        
            oldMarioX, oldMarioY = marioX, marioY
            if not (KeysPressed[pygame.K_s] or KeysPressed[pygame.K_DOWN] or KeysPressed[pygame.K_LCTRL]):
                marioVX = ((KeysPressed[pygame.K_d] or KeysPressed[pygame.K_RIGHT]) - (KeysPressed[pygame.K_q] or KeysPressed[pygame.K_LEFT])) * 5
            marioVY += gravity
            marioVY = min((tileWidth-5), marioVY)
            marioX += marioVX
            marioY += marioVY
            marioX, marioY, marioVX, marioVY = bloque_sur_collision((oldMarioX, oldMarioY), (marioX, marioY), marioVX, marioVY)
            marioRect = pygame.Rect((marioX, marioY), (30, 60))
            if playLuigi:
                screen_surface.blit(luigi[marioSide], (marioX, marioY-29))
            else:
                screen_surface.blit(mario[marioSide], (marioX, marioY-29))

        
            ## Fonctions spéciales des niveaux
            # IA des mobs
            for mob in mobList: # mob => [sprite, [x,y], [oldx,oldy], [vx,vy], speed, multi, mobId, [matriceX,matriceY]]
                mob[2][0] = mob[1][0]
                mob[3][0] = mob[4]*mob[5]
                mob[1][0] += mob[3][0]
                mob[1][0], mob[1][1], mob[3][0], mob[3][1] = bloque_sur_collision((mob[2][0],mob[1][1]), (mob[1][0],mob[1][1]), mob[3][0], 0)
                if mob[1][0] == mob[2][0]:
                    mob[5] *= -1
                # Sprites spécifiques
                if mob[6] == 100 or mob[6] == 101:
                    if mob[5] < 0:
                        mobsprite = blocs[100]
                    else:
                        mobsprite = blocs[101]
                else:
                    mobsprite = mob[0]
                screen_surface.blit(mobsprite, (mob[1][0], mob[1][1]))
                mobRect = pygame.Rect((mob[1][0], mob[1][1]), (tileWidth, tileWidth))
                
                if mob[6] == 100 or mob[6] == 101:
                    if marioRect.colliderect(mobRect):
                        if marioX+60 > mob[1][1] and marioY+60 < mob[1][1]+30: # Saut sur le haut du mob (y;y-25px)
                            pygame.mixer.Sound(resource_path('fichiers/sound/bump.ogg')).play()
                            score += 5
                            scoreHighlight = 25
                            mobList.remove(mob)
                            niveauActuel[mob[7][1]][mob[7][0]] = 0
                        else:
                            death()
                            break

            # Animation pieces
            if int(round(time.time() * 1000)) % 15 == 0:
                for row in niveauActuel:
                    if 7 in row:
                        row[:] = [x if x != 7 else 8 for x in row]
                    elif 8 in row:
                        row[:] = [x if x != 8 else 7 for x in row]
                    elif 16 in row:
                        row[:] = [x if x != 16 else 17 for x in row]
                    elif 17 in row:
                        row[:] = [x if x != 17 else 16 for x in row]
            
            nRow = 0
            for row in niveauActuel:
                # Drapeau / Porte / Peach
                if 5 in row or 20 in row or 21 in row or 31 in row or 37 in row or 38 in row or 41 in row:
                    pos = [i for i,x in enumerate(row) if x == 5 or x == 20 or x == 21 or x == 31 or x == 37 or x == 38 or x == 41]
                    for i in pos:
                        if marioRect.colliderect(pygame.Rect((i*32, nRow*32), (tileWidth, tileWidth))):
                            endLevel()
                            break

                # Tuyau
                if 25 in row or 26 in row:
                    pos = [i for i,x in enumerate(row) if x == 25 or x == 26]
                    for i in pos:
                        if (KeysPressed[pygame.K_s] or KeysPressed[pygame.K_DOWN] or KeysPressed[pygame.K_LCTRL]) and marioRect.colliderect(pygame.Rect((i*32, nRow*32), (tileWidth, tileWidth))):
                            pygame.mixer.Sound(resource_path('fichiers/sound/pipe.ogg')).play()
                            endLevel()

                # Pieces
                if (7 in row or 8 in row or 16 in row or 17 in row):
                    pos = [i for i,x in enumerate(row) if x == 7 or x == 8 or x == 16 or x == 17]
                    for i in pos:
                        if marioRect.colliderect(pygame.Rect((i*32, nRow*32), (tileWidth, tileWidth))):
                            pygame.mixer.Sound(resource_path('fichiers/sound/coin.ogg')).play().set_volume(0.6)
                            score += 10
                            scoreHighlight = 25
                            row[i] = 0

                # Champi vert
                if (28 in row):
                    pos = [i for i,x in enumerate(row) if x == 28]
                    for i in pos:
                        if marioRect.colliderect(pygame.Rect((i*32, nRow*32), (tileWidth, tileWidth))):
                            pygame.mixer.Sound(resource_path('fichiers/sound/one_up.ogg')).play().set_volume(0.6)
                            lifeCount += 1
                            row[i] = 0

                # Bowser
                if (32 in row or 33 in row or 34 in row):
                    pos = [i for i,x in enumerate(row) if x == 32 or x == 33 or x == 34]
                    for i in pos:
                        if marioRect.colliderect(pygame.Rect((i*32, nRow*32), (tileWidth, tileWidth))):
                            if marioX+60 > nRow*32 and marioY+60 < nRow*32+30:
                                pygame.mixer.Sound(resource_path('fichiers/sound/bump.ogg')).play()
                                score += 5
                                scoreHighlight = 100
                                row[:] = [x if x != 32 else 0 for x in row]
                                row[:] = [x if x != 34 else 0 for x in row]
                            else:
                                death()
                if (35 in row or 36 in row):
                    pos = [i for i,x in enumerate(row) if x == 35 or x == 36]
                    for i in pos:
                        if marioRect.colliderect(pygame.Rect((i*32, nRow*32), (tileWidth, tileWidth))):
                            if marioX+60 > nRow*32 and marioY+60 < nRow*32+30:
                                row[:] = [x if x != 35 else 0 for x in row]
                                row[:] = [x if x != 36 else 0 for x in row]

                nRow += 1

            pygame.display.flip()

    ###########################################################################
        music.fadeout(1500)
        fade((0,0,0), 8)
        if not muteGame:
            themeMusic(resource_path("fichiers/music/menu_theme.mp3"))
    pygame.display.flip()
    

## Fermer la fenêtre
music.fadeout(1500)
pygame.mixer.Sound(resource_path('fichiers/sound/buhbye.mp3')).play()
fade((0,0,0), 5)
pygame.quit()