# Imports

import pygame
import os

systemVars = ["WIDTH", "HEIGHT", "WIN", "TITLE", "ICON", "FPS"]

# Subclasses

class Sprites:
    def __init__(self, WIN):
        self.WIN = WIN
    
    def new_sprite(self, name, pos, size):
        if not name in systemVars:
            exec(f"self.{name} = pygame.Rect({pos[0]}, {pos[1]}, {size[0]}, {size[1]})")
        else:
            raise SystemVariable(f"You cannot name a character any of these names: {', '.join(systemVars)}.")

    def draw_sprite(self, name, imgSrc, dir=0, opacity=255):
        pos = (eval(f"self.{name}.x"), eval(f"self.{name}.y"))
        size = (eval(f"self.{name}.width"), eval(f"self.{name}.height"))

        exec(f"self.{name}_img = pygame.image.load({imgSrc}).convert()")
        exec(f"self.{name}_new_img = pygame.transform.rotate(pygame.transform.scale(self.{name}_img, {size}), {dir})")
        exec(f"self.{name}_new_img.set_alpha({opacity})")

        img = eval(f"self.{name}_new_img")

        self.WIN.blit(img, pos)

    def draw_shape(self, name, shape, color=(0, 0, 0)):
        shape = shape.lower().title()

        pos = (eval(f"self.{name}.x"), eval(f"self.{name}.y"))
        size = (eval(f"self.{name}.width"), eval(f"self.{name}.height"))

        exec(f"pygame.draw.rect(self.WIN, {color}, pygame.Rect({pos[0]}, {pos[1]}, {size[0]}, {size[1]}))")
    
    def scale_sprite(self, name, size):
        exec(f"self.{name}_new_img = pygame.transform.scale(self.{name}_new_img, {size})")

    def rotate_sprite(self, name, dir):
        exec(f"self.{name}_new_img = pygame.transform.rotate(self.{name}_new_img, {dir})")

class Text:
    def __init__(self, WIN):
        self.WIN = WIN

    def preview(self, text, font="comicsans", fontSize=40, pos=(10, 10), color=(255, 255, 255)):
        FONT = pygame.font.SysFont(font, fontSize)
        PREVIEW = FONT.render(text, 1, color)
        return PREVIEW

    def render(self, text, font="comicsans", fontSize=40, pos=(10, 10), color=(255, 255, 255)):
        FONT = pygame.font.SysFont(font, fontSize)
        RENDERED = FONT.render(text, 1, color)
        self.WIN.blit(RENDERED, pos)
    
class __Colors:
    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (222, 33, 20)
        self.ORANGE = (255, 170, 0)
        self.YELLOW = (255, 255, 0)
        self.GREEN = (12, 235, 34)
        self.MINT = (97, 255, 202)
        self.CYAN = (34, 227, 224)
        self.BLUE = (45, 141, 237)
        self.PURPLE = (150, 40, 235)
        self.PINK = (255, 179, 250)

colors = __Colors()

# Main Class

class Game:
    def __init__(self, WIDTH: int = 900, HEIGHT: int = 500, TITLE: str = "EZ-Game Window", ICON = None, FPS: int = 60):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        self.TITLE = TITLE
        if ICON != None:
            self.ICON = pygame.image.load(ICON)
            pygame.display.set_icon(self.ICON)
        self.FPS = FPS

        self.sprites = Sprites(self.WIN)
        self.text = Text(self.WIN)
        
        pygame.display.set_caption(TITLE)
        pygame.font.init()
        pygame.mixer.init()
    
    def handle_fps(self):
        clock = pygame.time.Clock()
        clock.tick(self.FPS)

    def set_background(self, color):
        self.WIN.fill(color)
    
    def is_colliding(self, obj1, obj2):
        return obj1.colliderect(obj2)
    
    def is_hovering(self, obj):
        self.new_sprite("mouseHover", (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), (10, 10))
        return self.is_colliding(self.mouseHover, obj)
    
    def key_pressed(self, pressed_keys, key):
        return pressed_keys[key]

    def set_cursor(self, cursor: str):
        exec(f"pygame.mouse.set_cursor(*pygame.cursors.{cursor})")

# Errors

class SystemVariable(Exception):
    pass