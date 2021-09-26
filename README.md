# EZ-Game
## Description
I made Pygame easy-to-use! Comes with window creation, sprite creation, sprite rendering, collision detections, and more! I made this library so I could shorten your 200 lines of code, to just 80 lines! (Credit: Pygame - the base library).

## Documentation
### Installation
It's very easy to setup. You just need to enter the following into your Command Line:

```sh
cd /dir/to/project/
git clone https://github.com/uberBuilder24/EZ-Game
pip install -r requirements.txt
```

After you download the source code, you need to import the library. To do so, add `import pygame` and `import EZGame` to the top of your Python file. Make sure the `EZGame.py` file and the file you wish to use the library in are in the same directory. To initialize the library, add `game = EZGame.Game()` to your code.

### Main Functions
```py
game.handle_fps() # Enables the FPS Limit
game.set_background(media, image) # Sets the Background
game.is_colliding(obj1, obj2) # Returns a Boolean Telling You If 2 Objects are Colliding
game.is_hovering(obj) # Returns a Boolean Telling You If Your Mouse is Hovering Something
game.key_pressed(pressed_keys, key) # Returns a Boolean Telling You If a Key Was Pressed
game.set_cursor(cursor) # Sets the Cursor
```

### Sprite Functions
```py
game.sprites.new_sprite(name, pos, size) # Creates an Invisible Sprite
game.sprites.draw_sprite(name, imgSrc, dir, background, opacity) # Makes a Sprite Visible (Image Form)
game.sprites.draw_shape(name, shape, color) # Makes a Sprite Visible (Shape Form)
game.sprites.move_sprite(name, pos, axis, set) # Moves a Sprite
game.sprites.scale_sprite(name, size) # Makes a Sprite Bigger/Smaller
game.sprites.rotate_sprite(name, dir) # Rotates a Sprite
```

If the `background` parameter for the `draw_sprite` function is set to `False`, the transparent background of the sprite will work properly. However, if it's set to `True`, you will be able to fade the sprite.

### Text Functions
```py
game.text.preview(text, font, fontSize, ttf, color) # Returns a Text Object
game.text.render(text, font, fontSize, ttf, pos, color) # Renders a Text Object
```

### Sound Functions
```py
game.sound.loadEffect(name, soundSrc) # Loads a Sound Effect
game.sound.playEffect(name) # Plays the Loaded Sound Effect
game.sound.effectVolume(name, set, volume) # Gets/Sets the Sound Effect Volume
game.sound.loadMusic(soundSrc) # Loads Background Music
game.sound.playMusic(startTime, loops) # Plays the Loaded Background Music
game.sound.musicVolume(set, volume) # Gets/Sets the Music Volume
game.sound.musicTime(set, pos) # Gets/Sets the Music Time
game.sound.pauseMusic() # Pauses/Resumes the Music
game.sound.stopMusic() # Stops the Music
```

### Event Variables
```py
game.events.MouseMotion # Returns the Pygame Event for Mouse Motion
game.events.MouseDown # Returns the Pygame Event for Mouse Motion
```

### Colors
#### Defaults
```py
colors.BLACK
colors.LIGHT_GRAY
colors.DARK_GRAY
colors.RED
colors.ORANGE
colors.YELLOW
colors.GREEN
colors.MINT
colors.CYAN
colors.SKY_BLUE
colors.BLUE
colors.PURPLE
colors.PINK
colors.WHITE
```

#### Custom
`colors.hex_to_rgb(hex)` - Turns a HEX code (#ff0000) into a RGB code that works with EZ-Game.
