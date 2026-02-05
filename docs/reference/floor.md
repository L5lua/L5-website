# floor()

Calculates the closest integer value that is less than or equal to the value of a number.

## Examples

![floor example 1](assets/floor1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  -- Use RGB color with values from 0 to 1.
  colorMode(RGB, 1)

  noStroke()

  -- Draw the left rectangle.
  local r = 0.8
  fill(r, 0, 0)
  rect(0, 0, 50, 100)

  -- Round r down to 0.
  r = floor(r)

  -- Draw the right rectangle.
  fill(r, 0, 0)
  rect(50, 0, 50, 100)

  describe('Two rectangles. The one on the left is bright red and the one on the right is black.')
end
```

## Syntax

```lua
floor(n)
```

## Parameters

| Parameter |                               |
| -         | --                            |
| n         | Number: number to round down. |

## Returns

Number: rounded down number

## Related

* [abs()](abs.md)
* [ceil()](ceil.md)
* [round()](round.md)
* [int()](int.md)



---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
