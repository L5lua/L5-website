# exp()
 
Calculates the value of Euler's number e (2.71828...) raised to the power of a number.

## Examples

![exp example 1](assets/exp1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Top-left.
  local d = exp(1)
  circle(10, 10, d)

  -- Left-center.
  d = exp(2)
  circle(20, 20, d)

  -- Right-center.
  d = exp(3)
  circle(40, 40, d)

  -- Bottom-right.
  d = exp(4)
  circle(80, 80, d)

  describe('A series of circles that grow exponentially from top left to bottom right.')
end
```

![exp example 2](assets/exp2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  describe('A series of black dots that grow exponentially from left to right.')
end

function draw() 
  -- Invert the y-axis.
  scale(1, -1);
  translate(0, -100)

  -- Calculate the coordinates.
  local x = frameCount;
  local y = 0.005 * exp(x * 0.1)

  -- Draw a point.
  point(x, y)
end
```

## Syntax

```lua
exp(n)
```

## Parameters

| Parameter |                              |
| -         | --                           |
| n         | Number: exponent to raise.   |

## Returns

Number: e^n

## Related

* [pow()](pow.md)
* [abs()](abs.md)
* [ceil()](ceil.md)
* [constrain()](constrain.md)
* [dist()](dist.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
