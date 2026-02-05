# dist()
 
Calculates the distance between two points.

## Examples

![dist example 1](assets/dist1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Set the coordinates.
  local x1 = 10
  local y1 = 50
  local x2 = 90
  local y2 = 50

  -- Draw the points and a line connecting them.
  line(x1, y1, x2, y2)
  strokeWeight(5)
  point(x1, y1)
  point(x2, y2)

  -- Calculate the distance.
  local d = dist(x1, y1, x2, y2)

  -- Style the text.
  textAlign(CENTER)
  textSize(16)

  -- Display the distance.
  text(d, 43, 40)

  describe('Two dots connected by a horizontal line. The number 80 is written above the center of the line.')
end
```

## Syntax

```lua
dist(x1, y1, x2, y2)
```

## Parameters

| Parameter | |
| - | -- |
| x1 | Number: x-coordinate of the first point. |
| y1 | Number: y-coordinate of the first point. |
| x2 | Number: x-coordinate of the second point. |
| y2 | Number: y-coordinate of the second point. |

## Returns

Number: distance between the two points.

## Related

* [abs()](abs.md)
* [ceil()](ceil.md)
* [constrain()](constrain.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
