# colorMode()

Changes the way color values are interpreted.

By default, the `Number` parameters for fill(), stroke(), background(), and color() are defined by values between 0 and 255 using the RGB color model. This is equivalent to calling `colorMode(RGB, 255)`. Pure red is `color(255, 0, 0)` in this model.

Calling `colorMode(RGB, 100)` sets colors to use RGB color values between 0 and 100. Pure red is `color(100, 0, 0)` in this model.

Calling `colorMode(HSB)` or `colorMode(HSL)` changes to HSB or HSL system instead of RGB. Pure red is `color(0, 100, 100)` in HSB and `color(0, 100, 50)` in HSL.

## Examples

![colorMode example 1](assets/colorMode1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Fill with pure red.
  fill(255, 0, 0)

  circle(50, 50, 25)

  describe('A gray square with a red circle at its center.')
end
```

![colorMode example 2](assets/colorMode2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Use RGB color with values in the range 0-100.
  colorMode(RGB, 100)

  -- Fill with pure red.
  fill(100, 0, 0)

  circle(50, 50, 25)

  describe('A gray square with a red circle at its center.')
end
```

![colorMode example 3](assets/colorMode3.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Use HSB color.
  colorMode(HSB)

  -- Fill with pure red.
  fill(0, 100, 100)

  circle(50, 50, 25)

  describe('A gray square with a red circle at its center.')
end
```

![colorMode example 4](assets/colorMode4.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Use HSL color.
  colorMode(HSL)

  -- Fill with pure red.
  fill(0, 100, 50)

  circle(50, 50, 25)

  describe('A gray square with a red circle at its center.')
end
```

![colorMode example 5](assets/colorMode5.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  -- Use RGB color with values in the range 0-100.
  colorMode(RGB, 100)

  for x=0,100 do
    for y=0,100 do
      stroke(x, y, 0)
      point(x, y)
    end
  end

  describe(
    'A diagonal green to red gradient from bottom-left to top-right with shading transitioning to black at top-left corner.'
  )
end
```

![colorMode example 6](assets/colorMode6.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  -- Use HSB color with values in the range 0-100.
  colorMode(HSB, 100)

  for x=0,100 do
    for y = 0,100 do
      stroke(x, y, 100)
      point(x, y)
    end
  end

  describe('A rainbow gradient from left-to-right. Brightness transitions to white at the top.')
end
```

![colorMode example 7](assets/colorMode7.webp)  

```lua
require("L5")

function setup()
  size(100, 100)

  -- Create a color table
  local myColor = color(180, 175, 230)
  background(myColor)

  -- Use RGB color with values in the range 0-1.
  colorMode(RGB, 1)

  -- Get the red, green, and blue color components.
  local redValue = red(myColor)
  local greenValue = green(myColor)
  local blueValue = blue(myColor)

  -- Round the color components for display.
  redValue = round(redValue, 2)
  greenValue = round(greenValue, 2)
  blueValue = round(blueValue, 2)

  -- Display the color components.
  fill(0)
  text("Red: "..redValue, 10, 10, 80, 80)
  text("Green: "..greenValue, 10, 40, 80, 80)
  text("Blue: "..blueValue, 10, 70, 80, 80)

  describe('A purple canvas with the red, green, and blue decimal values of the color written on it.')
end
```

![colorMode example 8](assets/colorMode8.webp)  

```lua
require("L5")

function setup()
  size(100, 100)

  background(255)

  -- Use RGB color with alpha values in the range 0-1.
  colorMode(RGB,255,255,255,1)

  noFill()
  strokeWeight(4)
  stroke(255, 0, 10, 0.3)
  circle(40, 40, 50)
  circle(50, 60, 50)

  describe('Two overlapping translucent pink circle outlines.')
end
```

## Syntax

```lua
colorMode(mode, [max])
```

## Parameters

| Parameter | |
| - | -- |
| mode | Constant: either RGB, HSB or HSL, corresponding to
                         Red/Green/Blue and Hue/Saturation/Brightness
                         (or Lightness). |
| max | Number: range for all values. |

## Related

* [color()](color-object.md)
* [hue()](hue.md)
* [brightness()](brightness.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
