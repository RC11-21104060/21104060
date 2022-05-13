import pygame,sys

class Cell:
    def __init__(self, type, rect, location, fertility = 1):
        self.type = type
        self.rect = rect
        self.location = location
        #self.fertility = fertility
        self.x = self.location[0]
        self.y = self.location[1]

        if self.type == 'dead':
            self.colour = pygame.Color(0,0,0)
        elif self.type == 'solornonsseal':
            self.colour = pygame.Color(255,192,203)
        elif self.type == 'lamier jaune':
            self.colour = pygame.Color(135,38,87)
        elif self.type == 'Algerian Iris':
            self.colour = pygame.Color(250,128,114)
        elif self.type == 'solidago vir':
            self.colour = pygame.Color(255,69,0)
        elif self.type == 'Lierre gri':
            self.colour = pygame.Color(210,180,140)
        elif self.type == 'Sureau rou':
            self.colour = pygame.Color(244,164,96)
        elif self.type == 'Nerprun al':
            self.colour = pygame.Color(139,69,19)
        elif self.type == 'Prunelier':
            self.colour = pygame.Color(188,143,143)
        elif self.type == 'Tamaris de France':
            self.colour = pygame.Color(255,125,64)
        elif self.type == 'Tamaris Afrique':
            self.colour = pygame.Color(128,42,42)
        elif self.type == 'Sureau noir':
            self.colour = pygame.Color(255,142,85)
        elif self.type == 'Sumac de Virginie':
            self.colour = pygame.Color(176,224,230)
        elif self.type == 'Large-leaved':
            self.colour = pygame.Color(65,105,225)
        elif self.type == 'European ash':
            self.colour = pygame.Color(42,224,208)
        elif self.type == 'Sycamore maple':
            self.colour = pygame.Color(189,252,201)
        elif self.type == 'Beech':
            self.colour = pygame.Color(107,142,35)
        elif self.type == 'Sessile oak':
            self.colour = pygame.Color(221,160,221)
        elif self.type == 'Pedunculate oak':
            self.colour = pygame.Color(160,102,211)

        else:
            self.colour = pygame.Color(51,161,201)

    def changeType(self, type):
        self.type = type
        if self.type == 'dead':
            self.colour = pygame.Color(0,0,0)
        elif self.type == 'solornons seal':
            self.colour = pygame.Color(255,192,203)
        elif self.type == 'lamier jaune':
            self.colour = pygame.Color(135,38,87)
        elif self.type == 'Algerian Iris':
            self.colour = pygame.Color(250,128,114)
        elif self.type == 'solidago vir':
            self.colour = pygame.Color(255,69,0)
        elif self.type == 'Lierre gri':
            self.colour = pygame.Color(210,180,140)
        elif self.type == 'Sureau rou':
            self.colour = pygame.Color(244,164,96)
        elif self.type == 'Nerprun al':
            self.colour = pygame.Color(139,69,19)
        elif self.type == 'Prunelier':
            self.colour = pygame.Color(188,143,143)
        elif self.type == 'Tamaris de France':
            self.colour = pygame.Color(255,125,64)
        elif self.type == 'Tamaris Afrique':
            self.colour = pygame.Color(128,42,42)
        elif self.type == 'Sureau noir':
            self.colour = pygame.Color(255,142,85)
        elif self.type == 'Sumac de Virginie':
            self.colour = pygame.Color(176,224,230)
        elif self.type == 'Large-leaved':
            self.colour = pygame.Color(65,105,225)
        elif self.type == 'European ash':
            self.colour = pygame.Color(42,224,208)
        elif self.type == 'Sycamore maple':
            self.colour = pygame.Color(189,252,201)
        elif self.type == 'Beech':
            self.colour = pygame.Color(107,142,35)
        elif self.type == 'Sessile oak':
            self.colour = pygame.Color(221,160,221)
        elif self.type == 'Pedunculate oak':
            self.colour = pygame.Color(160,102,211)
