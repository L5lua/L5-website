# sqrt()

Calculates the square root of a number.

A number's square root can be multiplied by itself to produce the original number. For example, `sqrt(9)` returns 3 because 3 × 3 = 9. `sqrt()` always returns a positive value. `sqrt()` doesn't work with negative arguments such as `sqrt(-9)`.

## Examples

![sqrt example 1](assets/sqrt1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Top-left.
  local d = sqrt(16)
  circle(33, 33, d)

  -- Bottom-right.
  d = sqrt(1600)
  circle(67, 67, d)

  describe('Two white circles. The circle at the top-left is small. The circle at the bottom-right is ten times larger.')
end
```

![sqrt example 2](assets/sqrt2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  describe('A series of black dots that get higher slowly from left to right.')
end

function draw() 
  -- Invert the y-axis.
  scale(1, -1)
  translate(0, -100)

  -- Calculate the coordinates.
  local x = frameCount
  local y = 5 * sqrt(x)

  -- Draw the point.
  point(x, y)
end
```

## Syntax

```lua
sqrt(n)
```

## Parameters

| Parameter |                                                                    |
| -         | --                                                                 |
| n         | Number: non-negative number to square root.                        |

## Returns

Number: square root of number.

## Related

* [abs()](abs.md)
* [ceil()](ceil.md)
* [constrain()](constrain.md)
* [dist()](dist.md)



---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
