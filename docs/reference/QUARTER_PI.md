# QUARTER_PI

A number constant that's approximately 0.7854.

QUARTER_PI is one-fourth the value of the mathematical constant π. It's useful for many tasks that involve rotation and oscillation. For example, calling `rotate(QUARTER_PI)` rotates the coordinate system `QUARTER_PI` radians, which is an eighth turn (45˚).

Note: `TWO_PI` radians equals 360 degrees, `PI` radians equals 180 degrees, `HALF_PI` radians equals 90 degrees, and `QUARTER_PI` radians equals 45 degrees.

## Examples

![QUARTER_PI example 1](assets/QUARTER_PI1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Draw an arc from 0 to QUARTER_PI.
  arc(50, 50, 80, 80, 0, QUARTER_PI)

  describe('A one-eighth slice of a circle drawn in white on a gray background.')
end
```

![QUARTER_PI example 2](assets/QUARTER_PI2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Translate the origin to the center.
  translate(50, 50)

  -- Draw a line.
  line(0, 0, 40, 0)

  -- Rotate an eighth turn.
  rotate(QUARTER_PI)

  -- Draw the same line, rotated.
  line(0, 0, 40, 0)

  describe('Two black lines that form a "V" opening towards the bottom-right corner of a gray square.')
end
```

![QUARTER_PI example 3](assets/QUARTER_PI3.gif)

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
  local x2 = 40 * sin(frameCount * 0.05 + QUARTER_PI)

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
* [PI](PI.md)
* [TWO_PI](TWO_PI.md)
* [RADIANS](radians-constant.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
