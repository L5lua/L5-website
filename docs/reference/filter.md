# filter()

Applies an image filter to the canvas.

The preset options are:

`INVERT` Inverts the colors in the image. No parameter is used.

`GRAY` Converts the image to grayscale. No parameter is used.

`THRESHOLD` Converts the image to black and white. Pixels with a grayscale value above a given threshold are converted to white. The rest are converted to black. The threshold must be between 0.0 (black) and 1.0 (white). If no value is specified, 0.5 is used.

`POSTERIZE` Limits the number of colors in the image. Each color channel is limited to the number of colors specified. Values between 2 and 255 are valid, but results are most noticeable with lower values. The default value is 4.

`BLUR` Blurs the image. The level of blurring is specified by a blur radius. Larger values increase the blur. The default value is 4. Exponential blurring is used though not currently at parity with p5.js. 

`ERODE` Reduces the light areas. No parameter is used.

`DILATE` Increases the light areas. No parameter is used.

**Current known bugs:** filter() is not at feature parity with p5.js's filters and may produce different results. `filter()` does not currently function within `setup()`

## Examples

![filter 1 example](assets/filter1.webp)

```lua
local img
require("L5")

function setup()
  size(100, 100)
  windowTitle("filter() example")
  img = loadImage('assets/bricks.jpg')
end
function draw()
  -- Display the image.
  image(img, 0, 0)

  -- Apply the INVERT filter.
  filter(INVERT)

  describe('A blue brick wall.')
end
```

![filter 2 example](assets/filter2.webp)

```lua
local img
require("L5")

function setup()
  size(100, 100)
  windowTitle("filter() example")
  img = loadImage('assets/bricks.jpg')
end
function draw()
  -- Display the image.
  image(img, 0, 0)

  -- Apply the GRAY filter.
  filter(GRAY)

  describe('A brick wall in grayscale.')
end
```

![filter 3 example](assets/filter3.webp)

```lua
local img
require("L5")

function setup()
  size(100, 100)
  windowTitle("filter() example")
  img = loadImage('assets/bricks.jpg')
end
function draw()
  -- Display the image.
  image(img, 0, 0)

  -- Apply the THRESHOLD filter.
  filter(THRESHOLD)

  describe('A brick wall in black and white.')
end
```

![filter 4 example](assets/filter4.webp)

```lua
local img
require("L5")

function setup()
  size(100, 100)
  windowTitle("filter() example")
  img = loadImage('assets/bricks.jpg')
end
function draw()
  -- Display the image.
  image(img, 0, 0)

  -- Apply the POSTERIZE filter.
  filter(POSTERIZE, 3)

  describe('A brick wall drawn with limited color palette.')
end
```

![filter 5 example](assets/filter5.webp)

```lua
local img
require("L5")

function setup()
  size(100, 100)
  windowTitle("filter() example")
  img = loadImage('assets/bricks.jpg')
end
function draw()
  -- Display the image.
  image(img, 0, 0)

  -- Apply the BLUR filter.
  filter(BLUR, 3)

  describe('A brick wall drawn blurred.')
end
```

![filter 6 example](assets/filter6.webp)

```lua
local img
require("L5")

function setup()
  size(100, 100)
  windowTitle("filter() example")
  img = loadImage('assets/bricks.jpg')
end
function draw()
  -- Display the image.
  image(img, 0, 0)

  -- Apply the DILATE filter.
  filter(DILATE)

  describe('A brick wall drawn with bright lines between bricks.')
end
```

![filter 7 example](assets/filter7.webp)

```lua
local img
require("L5")

function setup()
  size(100, 100)
  windowTitle("filter() example")
  img = loadImage('assets/bricks.jpg')
end
function draw()
  -- Display the image.
  image(img, 0, 0)

  -- Apply the ERODE filter.
  filter(ERODE)

  describe('A brick wall drawn with faint lines between bricks.')
end
```

## Syntax

```lua
filter(filterType, [filterParam])
```

## Parameters

| Parameter | |
| - | -- |
| filterType | Constant: either THRESHOLD, GRAY, INVERT, POSTERIZE, ERODE, DILATE or BLUR. |
| filterParam | Number: parameter unique to each filter. |

## Related

* [blend()](blend.md)
* [copy()](copy.md)
* [get()](get.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
