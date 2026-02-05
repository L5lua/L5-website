# line()

Draws a straight line between two points.

A line's default width is one pixel. The version of `line()` with four parameters draws the line in 2D. To color a line, use the `stroke()` function. To change its width, use the `strokeWeight()` function. A line can't be filled, so the `fill()` function won't affect the line's color.

## Examples

![line 1 example](assets/line1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  line(30, 20, 85, 75)

  describe('A black line on a gray canvas running from top-center to bottom-right.')
end
```

![line 2 example](assets/line2.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle("line example")
  background(200)
  stroke('magenta')
  strokeWeight(5)

  line(30, 20, 85, 75)

  describe('A thick, magenta line on a gray canvas running from top-center to bottom-right.')
end
```

![line 3 example](assets/line3.webp)  

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle("line example")
  background(200)

  -- Top
  line(30, 20, 85, 20)

  -- Right
  stroke(126)
  line(85, 20, 85, 75)

  -- Bottom
  stroke(255)
  line(85, 75, 30, 75)

  describe('Three lines drawn in grayscale on a gray window. They form the top, right, and bottom sides of a square.')
end
```

## Syntax

```lua
line(x1, y1, x2, y2)
```

## Parameters

| Parameter |                                                    |
| -         | -------------------------------------------------- |
| x1        | Number: x-coordinate of the first point.           |
| y1        | Number: y-coordinate of the first point.           |
| x2        | Number: x-coordinate of the second point.          |
| y2        | Number: y-coordinate of the second point.          |

## Related

* [strokeWeight()](strokeWeight.md)
* [strokeJoin()](strokeJoin.md)
* [beginShape()](beginShape.md)

---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
