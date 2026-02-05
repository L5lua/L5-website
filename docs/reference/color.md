# color()

Creates a color object.

By default, the parameters are interpreted as RGB values. Calling `color(255, 204, 0)` will return a bright yellow color. The way these parameters are interpreted may be changed with the colorMode() function.

The version of `color()` with one parameter interprets the value one of two ways. If the parameter is a number, it's interpreted as a grayscale value. If the parameter is a string, it's interpreted as a CSS color string.

The version of `color()` with two parameters interprets the first one as a grayscale value. The second parameter sets the alpha (transparency) value.

The version of `color()` with three parameters interprets them as RGB, HSB, or HSL colors, depending on the current `colorMode()`.

The version of `color()` with four parameters interprets them as RGBA, HSBA, or HSLA colors, depending on the current `colorMode()`. The last parameter sets the alpha (transparency) value.

## Examples

![color example 1](assets/color1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Create a color object using RGB values.
  local c = color(255, 204, 0)

  -- Draw the square.
  fill(c)
  noStroke()
  square(30, 20, 55)

  describe('A yellow square on a gray canvas.')
end
```

![color example 2](assets/color2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Create a color object using RGB values.
  local c1 = color(255, 204, 0)

  -- Draw the left circle.
  fill(c1)
  noStroke()
  circle(25, 25, 80)

  -- Create a color object using a grayscale value.
  local c2 = color(65)

  -- Draw the right circle.
  fill(c2)
  circle(75, 75, 80)

  describe(
    'Two circles on a gray canvas. The circle in the top-left corner is yellow and the one at the bottom-right is gray.'
  )
end
```

![color example 3](assets/color3.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Create a color object using a named color.
  local c = color('magenta')

  -- Draw the square.
  fill(c)
  noStroke()
  square(20, 20, 60)

  describe('A magenta square on a gray canvas.')
end
```

![color example 4](assets/color4.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Create a color object using a hex color code.
  local c1 = color('#0f0')

  -- Draw the left rectangle.
  fill(c1)
  noStroke()
  rect(0, 10, 45, 80)

  -- Create a color object using a hex color code.
  local c2 = color('#00ff00')

  -- Draw the right rectangle.
  fill(c2)
  rect(55, 10, 45, 80)

  describe('Two bright green rectangles on a gray canvas.')
end
```

## Syntax

```lua
color(gray, [alpha])
```

## Parameters

| Parameter | |
| - | -- |
| gray | Number: number specifying value between white and black. |
| alpha | Number: alpha value relative to current color range
                                (default is 0-255). |

## Related

* [HSB()](HSB.md)
* [colorMode()](colorMode.md)
* [fill()](fill.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
