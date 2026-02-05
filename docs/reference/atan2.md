# atan2()
 
Calculates the angle formed by a point, the origin, and the positive x-axis.

`atan2()` is most often used for orienting geometry to the mouse's position, as in `atan2(mouseY, mouseX)`. The first parameter is the point's y-coordinate and the second parameter is its x-coordinate.

By default, `atan2()` returns values in the range -π (about -3.14) to π (3.14). If the angleMode() is `DEGREES`, then values are returned in the range -180 to 180.

## Examples

![atan2 example 1](assets/atan21.gif)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle("atan2 example")
  describe('A rectangle at the top-left of the canvas rotates with mouse movements.')
end

function draw() 
  background(200)
  -- Calculate the angle between the mouse
  -- and the origin.
  local a = atan2(mouseY, mouseX)

  -- Rotate.
  rotate(a)

  -- Draw the shape.
  rect(0, 0, 60, 10)
end
```

![atan2 example 2](assets/atan22.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  describe('A rectangle at the center of the canvas rotates with mouse movements.')
end

function draw()
  background(200)

  -- Translate the origin to the center.
  translate(50, 50)

  -- Get the mouse's coordinates relative to the origin.
  local x = mouseX - 50
  local y = mouseY - 50

  -- Calculate the angle between the mouse and the origin.
  local a = atan2(y, x)

  -- Rotate.
  rotate(a)

  -- Draw the shape.
  rect(-30, -5, 60, 10)
end
```

## Syntax

```lua
atan2(y, x)
```

## Parameters

| Parameter |                                                   |
| -         | --                                                |
| y         | Number: y-coordinate of the point                 |
| x         | Number: x-coordinate of the point                 |

## Returns

Number: arc tangent of the given point

## Related

* [acos()](acos.md)
* [angleMode()](angleMode.md)
* [asin()](asin.md)
* [atan()](atan.md)



---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
