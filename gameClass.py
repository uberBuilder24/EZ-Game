# Imports

import pygame
import os

systemVars = ["WIN", "WIDTH", "HEIGHT", "FPS", "TITLE"]

# Window Creation

class Window:
    def __init__(self, WIDTH=900, HEIGHT=500, FPS=60, TITLE="EZ-Game Window"):
        self.FPS = 60
        self.WIDTH = 900
        self.HEIGHT = 500
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        self.TITLE = TITLE
        pygame.font.init()
        pygame.mixer.init()
        pygame.display.set_caption(TITLE)
    
    def new_sprite(self, name, pos, size, imgSrc, dir=0):
        if not name in systemVars:
            exec(f"self.{name} = pygame.Rect({pos[0]}, {pos[1]}, {size[0]}, {size[1]})")
            exec(f"self.{name}_img = pygame.image.load(imgSrc)")
            exec(f"self.{name}_new_img = pygame.transform.rotate(pygame.transform.scale(self.{name}_img, size), dir)")
        else:
            raise SystemVariable(f"You cannot name a character any of these names: {', '.join(systemVars)}.")

    def draw_sprite(self, name):
        img = eval(f"self.{name}_new_img")
        pos = (eval(f"self.{name}.x"), eval(f"self.{name}.y"))
        self.WIN.blit(img, pos)

    def draw_shape(self, name, shape, pos, size, color=(0, 0, 0)):
        shape = shape.lower().title()
        if not name in systemVars:
            exec(f"pygame.draw.rect(self.WIN, {color}, pygame.Rect({pos[0]}, {pos[1]}, {size[0]}, {size[1]}))")
        else:
            raise SystemVariable(f"You cannot name a character any of these names: {', '.join(systemVars)}.")
    
    def scale_sprite(self, name, size):
        exec(f"self.{name}_new_img = pygame.transform.scale(self.{name}_new_img, {size})")

    def rotate_sprite(self, name, direction):
        exec(f"self.{name}_new_img = pygame.transform.rotate(self.{name}_new_img, {direction})")
    
    def preview_text(self, text, font="comicsans", fontSize=40, pos=(10, 10), color=(255, 255, 255)):
        FONT = pygame.font.SysFont(font, fontSize)
        PREVIEW = FONT.render(text, 1, color)
        return PREVIEW

    def draw_text(self, text, font="comicsans", fontSize=40, pos=(10, 10), color=(255, 255, 255)):
        FONT = pygame.font.SysFont(font, fontSize)
        RENDERED = FONT.render(text, 1, color)
        self.WIN.blit(RENDERED, pos)
    
    def colliding(self, obj1, obj2):
        return obj1.colliderect(obj2)

# Colour Codes

class Colors:
    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.ORANGE = (255, 128, 0)
        self.YELLOW = (255, 255, 0)
        self.GREEN = (0, 255, 0)
        self.MINT = (0, 255, 128)
        self.CYAN = (0, 255, 255)
        self.BLUE = (0, 0, 255)
        self.PURPLE = (127, 0, 255)
        self.PINK = (255, 0, 255)

class SystemVariable(Exception):
    pass