# green()

Gets the green value of a color.

`green()` extracts the green value from a
color object, an array of color components, or
a CSS color string.

By default, `green()` returns a color's green value in the range 0 to 255. If the colorMode() is set to RGB, it returns the green value in the given range.

## Examples

![green example 1](assets/green1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Create a color object.
  local c = color(175, 100, 220)

  -- Draw the left rectangle.
  noStroke()
  fill(c)
  rect(15, 15, 35, 70)

  -- Set 'greenValue' to 100.
  local greenValue = green(c)

  -- Draw the right rectangle.
  fill(0, greenValue, 0)
  rect(50, 15, 35, 70)

  describe('Two rectangles. The left one is light purple and the right one is dark green.')
end
```

![green example 2](assets/green2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Create a color array.
  local c = {175, 100, 220}

  -- Draw the left rectangle.
  noStroke()
  fill(c)
  rect(15, 15, 35, 70)

  -- Set 'greenValue' to 100.
  local greenValue = green(c)

  -- Draw the right rectangle.
  fill(0, greenValue, 0)
  rect(50, 15, 35, 70)

  describe('Two rectangles. The left one is light purple and the right one is dark green.')
end
```

![green example 3](assets/green3.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Use RGB color with values in the range 0-100.
  colorMode(RGB, 100)

  -- Create a color object using RGB values.
  local c = color(69, 39, 86)

  -- Draw the left rectangle.
  noStroke()
  fill(c)
  rect(15, 15, 35, 70)

  -- Set 'greenValue' to 39.
  local greenValue = green(c)

  -- Draw the right rectangle.
  fill(0, greenValue, 0)
  rect(50, 15, 35, 70)

  describe('Two rectangles. The left one is light purple and the right one is dark green.')
endend
```

## Syntax

```lua
green(color)
```

## Parameters

| Parameter |                                                                 |
| -         | --------------------------------------------------              |
| color     | Color/Number/String. |

## Related

* [colorMode()](colorMode.md)
* [red()](red.md)
* [blue()](blue.md)
* [alpha()](alpha.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
