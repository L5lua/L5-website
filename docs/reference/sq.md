# sq()

Calculates the square of a number.

Squaring a number means multiplying the number by itself. For example, `sq(3)` evaluates 3 × 3 which is 9. `sq(-3)` evaluates -3 × -3 which is also 9. Multiplying two negative numbers produces a positive number. The value returned by `sq()` is always positive.

## Examples

![sq example 1](assets/sq1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Top-left.
  local d = sq(3)
  circle(33, 33, d)

  -- Bottom-right.
  d = sq(6)
  circle(67, 67, d)

  describe('Two white circles. The circle at the top-left is small. The circle at the bottom-right is four times larger.')
end
```

![sq example 2](assets/sq2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  describe('A series of black dots that get higher quickly from left to right.')
end

function draw() 
  -- Invert the y-axis.
  scale(1, -1)
  translate(0, -100)

  -- Calculate the coordinates.
  local x = frameCount
  local y = 0.01 * sq(x)

  -- Draw the point.
  point(x, y)
end
```

## Syntax

```lua
sq(n)
```

## Parameters

| Parameter |                                                                    |
| -         | --                                                                 |
| n         | Number: number to square.                                          |

## Returns

Number: squared number.

## Related

* [abs()](abs.md)
* [ceil()](ceil.md)
* [constrain()](constrain.md)
* [dist()](dist.md)




---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
