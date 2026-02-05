# TWO_PI
  
A number constant that's approximately 6.2832.

TWO_PI is the mathematical constant 2*π. It's useful for many tasks that involve rotation and oscillation. For example, calling `rotate(TWO_PI)` rotates the coordinate system `TWO_PI` radians, which is a complete turn (360 degrees).

Note: `TWO_PI` radians equals 360 degrees, `PI` radians equals 180 degrees, `HALF_PI` radians equals 90 degrees, `QUARTER_PI` radians equals 45 degrees.

## Examples

![TWO_PI example 1](assets/TWO_PI1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Draw an arc from 0 to TWO_PI.
  arc(50, 50, 80, 80, 0, TWO_PI)

  describe('A white circle drawn on a gray background.')
end
```

![TWO_PI example 2](assets/TWO_PI2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Translate the origin to the center.
  translate(50, 50)

  -- Draw a line.
  line(0, 0, 40, 0)

  -- Rotate a full turn.
  rotate(TWO_PI)

  -- Style the second line.
  strokeWeight(5)

  -- Draw the same line, shorter and rotated.
  line(0, 0, 20, 0)

  describe(
    'Two horizontal black lines on a gray background. A thick line extends from the center toward the right. A thin line extends from the end of the thick line.'
  )
end
```

![TWO_PI example 3](assets/TWO_PI3.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  describe(
    'A red circle with a blue center oscillates from left to right on a gray background.'
  )
end

function draw()
  background(200)

  -- Translate the origin to the center.
  translate(50, 50)

  -- Calculate the x-coordinates.
  local x1 = 40 * sin(frameCount * 0.05)
  local x2 = 40 * sin(frameCount * 0.05 + TWO_PI)

  -- Style the oscillators.
  noStroke()

  -- Draw the red oscillator.
  fill(255, 0, 0)
  circle(x1, 0, 20)

  -- Draw the blue oscillator, smaller.
  fill(0, 0, 255)
  circle(x2, 0, 10)
end
```

## Related

* [angleMode()](angleMode.md)
* [DEGREES](degrees-constant.md)
* [PI](PI.md)
* [HALF_PI](HALF_PI.md)
* [QUARTER_PI](QUARTER_PI.md)
* [RADIANS](radians-constant.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
