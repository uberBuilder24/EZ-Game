# EZ-Game
## Description
We made Pygame easy-to-use! Comes with window creation, sprite creation, sprite rendering, collision detections, and more! We made this library so we could shorten your 200 lines of code, to just 80 lines!

## Documentation
### Installation
It's very easy to setup. You just need to do the following:
```sh
cd /dir/to/project/
git clone https://github.com/uberBuilder24/EZ-Game
pip install -r requirements.txt
```
After you download the source code and all dependencies, you you need to import the library. To do so, add `import pygame` and `import gameClass` to the top of your Python file. Make sure the `gameClass.py` file and the file you wish to use the library in are in the same directory. To initialize the library, add the following code after your imports.
```py
game = gameClass.Window()
colors = gameClass.Colors() # This is just a class filled with RGB color codes.
```

### Functions
`game.new_sprite(name, position, size, image, direction)` - This will create an invisible Sprite. You will get an error if you name it after an important variable.

`game.draw_sprite(name)` - This will make an invisible Sprite visible.

`game.scale_sprite(name, size)` - This will change the size of a Sprite.

`game.rotate_sprite(name, direction)` - This will turn a Sprite.

`game.preview_text(text, font, fontSize, position, color)` - This will create an invisible text object.

`game.draw_text(text, font, fontSize, position, color)` - This will create a visible text object.

`game.colliding(obj1, obj2)` - This will check if a Sprite is colliding with another Sprite.