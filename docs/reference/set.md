# set()

Sets the color of a pixel or draws an image to the canvas.

`set()` is easy to use but it's not as fast as pixels if drawing many pixels individually. Use `pixels` table array to batch set many pixel values instead of once per pixel.

`set()` interprets the first two parameters as x- and y-coordinates. It interprets the last parameter as a grayscale value, a `{R, G, B, A}` pixel array, a color object, or a image object. If an image is passed, the first two parameters set the coordinates for the image's upper-left corner, regardless of the current imageMode().

updatePixels() must be called after using `set()` for changes to appear.

## Examples

![set example 1](assets/set1.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle("set example1")

  background(200)

  -- Set four pixels to black.
  set(30, 20, 0)
  set(85, 20, 0)
  set(85, 75, 0)
  set(30, 75, 0)

  -- Update the canvas.
  updatePixels()

  describe('Four black dots arranged in a square drawn on a gray background.')
end
```

![set example 2](assets/set2.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle("set example2")

  background(200)

  -- Create a color object.
  local black = color(0)

  -- Set four pixels to black.
  set(30, 20, black)
  set(85, 20, black)
  set(85, 75, black)
  set(30, 75, black)

  -- Update the canvas.
  updatePixels()

  describe('Four black dots arranged in a square drawn on a gray background.')
end
```

![set example 3](assets/set3.webp)

```lua
require("L5")

function setup()
  size(100, 100)
end

function draw()
  background(255)
  windowTitle("set gradient")

  -- Draw a horizontal color gradient.
  for x = 0, 100 do
    for y = 0, 100 do
      -- Calculate the grayscale value.
      local c = map(x, 0, 100, 0, 255)

      -- Set the pixel using the grayscale value.
      set(x, y, c)
    end
  end

  -- Update the canvas.
  updatePixels()

  describe('A horizontal color gradient from black to white.')
end
```

![set example 4](assets/set4.webp)

```lua
local img
require("L5")

function setup()
  size(100, 100)
  windowTitle("set example 4")
  img = loadImage('assets/rockies.jpg')
  
  -- use the image to set all pixels
  set(0, 0, img)

  -- Update the canvas.
  updatePixels()

  describe('An image of a mountain landscape.')
end
```

## Syntax

```lua
set(x, y, c)
```

## Parameters

| Parameter |                                                                     |
| -         | --                                                                  |
| x         | Number: x coordinate of the pixel                                   |
| y         | Number: y coordinate of the pixel                                   |
| c         | Number/Color                                   |

## Returns

RGBA color table, entire window as image, or subsection of window as image


## Related

* [get()](get.md)
* [pixels](pixels.md)
* [updatePixels()](updatePixels.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
