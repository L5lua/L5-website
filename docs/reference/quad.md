# quad()

A quad is a quadrilateral, a four sided polygon. It is similar to a rectangle, but the angles between its edges are not constrained to ninety degrees. The first pair of parameters (x1,y1) sets the first vertex and the subsequent pairs should proceed clockwise or counter-clockwise around the defined shape.

## Examples

![quad 1 example](assets/quad1.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle("line example")
  background(200)

  quad(20, 20, 80, 20, 80, 80, 20, 80)

  describe('A white square with a black outline drawn on a gray canvas.')
end
```

![quad 2 example](assets/quad2.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle("quad example")
  background(200)

  quad(20, 30, 80, 30, 80, 70, 20, 70)

  describe('A white rectangle with a black outline drawn on a gray canvas.')
end
```

![quad 3 example](assets/quad3.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle("quad example")
  background(200)

  quad(50, 62, 86, 50, 50, 38, 14, 50)

  describe('A white rhombus with a black outline drawn on a gray canvas.')
end
```

![quad 4 example](assets/quad4.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle("quad example")
  background(200)

  quad(20, 50, 80, 30, 80, 70, 20, 70)

  describe('A white trapezoid with a black outline drawn on a gray canvas.')
end
```

## Syntax

```lua
quad(x1, y1, x2, y2, x3, y3, x4, y4)
```

## Parameters

| Parameter |                                                    |
| -         | -------------------------------------------------- |
| x1        | Number: x-coordinate of the first corner.          |
| y1        | Number: y-coordinate of the first corner.          |
| x2        | Number: x-coordinate of the second corner.         |
| y2        | Number: y-coordinate of the second corner.         |
| x3        | Number: x-coordinate of the third corner.          |
| y3        | Number: y-coordinate of the third corner.          |
| x4        | Number: x-coordinate of the fourth corner.         |
| y4        | Number: y-coordinate of the fourth corner.         |

## Related

* [arc()](arc.md)
* [circle()](circle.md)
* [ellipse()](ellipse.md)
* [line()](line.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
