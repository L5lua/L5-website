# blue()

Gets the blue value of a color.

`blue()` extracts the blue value from a color object, an array of color components, or a CSS color string.

By default, `blue()` returns a color's blue value in the range 0 to 255. If the colorMode() is set to RGB, it returns the blue value in the given range.

## Examples

![blue example 1](assets/blue1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Create a color object using RGB values.
  local c = color(175, 100, 220)

  -- Draw the left rectangle.
  noStroke()
  fill(c)
  rect(15, 15, 35, 70)

  -- Set 'blueValue' to 220.
  local blueValue = blue(c)

  -- Draw the right rectangle.
  fill(0, 0, blueValue)
  rect(50, 15, 35, 70)

  describe('Two rectangles. The left one is light purple and the right one is royal blue.')
end
```

![blue example 2](assets/blue2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Create a color object using RGB values.
  local c = {175, 100, 220}

  -- Draw the left rectangle.
  noStroke()
  fill(c)
  rect(15, 15, 35, 70)

  -- Set 'blueValue' to 220.
  local blueValue = blue(c)

  -- Draw the right rectangle.
  fill(0, 0, blueValue)
  rect(50, 15, 35, 70)

  describe('Two rectangles. The left one is light purple and the right one is royal blue.')
end
```

![blue example 3](assets/blue3.webp)

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

  -- Set 'blueValue' to 86.
  local blueValue = blue(c)

  -- Draw the right rectangle.
  fill(0, 0, blueValue)
  rect(50, 15, 35, 70)

  describe('Two rectangles. The left one is light purple and the right one is royal blue.')
end
```

## Syntax

```lua
blue(color)
```

## Parameters


| Parameter |                                                                 |
| -         | --------------------------------------------------              |
| color     | Color/Number/String. |


## Related

* [color()](color-object.md)
* [red()](red.md)
* [green()](green.md)
* [colorMode()](colorMode.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
