# tint()

Tints images using a color.

The version of `tint()` with one parameter interprets it one of four ways. If the parameter is a number, it's interpreted as a grayscale value. If the parameter is a string, it's interpreted as a CSS color string. A table array (similar to what is described as a *color object* in p5.js) of `{R, G, B, A}` values can also be used to set the tint color.

The version of `tint()` with two parameters uses the first one as a grayscale value and the second as an alpha value. For example, calling `tint(255, 128)` will make an image 50% transparent.

The version of `tint()` with three parameters interprets them as RGB or HSB values, depending on the current colorMode(). The optional fourth parameter sets the alpha value. For example, `tint(255, 0, 0, 100)` will give images a red tint and make them transparent.

## Examples

![tint 1 example](assets/tint1.webp)

```lua
local img

require("L5")

function setup()
  size(100, 100)
  windowTitle('tint() example')
  -- Load the image.
  img = loadImage('assets/flower.jpg')

  -- Left image.
  image(img, 0, 0, width/2, height)

  -- Right image.
  -- Tint with CSS string.
  tint('red')
  image(img, 50, 0, width/2, height)

  describe('Two images of an umbrella and a ceiling side-by-side. The image on the right has a red tint.')
end

```

![tint 2 example](assets/tint2.webp)

```lua
local img
require("L5")

function setup()
  size(100, 100)
  windowTitle('tint example')
-- Load the image.
  img = loadImage('assets/flower.jpg')

  -- Left image.
  image(img, 0, 0, 50, 100)

  -- Right image.
  -- Tint with RGB values.
  tint(255, 0, 0)
  image(img, 50, 0, 50, 100)

  describe('Two images of a pink flower side-by-side. The image on the right has a red tint.')
end
```

![tint 3 example](assets/tint3.webp)

```lua
local img
require("L5")

function setup()
  size(100, 100)
  windowTitle('tint example')
-- Load the image.
  img = loadImage('assets/flower.jpg')

  -- Left image.
  image(img, 0, 0, 50, 100)

  -- Right image.
  -- Tint with RGBA values.
  tint(255, 0, 0, 100)
  image(img, 50, 0, 50, 100)

  describe('Two images of a pink flower side-by-side. The image on the right has a transparent red tint.')
end
```

![tint 4 example](assets/tint4.webp)

```lua
local img
require("L5")

function setup()
  size(100, 100)
  windowTitle('tint example')
-- Load the image.
  img = loadImage('assets/flower.jpg')

  -- Left image.
  image(img, 0, 0, 50, 100)

  -- Right image.
  -- Tint with grayscale and alpha values.
  tint(255, 180)
  image(img, 50, 0, 50, 100)

  describe('Two images of a pink flower side-by-side. The image on the right is transparent.')
end
```

## Syntax

```lua
tint(v1, v2, v3, [alpha])
```

```lua
tint(value)
```

```lua
tint(gray, [alpha])
```

```lua
tint(values)
```

```lua
tint(color)
```

## Parameters

| Parameter |                                                                  |
| -         | --                                                               |
| v1        | Number: red or hue value.                                        |
| v2        | Number: green or saturation value.                               |
| v3        | Number: blue or brightness.                                      |
| alpha     | Number:                                                          |
| value     | String: CSS color string.                                        |
| gray      | Number: grayscale value.                                         |
| values    | Table: table array containing red, green, blue and alpha.        |
| color     | color object: the tint color.                                    |

## Related

* [noTint()](noTint.md)
* [color()](color-object.md)
* [image()](image.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
