# background()

Sets the color or image used for the background of the canvas.

By default, the background is transparent. `background()` is typically used within draw() to clear the display window at the beginning of each frame. It can also be used inside setup() to set the background on the first frame of animation.

The version of `background()` with one parameter interprets the value one of four ways. If the parameter is a `Number`, it's interpreted as a grayscale
value. If the parameter is a `String`, it's interpreted as a CSS color string. RGB, RGBA, HSL, HSLA, hex, and named color strings are supported. If the
parameter is a color object, it will be used as the background color. If the parameter is a image object, it will be used as the background image.

The version of `background()` with two parameters interprets the first one as a grayscale value. The second parameter sets the alpha (transparency) value.

The version of `background()` with three parameters interprets them as RGB, HSB, or HSL colors, depending on the current colorMode(). By default, colors are specified in RGB values. Calling `background(255, 204, 0)` sets the background a bright yellow color.

## Examples

![background example 1](assets/background1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  -- A grayscale value.
  background(51)

  describe('A canvas with a dark charcoal gray background.')
end
```

![background example 2](assets/background2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  -- R, G, B values
  background(255, 204, 0, 128)
  describe('A canvas with a yellow background.')
end
```

![background example 3](assets/background3.webp)

```lua
require("L5")

function setup()
  size(100,100)
  -- 3 digit hex notation
  background('#fae')
  describe('A canvas with a pink background.')
end
```

![background example 4](assets/background4.webp)

```lua
require("L5")

function setup()
  size(100,100)
  -- 6-digit hex notation
  background('#222222')
  describe('A canvas with black background.')
end
```

![background example 5](assets/background5.webp)

```lua
require("L5")

function setup()
  size(100,100)

  --a color object
  local c = color(0, 0, 255)
  background(c)

  describe('A canvas with blue background.')
end
```

## Syntax

```lua
background(color)
```

```lua
background(colorstring, [a])
```

```lua
background(gray, [a])
```

```lua
background(v1, v2, v3, [a])
```

```lua
background(values)
```

```lua
background(image)
```

## Parameters

| Parameter   |                                                                                          |
| -           | --                                                                                       |
| color       | color: any value created by the color() function                                         |
| colorstring | string: color string, possible formats include html color name, 3-digit hex, 6-digit hex |
| a           | number: opacity of background relative to current color range (default 0 - 255)          |
| gray        | number: specifies a value between white and black                                        |
| v1          | number: red value if color mode is RGB, or hue value if color mode is HSB                |
| v2          | number: green value if color mode is RGB, or saturation value if color mode is HSB       |
| v3          | number: blue value if color mode is RGB, or brightness value if color mode is HSB        |
| values      | table: a table array containing the red, green, blue and alpha components of the color   |
| image       | image: image created with loadImage() to set as background                               |

## Related

* [clear()](clear.md)
* [color()](color-object.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
