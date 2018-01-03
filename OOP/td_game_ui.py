class UI:
    def __init__(self, rect):
        self.rect = rect


class Button(UI):
    def text_objects(self, text, font):
        text_surface = font.render(text, True, (0,0,0,0))
        return text_surface, text_surface.get_rect()

    def draw(self, display):
        pygame.draw.rect(self._display, ac, self.rect)
        small_text = pygame.font.SysFont("comicsansms", 20)
        text_surf, text_rect = self.text_objects(msg, small_text)
        text_rect.center = ((x + (w / 2)), (y + (h / 2)))
        self._display.blit(text_surf, text_rect)

