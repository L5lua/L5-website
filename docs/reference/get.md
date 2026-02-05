# get()

Gets a pixel or a region of pixels from the canvas.

`get()` is easy to use but it's not as fast as `pixels`. Use `pixels` to read many pixel values.

The version of `get()` with no parameters returns the entire canvas.

The version of `get()` with two parameters interprets them as coordinates. It returns a table with the {R, G, B, A} values of the pixel at the given point.

The version of `get()` with four parameters interprets them as coordinates and dimensions. It returns a subsection of the canvas as an image. The first two parameters are the coordinates for the upper-left corner of the subsection. The last two parameters are the width and height of the subsection.

## Examples

![get example 1](assets/get1.webp)

```lua
local img
require("L5")

function setup()
  size(100,100)
  img = loadImage("assets/rockies.jpg")
  windowTitle("get() example")

  -- Display the image.
  image(img, 0, 0, width, height)

  -- Get the entire canvas
  c = get()

  -- Display half the canvas
  image(c, 50, 0)

  describe('Two identical mountain landscapes side-by-side')
end

```

![get example 2](assets/get2.webp)

```lua
local img
require("L5")

function setup()
  size(100,100)
  img = loadImage("assets/rockies.jpg")
  windowTitle("get() example")

  -- Display the image.
  image(img, 0, 0)

  -- Get the color of a pixel.
  c = get(50, 90)

  -- Style the square with the pixel's color.
  fill(c)
  noStroke()

  -- Display the square.
  square(25, 25, 50)

  describe('A mountain landscape with an olive green square in its center.')
end
```

![get example 3](assets/get3.webp)

```lua
local img
require("L5")

function setup()
  size(100,100)
  img = loadImage("assets/rockies.jpg")
  windowTitle("get() example")

  -- Display the image.
  image(img, 0, 0)


  -- Get a region of the image.
  local c = get(0, 0, 50, 50)

  
  -- Display the region.
  image(c, 50, 50)

  describe('A mountain landscape drawn on top of another mountain landscape.')
end
```

## Syntax

```lua
get(x, y)
```

```lua
get(x, y, w, h)
```

```lua
get()
```

## Parameters

| Parameter |                                                                     |
| -         | --                                                                  |
| x         | Number: x coordinate of the pixel                                   |
| y         | Number: y coordinate of the pixel                                   |
| w         | Number: width of the section to be returned                         |
| h         | Number: height of the section to be returned                        |

## Returns

RGBA color table, entire window as image, or subsection of window as image

## Related

* [blend()](blend.md)
* [copy()](copy.md)
* [set()](set.md)
* [pixels](pixels.md)
* [filter()](filter.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
