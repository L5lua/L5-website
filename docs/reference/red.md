# red()

Gets the red value of a color.

`red()` extracts the red value from a color object, an array of color components, or a CSS color string.

By default, `red()` returns a color's red value in the range 0 to 255. If the colorMode() is set to RGB, it returns the red value in the given range.

## Examples

![red example 1](assets/red1.webp)

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

  -- Set 'redValue' to 175.
  local redValue = red(c)

  -- Draw the right rectangle.
  fill(redValue, 0, 0)
  rect(50, 15, 35, 70)

  describe('Two rectangles. The left one is light purple and the right one is red.')
end
```

![red example 2](assets/red2.webp)

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

  -- Set 'redValue' to 175.
  local redValue = red(c)

  -- Draw the right rectangle.
  fill(redValue, 0, 0)
  rect(50, 15, 35, 70)

  describe('Two rectangles. The left one is light purple and the right one is red.')
end
```

![red example 3](assets/red3.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Use RGB color with values in the range 0-100.
  colorMode(RGB, 100)

  -- Create a color object.
  local c = color(69, 39, 86)

  -- Draw the left rectangle.
  noStroke()
  fill(c)
  rect(15, 15, 35, 70)

  -- Set 'redValue' to 69.
  local redValue = red(c)

  -- Draw the right rectangle.
  fill(redValue, 0, 0)
  rect(50, 15, 35, 70)

  describe('Two rectangles. The left one is light purple and the right one is red.')
end
```

## Syntax

```lua
red(color)
```

## Parameters

| Parameter |                                                                 |
| -         | --------------------------------------------------              |
| color     | Color/Number/String. |

## Related

* [colorMode()](colorMode.md)
* [green()](green.md)
* [blue()](blue.md)
* [alpha()](alpha.md)



---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
