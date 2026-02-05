# curve()

Draws a curve using a Catmull-Rom spline.

Spline curves can form shapes and curves that slope gently. They’re like cables that are attached to a set of points. Splines are defined by two anchor points and two control points.

The first two parameters, `x1` and `y1`, set the first control point. This point isn’t drawn and can be thought of as the curve’s starting point.

The next four parameters, `x2`, `y2`, `x3`, and `y3`, set the two anchor points. The anchor points are the start and end points of the curve’s visible segment.

The seventh and eighth parameters, `x4` and `y4`, set the last control point. This point isn’t drawn and can be thought of as the curve’s ending point.

## Examples

![curve example 1](assets/curve1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Draw a black spline curve.
  noFill()
  strokeWeight(1)
  stroke(0)
  curve(5, 26, 73, 24, 73, 61, 15, 65)

  -- Draw red spline curves from the anchor points to the control points.
  stroke(255, 0, 0)
  curve(5, 26, 5, 26, 73, 24, 73, 61)
  curve(73, 24, 73, 61, 15, 65, 15, 65)

  -- Draw the anchor points in black.
  strokeWeight(5)
  stroke(0)
  point(73, 24)
  point(73, 61)

  -- Draw the control points in red.
  stroke(255, 0, 0)
  point(5, 26)
  point(15, 65)

  describe(
    'A gray square with a curve drawn in three segments. The curve is a sideways U shape with red segments on top and bottom, and a black segment on the right. The endpoints of all the segments are marked with dots.'
  )
end
```

## Syntax

```lua
curve(x1, y1, x2, y2, x3, y3, x4, y4)
```

## Parameters

| Parameter | |
| - | -- |
| x1 | Number: x-coordinate of the first control point. |
| y1 | Number: y-coordinate of the first control point. |
| x2 | Number: x-coordinate of the first anchor point. |
| y2 | Number: y-coordinate of the first anchor point. |
| x3 | Number: x-coordinate of the second anchor point. |
| y3 | Number: y-coordinate of the second anchor point. |
| x4 | Number: x-coordinate of the second control point. |
| y4 | Number: y-coordinate of the second control point. |

## Related

* [bezier()](bezier.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
