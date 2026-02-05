# log()
 
Calculates the natural logarithm (the base-e logarithm) of a number.

`log()` expects the `n` parameter to be a value greater than 0 because the natural logarithm is defined that way.

## Examples

![log example 1](assets/log1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Top-left.
  local d = log(50)
  circle(33, 33, d)

  -- Bottom-right.
  d = log(500000000)
  circle(67, 67, d)

  describe('Two white circles. The circle at the top-left is small. The circle at the bottom-right is about five times larger.')
end
```

![log example 2](assets/log2.webp)

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

  -- Calculate coordinates.
  local x = frameCount
  local y = 15 * log(x)

  -- Draw a point.
  point(x, y)
end
```

## Syntax

```lua
log(n)
```

## Parameters

| Parameter |                                                        |
| -         | --                                                     |
| n         | Number: number greater than 0.                         |

## Returns

Number: natural logarithm of n.

## Related

* [abs()](abs.md)
* [ceil()](ceil.md)
* [constrain()](constrain.md)
* [dist()](dist.md)



---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
