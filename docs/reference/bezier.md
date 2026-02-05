# bezier()

Draws a Bézier curve.

Bézier curves can form shapes and curves that slope gently. They're defined by two anchor points and two control points. Bézier curves provide more control than the spline curves created with the curve() function.

The first two parameters, x1 and y1, set the first anchor point. The first anchor point is where the curve starts.

The next four parameters, x2, y2, x3, and y3, set the two control points. The control points "pull" the curve towards them.

The seventh and eighth parameters, x4 and y4, set the last anchor point. The last anchor point is where the curve ends.

## Examples

![bezier 1 example](assets/bezier1.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle('bezier example')
  background(200)

  -- Draw the anchor points in black.
  stroke(0)
  strokeWeight(5)
  point(85, 20)
  point(15, 80)

  -- Draw the control points in red.
  stroke(255, 0, 0)
  point(10, 10)
  point(90, 90)

  -- Draw a black bezier curve.
  noFill()
  stroke(0)
  strokeWeight(1)
  bezier(85, 20, 10, 10, 90, 90, 15, 80)

  -- Draw red lines from the anchor points to the control points.
  stroke(255, 0, 0)
  line(85, 20, 10, 10)
  line(15, 80, 90, 90)

  describe(
    'A gray square with three curves. A black s-curve has two straight, red lines that extend from its ends. The endpoints of all the curves are marked with dots.'
  )
end
```

![bezier 2 example](assets/bezier2.webp)

```lua
-- Click the mouse near the red dot in the top-left corner
-- and drag to change the curve's shape.

local x2 = 10
local y2 = 10
local isChanging = false

require("L5")

function setup()
  size(100, 100)
  windowTitle('bezier example')
  describe(
    'A gray square with three curves. A black s-curve has two straight, red lines that extend from its ends. The endpoints of all the curves are marked with dots.'
  )
end

function draw() 
  background(200)

  -- Draw the anchor points in black.
  stroke(0)
  strokeWeight(5)
  point(85, 20)
  point(15, 80)

  -- Draw the control points in red.
  stroke(255, 0, 0)
  point(x2, y2)
  point(90, 90)

  -- Draw a black bezier curve.
  noFill()
  stroke(0)
  strokeWeight(1)
  bezier(85, 20, x2, y2, 90, 90, 15, 80)

  -- Draw red lines from the anchor points to the control points.
  stroke(255, 0, 0)
  line(85, 20, x2, y2)
  line(15, 80, 90, 90)
end

-- Start changing the first control point if the user clicks near it.
function mousePressed() 
  if dist(mouseX, mouseY, x2, y2) < 20  then
    isChanging = true
  end
end

-- Stop changing the first control point when the user releases the mouse.
function mouseReleased() 
  isChanging = false;
end

-- Update the first control point while the user drags the mouse.
function mouseDragged() 
  if isChanging == true then
    x2 = mouseX
    y2 = mouseY
  end
end
```

![bezier 3 example](assets/bezier3.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle('bezier example')
  background('skyblue')

  -- Draw the red balloon.
  fill('red')
  bezier(50, 60, 5, 15, 95, 15, 50, 60)

  -- Draw the balloon string.
  line(50, 60, 50, 80)

  describe('A red balloon in a blue sky.')
end
```

## Syntax

```lua
bezier(x1, y1, x2, y2, x3, y3, x4, y4)
```

## Parameters

| Parameter |                                                          |
| -         | --------------------------------------------------       |
| x1        | Number: x-coordinate of the first anchor point.          |
| y1        | Number: y-coordinate of the first anchor point.          |
| x2        | Number: x-coordinate of the first control point.         |
| y2        | Number: y-coordinate of the first control point.         |
| x3        | Number: x-coordinate of the second control point.        |
| y3        | Number: y-coordinate of the second control point.        |
| x4        | Number: x-coordinate of the second anchor point.         |
| y4        | Number: y-coordinate of the second anchor point.         |

## Related

* [curve()](curve.md)
* [vertex()](vertex.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
