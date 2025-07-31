# line()

Draws a straight line between two points.

A line's default width is one pixel. The version of `line()` with four parameters draws the line in 2D. To color a line, use the `stroke()` function. To change its width, use the `strokeWeight()` function. A line can't be filled, so the `fill()` function won't affect the line's color.

## Examples

![line example](assets/line.webp)

```lua
function setup() 
  size(100, 100)

  background(200)

  line(30, 20, 85, 75)

  describe('A black line on a gray canvas running from top-center to bottom-right.')
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

* [strokeWeight()](strokeweight.md)
* [strokeJoin()](strokejoin.md)
* [strokeCap()](strokecap.md)
* ~~beginShape()~~
