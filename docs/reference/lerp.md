# lerp()
 
Calculates a number between two numbers at a specific increment.

The `amt` parameter is the amount to interpolate between the two numbers. 0.0 is equal to the first number, 0.1 is very near the first number, 0.5 is half-way in between, and 1.0 is equal to the second number. The `lerp()` function is convenient for creating motion along a straight path and for drawing dotted lines.

If the value of `amt` is less than 0 or more than 1, `lerp()` will return a number outside of the original interval. For example, calling `lerp(0, 10, 1.5)` will return 15.

## Examples

![lerp example 1](assets/lerp1.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle("Lerp example")
  background(200)

  -- Declare variables for coordinates.
  local a = 20
  local b = 80
  local c = lerp(a, b, 0.2)
  local d = lerp(a, b, 0.5)
  local e = lerp(a, b, 0.8)

  strokeWeight(5)

  -- Draw the original points in black.
  stroke(0)
  point(a, 50)
  point(b, 50)

  -- Draw the lerped points in gray.
  stroke(100)
  point(c, 50)
  point(d, 50)
  point(e, 50)

  describe('Five points in a horizontal line. The outer points are black and the inner points are gray.')
end
```

![lerp example 2](assets/lerp2.webp)

```lua
local x = 50
local y = 50
local targetX = 50
local targetY = 50

require("L5")

function setup()
  size(100, 100)

  background(200)

  describe('A white circle at the center of a gray canvas. The circle moves to where the user clicks, then moves smoothly back to the center.')
end

function draw() 
  background(220)

  -- Move x and y toward the target.
  x = lerp(x, targetX, 0.05)
  y = lerp(y, targetY, 0.05)

  -- Draw the circle.
  circle(x, y, 20)
end

-- Set x and y when the user clicks the mouse.
function mouseClicked() 
  x = mouseX
  y = mouseY
end
```

## Syntax

```lua
lerp(start, stop, amt)
```

## Parameters

| Parameter |                                                        |
| -         | --                                                     |
| start     | Number: first value.                                   |
| stop      | Number: second value.                                  |
| amt       | Number: number.                                        |

## Returns

Number: lerped value.

## Related

* [abs()](abs.md)
* [ceil()](ceil.md)
* [constrain()](constrain.md)
* [map()](map.md)
* [dist()](dist.md)



---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
