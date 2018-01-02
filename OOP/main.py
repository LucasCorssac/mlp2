import pygame
import enemie
import board
import tower
#from pygame.locals import *

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

        #Tower attributes
        self._tower_list = []

    def start(self):
        pygame.init()
        self._display = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Main Menu")
        self._inimigo = enemie.Enemie(self._display)
        self._inimigo2 = enemie.Enemie(self._display)
        self._inimigo3 = enemie.Enemie(self._display)
        self._enemie_list = (self._inimigo, self._inimigo2, self._inimigo3)
        self._enemie_list_len = len(self._enemie_list)
        self._start_wave = False



        while not self._endgame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._endgame = True
                
                #CATCHES MOUSE CLICK EVENT
                if event.type == pygame.locals.MOUSEBUTTONDOWN:
                    tower = Tower(self._display)
                    self._tower_list.append(tower)

            cont = 0
            for e in self._enemie_list:
                if e.is_active():
                    cont = cont+1
            if cont == 0:
                self._start_wave = False

            if self._start_wave:
                now = pygame.time.get_ticks()
                if self._enemie_list[0].is_active():
                    self._enemie_list[0].logic()
                if self._enemie_list[1].is_active() and now - self._last >= self._cooldown:
                    self._enemie_list[1].logic()
                if self._enemie_list[2].is_active() and now - self._last >= self._cooldown+200:
                    self._enemie_list[2].logic()

            self._clock.tick(50)
            self.update_screen()


    def update_screen(self):
        self._print_background(self._display)
        self._board.draw_board(self._display, 1)
        for e in self._enemie_list:
            if e.is_active():
                e.update()
        #self._enemie_list[0].update()
        #self._enemie_list[1].update()
        #self._enemie_list[2].update()
        green = (0, 200, 0)
        bright_green = (0, 255, 0)
        self.button("Wave: "  + str(self._inimigo.get_level()), 150, 450, 100, 50, green, bright_green)
        pygame.display.update()
        print(self._enemie_list[0].get_pos(), self._inimigo.is_active(), self._start_wave)

    def _set_start_wave(self):
        if not self._start_wave:
            self._last = pygame.time.get_ticks()
            self._enemie_list[0].set_active()
            self._enemie_list[1].set_active()
            self._enemie_list[2].set_active()
            self._start_wave = True

    def _print_background(self, display):
        display.blit(pygame.image.load("img/fundo_jogo.png"), (0, 0))

    def button(self, msg, x, y, w, h, ic, ac):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(self._display, ac, (x, y, w, h))
            if click[0] == 1 and not self._start_wave:
                self._set_start_wave()
                for e in self._enemie_list:
                    e.set_active()
        else:
            pygame.draw.rect(self._display, ic, (x, y, w, h))

        small_text = pygame.font.SysFont("comicsansms", 20)
        text_surf, text_rect = self.text_objects(msg, small_text)
        text_rect.center = ((x + (w / 2)), (y + (h / 2)))
        self._display.blit(text_surf, text_rect)

    def text_objects(self, text, font):
        text_surface = font.render(text, True, (0,0,0,0))
        return text_surface, text_surface.get_rect()

inicio = Main()
inicio.start()