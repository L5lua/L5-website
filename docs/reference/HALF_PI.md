# HALF_PI
 
A number constant that's approximately 1.5708.

HALF_PI is the mathematical constant π/2. It's useful for many tasks that involve rotation and oscillation. For example, calling `rotate(HALF_PI)` rotates the coordinate system `HALF_PI` radians, which is a quarter turn (90 degrees).

Note: `TWO_PI` radians equals 360 degrees, `PI` radians equals 180 degrees, `HALF_PI` radians equals 90 degrees.

## Examples

![HALF_PI example 1](assets/HALF_PI1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Draw an arc from 0 to HALF_PI.
  arc(50, 50, 80, 80, 0, HALF_PI)

  describe('The bottom-right quarter of a circle drawn in white on a gray background.')
end
```

![HALF_PI example 2](assets/HALF_PI2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Translate the origin to the center.
  translate(50, 50)

  -- Draw a line.
  line(0, 0, 40, 0)

  -- Rotate a quarter turn.
  rotate(HALF_PI)

  -- Draw the same line, rotated.
  line(0, 0, 40, 0)

  describe('Two black lines on a gray background. One line extends from the center to the right. The other line extends from the center to the bottom.')
end
```

![HALF_PI example 3](assets/HALF_PI3.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  describe(
    'A red circle and a blue circle oscillate from left to right on a gray background. The red circle appears to chase the blue circle.'
  )
end

function draw()
  background(200)

  -- Translate the origin to the center.
  translate(50, 50)

  -- Calculate the x-coordinates.
  local x1 = 40 * sin(frameCount * 0.05)
  local x2 = 40 * sin(frameCount * 0.05 + HALF_PI)

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
* [TWO_PI](TWO_PI.md)
* [PI](PI.md)
* [QUARTER_PI](QUARTER_PI.md)
* [RADIANS](radians-constant.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
