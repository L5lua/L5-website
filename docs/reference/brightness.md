

Gets the brightness value of a color.

`brightness()` extracts the HSB brightness value from a color object, an array of color components, or
a CSS color string.

By default, `brightness()` returns a color's HSB brightness in the range 0 to 100. If the colorMode() is set to HSB, it returns the brightness value in the given range.

## Examples

![brightness example 1](assets/brightness1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Use HSB color.
  colorMode(HSB)

  -- Create a color object.
  local c = color(0, 50, 100)

  -- Draw the left rectangle.
  noStroke()
  fill(c)
  rect(15, 15, 35, 70)

  -- Set 'brightValue' to 100.
  local brightValue = brightness(c)

  -- Draw the right rectangle.
  fill(brightValue)
  rect(50, 15, 35, 70)

  describe('Two rectangles. The left one is salmon pink and the right one is white.')
end
```

![brightness example 2](assets/brightness2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Use HSB color.
  colorMode(HSB)

  -- Create a color array.
  local c = [0, 50, 100]

  -- Draw the left rectangle.
  noStroke()
  fill(c)
  rect(15, 15, 35, 70)

  -- Set 'brightValue' to 100.
  local brightValue = brightness(c)

  -- Draw the right rectangle.
  fill(brightValue)
  rect(50, 15, 35, 70)

  describe('Two rectangles. The left one is salmon pink and the right one is white.')
end
```

![brightness example 3](assets/brightness3.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Use HSB color with values in the range 0-255.
  colorMode(HSB, 255)

  -- Create a color object.
  local c = color(0, 127, 255)

  -- Draw the left rectangle.
  noStroke()
  fill(c)
  rect(15, 15, 35, 70)

  -- Set 'brightValue' to 255.
  local brightValue = brightness(c)

  -- Draw the right rectangle.
  fill(brightValue)
  rect(50, 15, 35, 70)

  describe('Two rectangles. The left one is salmon pink and the right one is white.')
end
```

## Syntax

```lua
brightness(color)
```

## Parameters

| Parameter |                                                                 |
| -         | --------------------------------------------------              |
| color     | Color/Number/String. |


## Related

* [color()](color.md)
* [hue()](hue.md)
* [lightness()](lightness.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
