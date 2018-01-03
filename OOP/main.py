import pygame
import enemie
import board
from td_game_ui import *
from tower import *
import config
import player

class Main:
    def __init__(self):
        self._display = None
        self._endgame = False
        self._enemie_list = []
        self._clock = pygame.time.Clock()
        self._inimigo = None
        self._last = pygame.time.get_ticks()
        self._cooldown = 200 #0.3seconds
        self._i = 0
        self._wave_number = 1
        self._board = board.Board()
        # PLAYER
        self._player = player.Player()

        # MENU
        self._option_list = [(True, (35, 710)),
                             (False, (135, 710)),
                             (False, (235, 710))]

        #Tower attributes
        self._tower_list = []


        #UI attributes
         
        self._wave_button = Button(pygame.Rect(680, 250, 100, 50), "Wave")
        self._ui_elements_list = []
        self._gold_stats = Stats(pygame.Rect(740, 98, 0, 0), str(self._player.get_gold()))
        self._life_stats = Stats(pygame.Rect(740, 48, 0, 0), str(self._player.get_life()))

    def start(self):
        pygame.init()
        self._display = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Main Menu")
        self._inimigo = enemie.Enemie(self._display)
        self._inimigo2 = enemie.Enemie(self._display)
        self._inimigo3 = enemie.Enemie(self._display)
        self._enemie_list = [self._inimigo, self._inimigo2, self._inimigo3]
        self._enemie_list_len = len(self._enemie_list)
        self._start_wave = False

        while not self._endgame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._endgame = True
                
                #CATCHES MOUSE CLICK EVENT
                if event.type == pygame.MOUSEBUTTONUP:
                    if self._wave_button.get_rect().collidepoint(event.pos):
                        if not self._start_wave:
                            self._set_start_wave()
                        for e in self._enemie_list:
                            e.set_active()
                    else:
                        tower = None
                        if self._option_list[0][0]:
                            tower = Tower(self._display)
                        if tower != None and self._player.get_gold() >= tower.get_price() and self.on_board(event.pos):
                            self._player.set_gold(self._player.get_gold() - tower.get_price())
                            tower._pos = event.pos
                            self._tower_list.append(tower)

            cont = 0
            for e in self._enemie_list:
                if e.is_active():
                    cont = cont+1
            if cont == 0:
                self._start_wave = False
                for e in self._enemie_list:
                    e.go_to_start_pos()



            if self._start_wave:
                now = pygame.time.get_ticks()
                if self._enemie_list[0].is_active():
                    self._enemie_list[0].logic()
                if self._enemie_list[1].is_active() and now - self._last >= self._cooldown:
                    self._enemie_list[1].logic()
                if self._enemie_list[2].is_active() and now - self._last >= self._cooldown+200:
                    self._enemie_list[2].logic()

            #COMPUTE TOWER ATTACKS
            for _tower in self._tower_list:
                #LIST MUST START EMPTY NOT TO STACK ATTACKS FROM PREVIOUS CYCLES
                _tower._attack_list = []
                for _enemy in self._enemie_list:
                    #ONLY ATTACK IF THE ENEMY IS IN RANGE AND THERE ARE ATTACKS LEFT (MAX ATTACKS = LEVEL OF TOWER)
                    if _tower._distance_to(_enemy) <= _tower._range and len(_tower._attack_list) < tower._level and _enemy.is_active():
                        _tower._attack_list.append(_enemy._pos)
                        _enemy._health -= _tower._damage
                        if _enemy._health <= 0:
                            _enemy.set_not_active()
                            self._player.set_gold(self._player.get_gold()+_enemy.get_reward())


            
            self.draw_screen()
            self._clock.tick(50)


    def draw_screen(self):
        self._print_background(self._display)
        self._board.draw_board(self._display, 1)
        
        #DRAW ENEMIES
        for e in self._enemie_list:
            if e.is_active():
                e.draw()

        #DRAW TOWERS
        for _tower in self._tower_list:
            _tower.draw()

        #DRAW GOLD
        self._gold_stats.set_text(str(self._player.get_gold()))
        self._gold_stats.draw(self._display)
        #DRAW LIFE
        life = 0
        for e in self._enemie_list:
            life += e.get_attacking()
        self._life_stats.set_text(str(self._player.get_life()-life))
        self._life_stats.draw(self._display)

        #self._enemie_list[0].update()
        #self._enemie_list[1].update()
        #self._enemie_list[2].update()

        #DRAW UI ELEMENTS

        #DRAW "WAVE" BUTTON
        self._wave_button.set_text("Wave: " + str(self._inimigo.get_level()))
        self._wave_button.draw(self._display)
        pygame.display.update()


        #print(self._enemie_list[0].get_pos(), self._inimigo.is_active(), self._start_wave)
        

    def _set_start_wave(self):
        if not self._start_wave:
            self._last = pygame.time.get_ticks()
            self._enemie_list[0].set_active()
            self._enemie_list[1].set_active()
            self._enemie_list[2].set_active()
            self._start_wave = True

    def _print_background(self, display):
        display.blit(pygame.image.load("img/fundo_jogo.png"), (0, 0))
        display.blit(pygame.image.load("img/tower1.png"),(70, 700))
        display.blit(pygame.image.load("img/icetower1.png"), (170, 700))
        display.blit(pygame.image.load("img/firetower1.png"), (270, 700))
        display.blit(pygame.image.load("img/tower1.png"), (70, 700))
        for e in self._option_list:
            self._print_button(e[0], e[1])

    def _print_button(self, bool, pos):
        if bool:
            self._display.blit(pygame.image.load("img/on.png"), pos)
        else:
            self._display.blit(pygame.image.load("img/off.png"), pos)

    def on_board(self, pos):
        if 620 >= pos[0] >= 60 and 620 >= pos[1] >= 60:
            return True
        else:
            return False




inicio = Main()
inicio.start()