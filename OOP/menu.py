import pygame
import config


class Menu:
    def __init__(self):
        self._display = None
        self._start_game = False
        self._collide_new_game = False
        self._collide_quick_game = False
        self._collide_create_map = False
        self._collide_exit_game = False
        self._exit_menu = False

    def _display_text(self):
        pass

    def _display_menu_back_image(self):
        main_menu_back_image = pygame.image.load(config.Config.MENU_BACK_IMAGE)
        self._display.blit(main_menu_back_image, (0, 0))

    def _display_title(self):
        title = pygame.image.load(config.Config.TITLE_IMAGE)
        self._display.blit(title, (145, 50))

    def _display_options(self):

        x, y = pygame.mouse.get_pos()

        option_new_game = pygame.image.load(config.Config.MENU_OPTION_NEW_GAME)
        option_quick_game = pygame.image.load(config.Config.MENU_OPTION_QUICK_GAME)
        option_create_map = pygame.image.load(config.Config.MENU_OPTION_CREATE_MAP)
        option_exit_game = pygame.image.load(config.Config.MENU_OPTION_EXIT_GAME)

        option_new_game_2 = pygame.image.load(config.Config.MENU_OPTION_NEW_GAME_2)
        option_quick_game_2 = pygame.image.load(config.Config.MENU_OPTION_QUICK_GAME_2)
        option_create_map_2 = pygame.image.load(config.Config.MENU_OPTION_CREATE_MAP_2)
        option_exit_game_2 = pygame.image.load(config.Config.MENU_OPTION_EXIT_GAME_2)

        if self._collide_new_game:
            self._display.blit(option_new_game_2, (275, 250))
        else:
            self._display.blit(option_new_game, (275, 250))

        if self._collide_quick_game:
            self._display.blit(option_quick_game_2, (275, 325))
        else:
            self._display.blit(option_quick_game, (275, 325))

        if self._collide_create_map:
            self._display.blit(option_create_map_2, (275, 400))
        else:
            self._display.blit(option_create_map, (275, 400))

        if self._collide_exit_game:
            self._display.blit(option_exit_game_2, (275, 475))
        else:
            self._display.blit(option_exit_game, (275, 475))

    def _update_screen(self):
        self._display_menu_back_image()
        self._display_options()
        self._display_title()

    def _option_select(self):
        x, y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == (1, 0, 0) and (275 < x < 525)and(250 < y < 310):
            self._new_game_option()
        if pygame.mouse.get_pressed() == (1, 0, 0) and (275 < x < 525)and(325 < y < 385):
            self._quick_game_option()
        if pygame.mouse.get_pressed() == (1, 0, 0) and (275 < x < 525)and(400 < y < 460):
            self._create_map_option()
        if pygame.mouse.get_pressed() == (1, 0, 0) and (275 < x < 525)and(475 < y < 535):
            self._exit_game_option()

    def _option_collide(self):
        x, y = pygame.mouse.get_pos()
        if (275 < x < 525)and(250 < y < 310):
            self._collide_new_game = True
        else:
            self._collide_new_game = False

        if (275 < x < 525)and(325 < y < 385):
            self._collide_quick_game = True
        else:
            self._collide_quick_game = False

        if (275 < x < 525)and(400 < y < 460):
            self._collide_create_map = True
        else:
            self._collide_create_map = False

        if (275 < x < 525)and(475 < y < 535):
            self._collide_exit_game = True
        else:
            self._collide_exit_game = False

    def _new_game_option(self):
        self._exit_menu = True
        self._start_game = True


    def _quick_game_option(self):
        pass

    def _create_map_option(self):
        pass

    def _exit_game_option(self):
        self._exit_menu = True
        self._start_game = False

    def get_start_game(self):
        return self._start_game

    def start(self):
        pygame.init()
        self._display = pygame.display.set_mode((config.Config.MENU_WIDTH, config.Config.MENU_HEIGHT))
        pygame.display.set_caption("Main Menu")

        while not self._exit_menu:
            for event in pygame.event.get():
                self._option_select()
                self._option_collide()
                if event.type == pygame.QUIT:
                    self._exit_menu = True
                    self._start_game = False
            self._update_screen()
            pygame.display.update()
        if self._exit_menu:
            pygame.quit()
