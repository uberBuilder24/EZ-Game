# Imports

import pygame
import os

pygame.init()
pygame.mixer.init()
pygame.font.init()

systemVars = ["WIDTH", "HEIGHT", "WIN", "TITLE", "ICON", "FPS"]
getColor = lambda hx: tuple(int(hx[i:i + 2], 16) for i in (0, 2, 4))

# Subclasses

class Sprites:
    def __init__(self, WIN):
        self.WIN = WIN
    
    def new_sprite(self, name, pos, size):
        if not name in systemVars:
            exec(f"self.{name} = pygame.Rect({pos[0]}, {pos[1]}, {size[0]}, {size[1]})")
            exec(f"self.{name}_rotation = 0")
        else:
            raise SystemVariable(f"You cannot name a character any of these names: {', '.join(systemVars)}.")

    def draw_sprite(self, name, imgSrc, dir=0, background=False, opacity=255):
        pos = (eval(f"self.{name}.x"), eval(f"self.{name}.y"))
        size = (eval(f"self.{name}.width"), eval(f"self.{name}.height"))
        dir += eval(f"self.{name}_rotation")

        if background == False:
            exec(f"self.{name}_img = pygame.image.load('{imgSrc}').convert_alpha()")
        else:
            exec(f"self.{name}_img = pygame.image.load('{imgSrc}').convert()")
        exec(f"self.{name}_new_img = pygame.transform.rotate(pygame.transform.scale(self.{name}_img, {size}), {dir})")
        exec(f"self.{name}_new_img.set_alpha({opacity})")

        img = eval(f"self.{name}_new_img")

        self.WIN.blit(img, pos)

    def draw_shape(self, name, shape, color=(0, 0, 0)):
        shape = shape.lower().title()

        pos = (eval(f"self.{name}.x"), eval(f"self.{name}.y"))
        size = (eval(f"self.{name}.width"), eval(f"self.{name}.height"))

        exec(f"pygame.draw.rect(self.WIN, {color}, pygame.Rect({pos[0]}, {pos[1]}, {size[0]}, {size[1]}))")
    
    def move_sprite(self, name, pos, axis="x", set=True):
        if set == True:
            exec(f"self.{name}.{axis} = {pos}")
        else:
            exec(f"self.{name}.{axis} += {pos}")
    
    def scale_sprite(self, name, size):
        exec(f"self.{name}.width = {size[0]}")
        exec(f"self.{name}.height = {size[1]}")

    def rotate_sprite(self, name, dir):
        exec(f"self.{name}_rotation = {dir}")

class Text:
    def __init__(self, WIN):
        self.WIN = WIN

    def preview(self, text, font="comicsans", fontSize=40, ttf=False, color=(255, 255, 255)):
        if ttf == False:
            FONT = pygame.font.SysFont(font, fontSize)
        else:
            FONT = pygame.font.Font(font, fontSize)
        PREVIEW = FONT.render(text, 1, color)
        return PREVIEW

    def render(self, text, font="comicsans", fontSize=40, ttf=False, pos=(10, 10), color=(255, 255, 255)):
        if ttf == False:
            FONT = pygame.font.SysFont(font, fontSize)
        else:
            FONT = pygame.font.Font(font, fontSize)
        RENDERED = FONT.render(text, 1, color)
        self.WIN.blit(RENDERED, pos)

class Sound:
    def __init__(self):
        self.PAUSED = False
    
    def loadEffect(self, name, soundSrc):
        exec(f"self.{name} = pygame.mixer.Sound('{soundSrc}')")
    
    def playEffect(self, name):
        exec(f"self.{name}.play()")
    
    def effectVolume(self, name, set=True, volume=1):
        if set == True:
            exec(f"self.{name}.set_volume({volume})")
        else:
            return eval(f"self.{name}.get_volume()")
    
    def loadMusic(self, soundSrc):
        pygame.mixer.music.load(soundSrc)
    
    def playMusic(self, startTime=0.0, loops=-1):
        pygame.mixer.music.play(loops, startTime)
    
    def musicVolume(self, set=True, volume=1):
        if set == True:
            pygame.mixer.music.set_volume(volume)
        else:
            return pygame.mixer.music.get_volume()
        
    def musicTime(self, set=True, pos=0.0):
        if set == True:
            pygame.mixer.music.set_pos(pos)
        else:
            return pygame.mixer.music.get_pos()
    
    def pauseMusic(self):
        if self.PAUSED == False:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
    
    def stopMusic(self):
        pygame.mixer.music.stop()

class Events:
    def __init__(self):
        self.MouseMotion = 4
        self.MouseDown = 5

# Main Class

class Game:
    def __init__(self, WIDTH = 900, HEIGHT = 500, TITLE = "EZ-Game Window", ICON = None, FPS = 60):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        self.TITLE = TITLE
        if ICON != None:
            self.ICON = pygame.image.load(f"{ICON}")
            pygame.display.set_icon(self.ICON)
        self.FPS = FPS

        self.sprites = Sprites(self.WIN)
        self.text = Text(self.WIN)
        self.sound = Sound()
        self.events = Events()

        pygame.display.set_caption(TITLE)
    
    def handle_fps(self):
        clock = pygame.time.Clock()
        clock.tick(self.FPS)

    def set_background(self, media, image=False):
        if image == False:
            self.WIN.fill(media)
        else:
            background = pygame.image.load(media)
            self.WIN.blit(background, (0, 0))
    
    def is_colliding(self, obj1, obj2):
        if obj1.colliderect(obj2):
            return True
        else:
            return False
    
    def is_hovering(self, obj):
        self.sprites.new_sprite("mouseHover", (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), (10, 10))
        return self.is_colliding(self.sprites.mouseHover, obj)
    
    def key_pressed(self, pressed_keys, key):
        if pressed_keys[key]:
            return True
        else:
            return False

    def set_cursor(self, cursor):
        exec(f"pygame.mouse.set_cursor(*pygame.cursors.{cursor})")

# Colors

class __Colors:
    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.LIGHT_GRAY = (176, 176, 176)
        self.DARK_GRAY = (74, 74, 74)
        self.RED = (222, 33, 20)
        self.ORANGE = (255, 170, 0)
        self.YELLOW = (255, 255, 0)
        self.GREEN = (12, 235, 34)
        self.MINT = (97, 255, 202)
        self.CYAN = (34, 227, 224)
        self.SKY_BLUE = (135, 206, 235)
        self.BLUE = (0, 128, 255)
        self.PURPLE = (150, 40, 235)
        self.PINK = (255, 179, 250)
        self.WHITE = (255, 255, 255)
    
    def hex_to_rgb(self, hex):
        return getColor(hex.strip("#"))

colors = __Colors()

# Errors

class SystemVariable(Exception):
    pass