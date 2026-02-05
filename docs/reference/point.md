# point()

Draws a single point in space.

A point's default width is one pixel. To color a point, use the stroke() function. To change its width, use the strokeWeight() function. A point can't be filled, so the fill() function won't affect the point's color.

Set the point location with its x- and y-coordinates, as in point(10, 20).

## Example

![point 1 example](assets/point1.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle("point example")
  background(200)

  -- Top-left.
  point(30, 20)

  -- Top-right.
  point(85, 20)

  -- Bottom-right.
  point(85, 75)

  -- Bottom-left.
  point(30, 75)

  describe(
    'Four small, black points drawn on a gray canvas. The points form the corners of a square.'
  )
end
```

![point 2 example](assets/point2.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle("point example")
  background(200)

  -- Top-left.
  point(30, 20)

  -- Top-right.
  point(70, 20)

  -- Style the next points.
  stroke('purple')
  strokeWeight(10)

  -- Bottom-right.
  point(70, 80)

  -- Bottom-left.
  point(30, 80)

  describe('Four points drawn on a gray canvas. Two are black and two are purple. The points form the corners of a square.')
end
```

## Syntax

```lua
point(x, y)
```

## Parameters

| Parameter |                                                    |
| -         | -------------------------------------------------- |
| x        | Number: x-coordinate of the point.           |
| y        | Number: y-coordinate of the point.           |

## Related

* [stroke()](stroke.md)
* [strokeWeigh()](strokeWeight.md)
* [line()](line.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
