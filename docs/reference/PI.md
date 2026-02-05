# PI

A number constant that's approximately 3.1416.

PI is the mathematical constant π. It's useful for many tasks that involve rotation and oscillation. For example, calling `rotate(PI)` rotates the coordinate system `PI` radians, which is a half turn (180 degrees).

Note: `TWO_PI` radians equals 360 degrees, `PI` radians equals 180 degrees, `HALF_PI` radians equals 90 degrees, `QUARTER_PI` radians equals 45 degrees.

## Examples

![PI example 1](assets/PI1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Draw an arc from 0 to PI.
  arc(50, 50, 80, 80, 0, PI)

  describe('The bottom half of a circle drawn in white on a gray background.')
end
```

![PI example 2](assets/PI2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Translate the origin to the center.
  translate(50, 50)

  -- Draw a line.
  line(0, 0, 40, 0)

  -- Rotate a half turn.
  rotate(PI)

  -- Draw the same line, rotated.
  line(0, 0, 40, 0)

  describe('A horizontal black line on a gray background.')
end
```

![PI example 3](assets/PI3.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  describe(
    'A red circle and a blue circle oscillate from left to right on a gray background. The circles drift apart, then meet in the middle, over and over again.'
  )
end

function draw()
  background(200)

  -- Translate the origin to the center.
  translate(50, 50)

  -- Calculate the x-coordinates.
  local x1 = 40 * sin(frameCount * 0.05)
  local x2 = 40 * sin(frameCount * 0.05 + PI)

  -- Style the oscillators.
  noStroke()

  -- Draw the red oscillator.
  fill(255, 0, 0)
  circle(x1, 0, 20)

  -- Draw the blue oscillator.
  fill(0, 0, 255)
  circle(x2, 0, 20)
end
```

## Related

* [angleMode()](angleMode.md)
* [DEGREES](degrees-constant.md)
* [HALF_PI](HALF_PI.md)
* [TWO_PI](TWO_PI.md)
* [QUARTER_PI](QUARTER_PI.md)
* [RADIANS](radians-constant.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
