# DEGREES

A string constant that's used to set the [angleMode()](angleMode.md).

By default, functions such as [rotate()](rotate.md) and [sin()](sin.md) expect angles measured in units of radians. Calling `angleMode(DEGREES)` ensures that angles are measured in units of degrees.

*Note: `TWO_PI` radians equals 360˚.*

## Examples

![DEGREES example 1](assets/degrees-constant1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Draw a red arc from 0 to HALF_PI radians.
  fill(255, 0, 0)
  arc(50, 50, 80, 80, 0, HALF_PI)

  -- Use degrees.
  angleMode(DEGREES)

  -- Draw a blue arc from 90˚ to 180˚.
  fill(0, 0, 255)
  arc(50, 50, 80, 80, 90, 180)

  describe('The bottom half of a circle drawn on a gray background. The bottom-right quarter is red. The bottom-left quarter is blue.')
end
```

## Related

* [angleMode()](angleMode.md)
* [degrees()](degrees.md)
* [ellipseMode()](ellipseMode.md)
* [ellipse()](ellipse.md)
* [RADIANS](radians-constant.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
