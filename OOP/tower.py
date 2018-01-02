
class Tower:
    def __init__(self, display):
        self._display = display
        self._start_pos = (0, 0)
        self._pos = self._start_pos
        self._image = pygame.image.load("img/tower.png")
        self._level = 1
        self._id = 0


    def logic(self):
            if self._spawn >= 3019 and self.is_active():
                self._spawn = 0 - self._speed
                self._level += 1
                self._pos = self._start_pos
                self._active = False
            else:
                self._spawn = self._spawn + int(1*self._speed)
                self._move(self._spawn)

    def update(self):
        self._print(self._display)
        self._draw_enemie_health()

    def _print(self, display):
        display.blit(self.get_image(), self.get_pos())

    def _move(self, init):
        x, y = self.get_pos()
        if self._move_list_x[init] < 0:
            self._image = pygame.image.load("img/snake_inv.png")
        else:
            self._image = pygame.image.load("img/snake.png")
        self.set_pos(x + int(self._move_list_x[init]*self._speed), y + int(self._move_list_y[init]*self._speed))
