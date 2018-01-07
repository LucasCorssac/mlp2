import pygame, sys
from pygame.locals import *
import math

#Set up pygame.
pygame.init()
mainClock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Set up the window.
windowSurface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),0, 32) #last param, depth = 32
pygame.display.set_caption("Tower Defense")

#Set up the colors.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0,200,0)
BLUE = (0,0,255)
ORANGE = (255, 125, 0)
CYAN = (0, 255, 255)
BROWN = (200, 125, 100)

#Set up the fonts.
basicFont = pygame.font.SysFont(None, 48)

#Set up the text.
text = basicFont.render('Hello world!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

#Draw the white background onto the surface
windowSurface.fill(WHITE)

#Draw a green polygon onto the surface.
# pygame.draw.polygon(windowSurface, GREEN, ((146,0),   (291, 106),
#                                            (236,277), (56, 277),   (0, 106)  
#                                            ))

#Draw some blue lines onto the surface
# pygame.draw.line(windowSurface, BLUE, (60,60), (120, 60), 4)
# pygame.draw.line(windowSurface, BLUE, (120,60), (60, 120))
# pygame.draw.line(windowSurface, BLUE, (60,120), (120, 120), 4)

# Draw a blue circle onto the surface.
# pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)

# Draw a red ellipse onto the surface
# pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

#Draw the text's background rectangle onto the surface.
pygame.draw.rect(windowSurface, RED, (0,0, 10, 10))

# #Get a pixel array of the surface.
# pixArray = pygame.PixelArray(windowSurface)
# pixArray[480][380] = BLACK
# del pixArray


#Draw the text onto the surface.
# windowSurface.blit(text, textRect)

#Draw the window onto the screen.

def distance(pos1, pos2):
    p1x, p1y = pos1
    p2x, p2y = pos2
    x = p1x - p2x
    y = p1y - p2y
    result = math.sqrt(math.pow(x,2) + math.pow(y,2))
    return result

MOVE_SPEED = 5

#trail
point0 =          (0,0)
point1 =          (200, 0)
point2 =          (200, 200)
point3 =          (0, 200)
point4 =          (0, 500)
point5 =          (500,500)
point6 =          (500, 300)
point7 =          (300,300)
point8 =          (300,400)
point9 =          (600,400)
point_final =     (600,0)




trail = [point1, point2, point3, point4, point5, point6, point7, point8, point9, point_final]
trail0 = [point0] + trail

def make_trail_direction(i):
    px,py = trail0[i]
    dx,dy = trail0[i+1]
    if px == dx:
        if dy < py:
            return 'u'
        elif dy > py:
            return 'd'
    elif py == dy:
        if dx < px:
            return 'l'
        elif dx > px:
            return 'r'

    
trail_direction = [s for s in map(make_trail_direction, range(len(trail)))]

#trail_direction = ['r', 'd', 'l', 'd', 'r', 'u', 'l','d', 'r', 'u']

ROAD_WIDTH = 30

#Rect((left, top), (width, height))

def make_trail_drawing(i):
    if trail_direction[i] == 'l':
        return pygame.Rect(trail0[i+1], (distance(trail0[i], trail0[i+1]) + ROAD_WIDTH, ROAD_WIDTH) )
    elif trail_direction[i] == 'd':
        return pygame.Rect(trail0[i], (ROAD_WIDTH, distance(trail0[i], trail0[i+1]) ) )
    elif trail_direction[i] == 'r':
        return pygame.Rect(trail0[i], (distance(trail0[i], trail0[i+1]), ROAD_WIDTH) )
    elif trail_direction[i] == 'u':
        return pygame.Rect(trail0[i+1], (ROAD_WIDTH, distance(trail0[i], trail0[i+1]) + ROAD_WIDTH ))

trail_drawings_list = [make_trail_drawing(i) for i in range(len(trail))]



DOWNRIGHT = 0
ENEMY_SIZE = 20

enemy = {'rect': pygame.Rect(0, 0, ENEMY_SIZE, ENEMY_SIZE),
      'color': GREEN,
      'dir': DOWNRIGHT,
      'trail_point': 0,
      'health': 200
      }

enemy_list = [enemy]

TOWER_SIZE = 10
TOWER_RANGE = 50
TOWER_DAMAGE = 10

tower_list = []





def update_enemy_path(enemy):
    
    trail_point = enemy['trail_point']

    if trail_point >= len(trail):
        return
    
    destination = trail[trail_point]
    destination_x = destination[0]
    destination_y = destination[1]

    enemy_direction = trail_direction[trail_point]

    enemy_pos_x = enemy['rect'].left
    enemy_pos_y = enemy['rect'].top


    if enemy_direction == 'l':
        if enemy_pos_x <= destination_x:
            enemy['trail_point'] +=1
    elif enemy_direction == 'd':
        if enemy_pos_y >= destination_y:
            enemy['trail_point'] +=1
    elif enemy_direction == 'r':
        if enemy_pos_x >= destination_x:
            enemy['trail_point'] +=1
    elif enemy_direction == 'u':
        if enemy_pos_y <= destination_y:
            enemy['trail_point'] +=1


def update_enemy_position(enemy):
    trail_point = enemy['trail_point']
    
    if trail_point >= len(trail_direction):
        return
    
    enemy_direction = trail_direction[trail_point]
    
    if enemy_direction == 'l':
        enemy['rect'].left -= MOVE_SPEED
    elif enemy_direction == 'd':
        enemy['rect'].bottom += MOVE_SPEED
    elif enemy_direction == 'r':
        enemy['rect'].right += MOVE_SPEED
    elif enemy_direction == 'u':
        enemy['rect'].top -= MOVE_SPEED

def update_enemy():
    for enemy in enemy_list[:]:
        update_enemy_path(enemy)
        update_enemy_position(enemy)
        if enemy['health'] <= 0:
            enemy_list.remove(enemy)
    


def distance(pos1, pos2):
    p1x, p1y = pos1
    p2x, p2y = pos2
    x = p1x - p2x
    y = p1y - p2y
    result = math.sqrt(math.pow(x,2) + math.pow(y,2))
    return result

laser_list = []

def attack_tower():
    for tower in tower_list:
        tower_pos = tower['rect'].center
        for enemy in enemy_list:
            enemy_pos = enemy['rect'].center
            if (distance(enemy_pos, tower_pos) <= TOWER_RANGE):
                laser = (tower_pos, enemy_pos)
                laser_list.append(laser)
                enemy['health'] -= TOWER_DAMAGE
                
def draw_trail():
    for trail_drawing in trail_drawings_list:
        pygame.draw.rect(windowSurface, BROWN, trail_drawing)


def draw_enemies():
    for enemy in enemy_list:
        pygame.draw.rect(windowSurface, RED, enemy['rect'])
    

def draw_towers():
    for tower in tower_list:
        pygame.draw.rect(windowSurface, CYAN, tower['rect'])

def draw_lasers():
    while laser_list:
        p1,p2 = laser_list.pop()
        pygame.draw.line(windowSurface, ORANGE, p1, p2, 4)        

def draw():
    draw_trail()
    draw_enemies()
    draw_towers()
    draw_lasers()


#Run the game loop.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            tower = {}
            tower['rect'] = pygame.Rect(0,0, TOWER_SIZE, TOWER_SIZE)
            tower['rect'].center = event.pos
            tower_list.append(tower)
    update_enemy()
    attack_tower()
    windowSurface.fill(GREEN)
    draw()
    pygame.display.update()
    mainClock.tick(40)