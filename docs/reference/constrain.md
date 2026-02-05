# constrain()
 
Constrains a number between a minimum and maximum value.

## Examples

![constrain example 1](assets/constrain1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  describe('A black dot drawn on a gray square follows the mouse from left to right. Its movement is constrained to the middle third of the square.')
end

function draw()
  background(200)

  local x = constrain(mouseX, 33, 67)
  local y = 50

  strokeWeight(5)
  point(x, y)
end
```

![constrain example 2](assets/constrain2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  describe('Two vertical lines. Two circles move horizontally with the mouse. One circle stops at the vertical lines.')
end

function draw() 
  background(200)

  -- Set boundaries and draw them.
  local leftWall = 25
  local rightWall = 75
  line(leftWall, 0, leftWall, 100)
  line(rightWall, 0, rightWall, 100)

  -- Draw a circle that follows the mouse freely.
  fill(255)
  circle(mouseX, 33, 9)

  -- Draw a circle that's constrained.
  local xc = constrain(mouseX, leftWall, rightWall)
  fill(0)
  circle(xc, 67, 9)
end
```

## Syntax

```lua
constrain(n, low, high)
```

## Parameters

| Parameter |                              |
| -         | --                           |
| n         | Number: number to constrain. |
| low       | Number: minimum limit.      |
| high     | Number: minimum limit.      |

## Returns

Number: constrained number

## Related

* [abs()](abs.md)
* [floor()](floor.md)
* [round()](round.md)
* [int()](int.md)



---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
