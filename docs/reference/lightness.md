# lightness()

Gets the lightness value of a color.

`lightness()` extracts the HSL lightness value from a color object, an array of color components, or a CSS color string.

By default, `lightness()` returns a color's HSL lightness in the range 0 to 100. If the colorMode() is set to HSL, it returns the lightness value in the given range.

## Examples

![lightness example 1](assets/lightness1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(50)

  -- Use HSL color.
  colorMode(HSL)

  -- Create a color object using HSL values.
  local c = color(0, 100, 75)

  -- Draw the left rectangle.
  noStroke()
  fill(c)
  rect(15, 15, 35, 70)

  -- Set 'lightValue' to 75.
  local lightValue = lightness(c)

  -- Draw the right rectangle.
  fill(lightValue)
  rect(50, 15, 35, 70)

  describe('Two rectangles. The left one is salmon pink and the right one is gray.')
end
```

![lightness example 2](assets/lightness2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(50)

  -- Use HSL color.
  colorMode(HSL)

  -- Create a color array.
  local c = {0, 100, 75}

  -- Draw the left rectangle.
  noStroke()
  fill(c)
  rect(15, 15, 35, 70)

  -- Set 'lightValue' to 75.
  local lightValue = lightness(c)

  -- Draw the right rectangle.
  fill(lightValue)
  rect(50, 15, 35, 70)

  describe('Two rectangles. The left one is salmon pink and the right one is gray.')
end
```

![lightness example 3](assets/lightness3.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(50)

  -- Use HSL color with values in the range 0-255.
  colorMode(HSL, 255)

  -- Create a color object using HSL values.
  local c = color(0, 255, 191.5)

  -- Draw the left rectangle.
  noStroke()
  fill(c)
  rect(15, 15, 35, 70)

  -- Set 'lightValue' to 191.5.
  local lightValue = lightness(c)

  -- Draw the right rectangle.
  fill(lightValue)
  rect(50, 15, 35, 70)

  describe('Two rectangles. The left one is salmon pink and the right one is gray.')
end
```

## Syntax

```lua
lightness(color)
```

## Parameters

| Parameter |                                                                 |
| -         | --------------------------------------------------              |
| color     | Color/Number/String. |


## Related

* [color()](color.md)
* [hue()](hue.md)
* [brightness()](brightness.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
