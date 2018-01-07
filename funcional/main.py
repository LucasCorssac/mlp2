import pygame
import enemie
import board
from td_game_ui import *
import tower
import config
import player
import menu
import sound
from lists import *

class Main:
    def __init__(self):
        self._display = None
        self._endgame = False
        self._game_over = False
        self._enemie_list = []
        self._clock = pygame.time.Clock()
        self._inimigo = None
        self._last = pygame.time.get_ticks()
        self._i = 0
        self._wave_number = 1
        self._cooldown = 4000 #0.2seconds
        self._board = board.Board()
        # PLAYER
        self._player = player.Player()

        # MENU
        self._option_list = [[True, (76, 750), 1],
                             [False, (176, 750), 2],
                             [False, (276, 750), 3]]

        #Tower attributes
        self._tower_list = []
        self._example_tower = tower.Tower(self._display,1)
        self._tower_attributes = [Stats(pygame.Rect(580, 700, 0, 0), "Level " + str(self._example_tower.get_level()) + " Stats"),
                                  Stats(pygame.Rect(580, 712, 0, 0), "Damage: " + str(self._example_tower.get_damage())),
                                  Stats(pygame.Rect(580, 724, 0, 0), "Range: " + str(self._example_tower.get_range())),
                                  Stats(pygame.Rect(580, 736, 0, 0), "Price: " + str(self._example_tower.get_price())+"$"),
                                  Stats(pygame.Rect(580, 748, 0, 0), "Upgrade: " + str(self._example_tower.get_upgrade_price())+"$")]

        self._tower_next_attributes = [Stats(pygame.Rect(710, 700, 0, 0), "Level " + str(self._example_tower.get_next_level()) + " Stats"),
                                       Stats(pygame.Rect(710, 712, 0, 0), "Damage: " + str(self._example_tower.get_next_damage())),
                                       Stats(pygame.Rect(710, 724, 0, 0), "Range: " + str(self._example_tower.get_next_range())),
                                       Stats(pygame.Rect(710, 736, 0, 0), "Price: " + str(self._example_tower.get_next_price())+"$"),
                                       Stats(pygame.Rect(710, 748, 0, 0), "Upgrade: " + str(self._example_tower.get_next_upgrade_price())+"$")]

        self._tower_level = 1
        self._poisontower_level = 1
        self._firetower_level = 1



        #UI attributes
        self._not_muted = True
        self._mute_button_image = pygame.image.load("img/audio_button.png")
         
        self._wave_button = Stats(pygame.Rect(690, 135, 90, 30), "")
        self._wave_number_display = Stats(pygame.Rect(690, 165, 90, 30), "Wave")
        self._sound_button = Stats(pygame.Rect(730, 195, 50, 50), "")
        self._ui_elements_list = []
        self._gold_stats = Stats(pygame.Rect(740, 98, 0, 0), str(self._player.get_gold()))
        self._life_stats = Stats(pygame.Rect(740, 48, 0, 0), str(self._player.get_life()))





    def start(self):
        pygame.init()
        sound.Sound.stop_BGM(self)
        sound.Sound.play_BGM(self, config.Config.GAME_BGM)
        self._display = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("py.defense")

        self._inimigo = enemie.Enemie(self._display)
        self._inimigo2 = enemie.Enemie(self._display)
        self._inimigo3 = enemie.Enemie(self._display)
        self._inimigo4 = enemie.Enemie(self._display)
        self._inimigo5 = enemie.Enemie(self._display)

        self._enemie_list = [self._inimigo, self._inimigo2, self._inimigo3, self._inimigo4, self._inimigo5]
        self._enemie_list_len = len(self._enemie_list)
        self._start_wave = False

        while not self._endgame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._endgame = True
                #CATCHES MOUSE CLICK EVENT

                if event.type == pygame.MOUSEBUTTONUP:
                    self.tower_option(event.pos)
                    if self._wave_button.get_rect().collidepoint(event.pos):
                        if not self._start_wave:
                            self._set_start_wave()

                        for e in self._enemie_list:
                            e.set_active()
                    else:
                        tower_create = None
                        if self._sound_button.get_rect().collidepoint(event.pos):
                            if self._not_muted:
                                sound.Sound.stop_BGM(self)
                                self._mute_button_image = pygame.image.load("img/audio_button_x.png")
                                self._not_muted = False
                            else:
                                sound.Sound.start_BGM(self)
                                self._mute_button_image = pygame.image.load("img/audio_button.png")
                                self._not_muted = True
                        if self._option_list[0][0]:
                            if self.on_upgrade_button(event.pos) and self._player.get_gold() >= (200 + (self._tower_level-1)*100):
                                self._tower_level += 1
                                tower_create = tower.Tower(self._display, self._tower_level)
                                self.update_tower_attributes(tower_create)
                                self.update_tower_next_attributes(tower_create)
                            else:
                                tower_create = tower.Tower(self._display, self._tower_level)
                                self.update_tower_attributes(tower_create)
                                self.update_tower_next_attributes(tower_create)
                        if self._option_list[1][0]:
                            if self.on_upgrade_button(event.pos) and self._player.get_gold() >= (250 + (self._poisontower_level-1)*150):
                                self._poisontower_level += 1
                                tower_create = tower.PoisonTower(self._display, self._poisontower_level)
                                self.update_tower_attributes(tower_create)
                                self.update_tower_next_attributes(tower_create)
                            else:
                                tower_create = tower.PoisonTower(self._display, self._poisontower_level)
                                self.update_tower_attributes(tower_create)
                                self.update_tower_next_attributes(tower_create)
                        if self._option_list[2][0]:
                            if self.on_upgrade_button(event.pos) and self._player.get_gold() >= (300 + (self._firetower_level-1)*180):
                                self._firetower_level += 1
                                tower_create = tower.FireTower(self._display, self._firetower_level)
                                self.update_tower_attributes(tower_create)
                                self.update_tower_next_attributes(tower_create)
                            else:
                                tower_create = tower.FireTower(self._display, self._firetower_level)
                                self.update_tower_attributes(tower_create)
                                self.update_tower_next_attributes(tower_create)

                        if self.on_upgrade_button(event.pos) and (self._player.get_gold() >= tower_create.get_upgrade_price()):
                            sound.Sound.play_Sound(self, config.Config.UPGRADE_SOUND)
                            self._player.set_gold(self._player.get_gold() - tower_create.get_upgrade_price())
                            tower_create.upgrade_level()
                        if tower_create != None and self._player.get_gold() >= tower_create.get_price() and self.on_board(event.pos):
                            sound.Sound.play_Sound(self, config.Config.BUILD_SOUND)
                            self._player.set_gold(self._player.get_gold() - tower_create.get_price())
                            tower_create._pos = event.pos
                            self._tower_list.append(tower_create)

            if self._start_wave:
                cont = 0
                for e in self._enemie_list:
                    if e.is_active():
                        cont = cont + 1
                        if e._health <= 0:
                            e.set_not_active()
                            self._player.set_gold(self._player.get_gold()+e.get_reward())
                if cont == 0:
                    self._start_wave = False
                    for e in self._enemie_list:
                        e.go_to_start_pos()
                now = pygame.time.get_ticks()
                if self._enemie_list[0].is_active():
                    self._enemie_list[0].logic()
                if self._enemie_list[1].is_active() and now - self._last >= 1*self._cooldown/self._inimigo2.get_speed():
                    self._enemie_list[1].logic()
                if self._enemie_list[2].is_active() and now - self._last >= 2*self._cooldown/self._inimigo3.get_speed():
                    self._enemie_list[2].logic()
                if self._enemie_list[3].is_active() and now - self._last >= 3*self._cooldown/self._inimigo4.get_speed():
                    self._enemie_list[3].logic()
                if self._enemie_list[4].is_active() and now - self._last >= 4*self._cooldown/self._inimigo5.get_speed():
                    self._enemie_list[4].logic()

            #COMPUTE TOWER ATTACKS
            for _tower in self._tower_list:
                #LIST MUST START EMPTY NOT TO STACK ATTACKS FROM PREVIOUS CYCLES
                _tower.attack_enemies(self._enemie_list)

            self.draw_screen()
            if int(self._life_stats.get_text()) <= 0:
                self._display.blit(pygame.image.load("img/gameover.png"), (84, 300))
                self.game_over()
            self._clock.tick(50)


    def draw_screen(self):
        self._print_background(self._display)
        self._board.draw_board(self._display, 1)
        #FUNCT
        def draw_enem(list):
            if len(list) > 0:
                if first(list).is_active():
                    first(list).draw()
                draw_enem(rest(list))
        #FUNCT
        def draw_towers(list):
            if len(list)>0:
                first(list).draw()
                draw_towers(rest(list))
        #DRAW ENEMIES
        draw_enem(self._enemie_list)

        for e in self._option_list:
            self._print_button(e[0], e[1])
        #DRAW TOWERS
        draw_towers(self._tower_list)

        #DRAW GOLD
        self._gold_stats.set_text(str(self._player.get_gold()))
        self._gold_stats.draw(self._display)

        #FUNCT
        #DRAW TOWER ATTRIBUTES
        def draw_att(list):
            if len(list) > 0:
                first(list).draw(self._display)
                draw_att(rest(list))

        draw_att(self._tower_attributes)
        #DRAW TOWER NEXT ATTRIBUTES
        draw_att(self._tower_next_attributes)



        #DRAW TOWER NEXT ATTRIBUTES ARROW
        self._display.blit(pygame.image.load("img/seta.png"), (635, 717))

        #DRAW UPGRADE BUTTON
        self._display.blit(pygame.image.load("img/upgrade.png"), (595, 760))

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

        #DRAW SOUND BUTTON
        self._display.blit(self._mute_button_image, (730, 195))

        #DRAW "WAVE" BUTTON
        self._wave_number_display.set_text("Wave nº: " + str(self._inimigo.get_level()))
        self._wave_number_display.draw(self._display)
        self._wave_button.draw(self._display)
        pygame.display.update()


        #print(self._enemie_list[0].get_pos(), self._inimigo.is_active(), self._start_wave)
        

    def _set_start_wave(self):
        if not self._start_wave:
            self._start_wave = True
            self._last = pygame.time.get_ticks()

    def _print_background(self, display):
        display.blit(pygame.image.load("img/fundo_jogo.png"), (0, 0))
        display.blit(pygame.image.load("img/tower1.png"),(70, 700))
        display.blit(pygame.image.load("img/poisontower1.png"), (170, 700))
        display.blit(pygame.image.load("img/firetower1.png"), (270, 700))
        display.blit(pygame.image.load("img/tower1.png"), (70, 700))

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

    def tower_option(self, pos):
        if 120 >= pos[0] >= 70 and 750 >= pos[1] >= 700:
            sound.Sound.play_Sound(self, config.Config.SWITCH_SOUND)
            self.set_option(self._option_list,1)
        if 220 >= pos[0] >= 170 and 750 >= pos[1] >= 700:
            sound.Sound.play_Sound(self, config.Config.SWITCH_SOUND)
            self.set_option(self._option_list,2)
        if 320 >= pos[0] >= 270 and 750 >= pos[1] >= 700:
            sound.Sound.play_Sound(self, config.Config.SWITCH_SOUND)
            self.set_option(self._option_list,3)
    #FUNCT
    def set_option(self,list,x):
        if len(list) > 0:
            if first(list)[2] == x:
                first(list)[0] = True
            else:
                first(list)[0] = False
            self.set_option(rest(list),x)

    def update_tower_attributes(self, one_tower):
        self._tower_attributes[0].set_text("Level " + str(one_tower.get_level()) + " Stats")
        self._tower_attributes[1].set_text("Damage: " + str(one_tower.get_damage()))
        self._tower_attributes[2].set_text("Range: " + str(one_tower.get_range()))
        self._tower_attributes[3].set_text("Price: " + str(one_tower.get_price())+"$")
        self._tower_attributes[4].set_text("Upgrade: " + str(one_tower.get_upgrade_price())+"$")

    def update_tower_next_attributes(self, one_tower):
        self._tower_next_attributes[0].set_text("Level " + str(one_tower.get_next_level()) + " Stats")
        self._tower_next_attributes[1].set_text("Damage: " + str(one_tower.get_next_damage()))
        self._tower_next_attributes[2].set_text("Range: " + str(one_tower.get_next_range()))
        self._tower_next_attributes[3].set_text("Price: " + str(one_tower.get_next_price())+"$")
        self._tower_next_attributes[4].set_text("Upgrade: " + str(one_tower.get_next_upgrade_price())+"$")

    def on_upgrade_button(self, pos):
        if 695 >= pos[0] >= 595 and 790 >= pos[1] >= 760:
            return True
        else:
            return False

    def game_over(self):
        while not self._game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._game_over = True
                    self._endgame = True

            pygame.display.update()





start_sounds = sound.Sound()
main_menu = menu.Menu()
inicio = Main()
print (pygame.font.get_fonts())
main_menu.start()
if main_menu.get_start_game():
    inicio.start()