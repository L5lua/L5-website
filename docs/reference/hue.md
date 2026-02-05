# hue()

Gets the hue value of a color.

`hue()` extracts the hue value from a color object, an array of color components, or a CSS color string.

Hue describes a color's position on the color wheel. By default, `hue()` returns a color's HSL hue in the range 0 to 360. If the colorMode() is set to HSB or HSL, it returns the hue value in the given mode.

## Examples

![hue example 1](assets/hue1.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  noStroke()
  colorMode(HSB, 255)
  local c = color(0, 126, 255)
  fill(c)
  rect(15, 15, 35, 70)
  value = hue(c)  -- Sets 'value' to "0
  fill(value)
  rect(50,15,35,70)
  describe("Two rectangles. The rectanle on the left is salmon pink and the one on the right is black.")
end
```

![hue example 2](assets/hue1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Use HSL color.
  colorMode(HSL)

  -- Create a color object.
  local c = color(0, 50, 100)

  -- Draw the left rectangle.
  noStroke()
  fill(c)
  rect(15, 20, 35, 60)

  -- Set 'hueValue' to 0.
  local hueValue = hue(c)

  -- Draw the right rectangle.
  fill(hueValue)
  rect(50, 20, 35, 60)
end
```

![hue example 3](assets/hue2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Use HSL color.
  colorMode(HSL)

  -- Create a color array.
  local c = {0, 50, 100}

  -- Draw the left rectangle.
  noStroke()
  fill(c)
  rect(15, 20, 35, 60)

  -- Set 'hueValue' to 0.
  local hueValue = hue(c)

  -- Draw the right rectangle.
  fill(hueValue)
  rect(50, 20, 35, 60)
end
```

![hue example 3](assets/hue3.webp)

```lua
require("L5")

function setup()
  size(400, 400)
  noStroke()
  colorMode(HSB, 255)
  local c = color(0, 126, 255)
  fill(c)
  rect(60, 80, 140, 240)
  value = hue(c)  -- Sets 'value' to "0
  fill(value)
  rect(200, 80, 140, 240)
end
```

## Syntax

```lua
hue(color)
```

## Parameters

| Parameter |                                                                 |
| -         | --------------------------------------------------              |
| color     | Color/Number/String. |


## Related

* [color()](color.md)
* [brightness()](brightness.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
