# angleMode()
 
Changes the unit system used to measure angles.

Degrees and radians are both units for measuring angles. There are 360˚ in one full rotation. A full rotation is 2 × π (about 6.28) radians.

Functions such as rotate() and sin() expect angles measured radians by default. Calling `angleMode(DEGREES)` switches to degrees. Calling `angleMode(RADIANS)` switches back to radians.

Calling `angleMode()` with no arguments returns current angle mode, which is either `RADIANS` or `DEGREES`.

## Examples

![angleMode example 1](assets/angleMode1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Rotate 1/8 turn.
  rotate(QUARTER_PI)

  -- Draw a line.
  line(0, 0, 80, 0)

  describe('A diagonal line radiating from the top-left corner of a square.')
end
```

![angleMode example 2](assets/angleMode2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Use degrees.
  angleMode(DEGREES)

  -- Rotate 1/8 turn.
  rotate(45)

  -- Draw a line.
  line(0, 0, 80, 0)

  describe('A diagonal line radiating from the top-left corner of a square.')
end
```

![angleMode example 3](assets/angleMode3.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(50)

  -- Calculate the angle to rotate.
  local angle = TWO_PI / 7

  -- Move the origin to the center.
  translate(50, 50)

  -- Style the flower.
  noStroke()
  fill(255, 50)

  -- Draw the flower.
  for i = 0, 7 do
    ellipse(0, 0, 80, 20)
    rotate(angle)
  end

  describe('A translucent white flower on a dark background.')
end
```

![angleMode example 4](assets/angleMode4.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(50)

  -- Use degrees.
  angleMode(DEGREES)

  -- Calculate the angle to rotate.
  local angle = 360 / 7

  -- Move the origin to the center.
  translate(50, 50)

  -- Style the flower.
  noStroke()
  fill(255, 50)

  -- Draw the flower.
  for i = 0,7 do
    ellipse(0, 0, 80, 20)
    rotate(angle)
  end

  describe('A translucent white flower on a dark background.')
end
```

![angleMode example 5](assets/angleMode5.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  describe('A white ball on a string oscillates left and right.')
end

function draw()
  background(200)

  -- Calculate the coordinates.
  local x = 30 * cos(frameCount * 0.05) + 50
  local y = 50

  -- Draw the oscillator.
  line(50, y, x, y)
  circle(x, y, 20)
end
```

![angleMode example 6](assets/angleMode5.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  -- Use degrees.
  angleMode(DEGREES)

  describe('A white ball on a string oscillates left and right.')
end

function draw()
  background(200)

  -- Calculate the coordinates.
  local x = 30 * cos(frameCount * 2.86) + 50
  local y = 50

  -- Draw the oscillator.
  line(50, y, x, y)
  circle(x, y, 20)
end
```

![angleMode example 7](assets/angleMode7.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Draw the upper line.
  rotate(PI / 6)
  line(0, 0, 80, 0)

  -- Use degrees.
  angleMode(DEGREES)

  -- Draw the lower line.
  rotate(30)
  line(0, 0, 80, 0)

  describe('Two diagonal lines radiating from the top-left corner of a square. The lines are oriented 30 degrees from the edges of the square and 30 degrees apart from each other.')
end
```

## Syntax

```lua
angleMode(mode)
```

```lua
angleMode()
```

## Parameters

| Parameter | |
| - | -- |
| mode | Constant: either RADIANS or DEGREES. |

## Related

* [acos()](acos.md)
* [asin()](asin.md)
* [atan()](atan.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
