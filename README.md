# EZ-Game
## Description
We made Pygame easy-to-use! Comes with window creation, sprite creation, sprite rendering, collision detections, and more! We made this library so we could shorten your 200 lines of code, to just 80 lines!

## Documentation
### Installation
It's very easy to setup. You just need to enter the following into your Command Line:
```sh
cd /dir/to/project/
git clone https://github.com/uberBuilder24/EZ-Game
pip install -r requirements.txt
```
After you download the source code and all dependencies, you you need to import the library. To do so, add:
```py
import pygame
from EZGame import Game, colors

game = Game()
```

### Functions
#### Main Game Functions
`game.handle_fps()` - Get better framerates by setting an FPS limit.

`game.set_background(color)` - Set a background color for your window.

`game.is_colliding(obj1, obj2)` - Returns a True/False statement telling you if 2 objects are colliding.

`game.is_hovering(obj)` - Returns a True/False statement telling you if the mouse is hovering something.

`game.key_pressed(pressed_keys, key)` - Returns a True/False statement telling you if a certain key was pressed.

`game.set_cursor(cursor)` - Sets your cursor to be different from the classic arrow.

#### Sprite Subfunctions
`game.sprites.new_sprite(name, pos, size)` - Creates an invisible Sprite object.

`game.sprites.draw_sprite(name, imgSrc, dir, background, opacity)` - Makes an invisible Sprite object visible in an image form. The 'background' boolean will choose if you want a transparent background, or to be able to fade the image. Sadly, they don't work together.

`game.sprites.draw_shape(name, shape, color)` - Makes an invisible Sprite object visible in an shape form.

`game.sprites.scale_sprite(name, size)` - Makes a Sprite's image object bigger/smaller.

`game.sprites.rotate_sprite(name, dir)` - Turns a Sprite's image object.

#### Text Subfunctions
`game.text.preview(text, font, fontSize, pos, color)` - Returns a Pygame text object.

`game.text.render(text, font, fontSize, pos, color)` - Renders a Pygame text object.

#### Colors
__**Defaults**__:

```py
colors.BLACK
colors.WHITE
colors.RED
colors.ORANGE
colors.YELLOW
colors.GREEN
colors.MINT
colors.CYAN
colors.BLUE
colors.PURPLE
colors.PINK
```

__**Custom**__:

`colors.hex_to_rgb(hex)` - Turns a HEX code (#ff0000) into a RGB code that works with EZ-Game.