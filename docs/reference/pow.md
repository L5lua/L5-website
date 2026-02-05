# pow()
 
Calculates exponential expressions such as <var>2<sup>3</sup></var>.

For example, `pow(2, 3)` evaluates the expression
2 × 2 × 2. `pow(2, -3)` evaluates 1 ÷
(2 × 2 × 2).

## Examples

![pow example 1](assets/pow1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Set the base of the exponent.
  local base = 3

  -- Top-left.
  local d = pow(base, 1)
  circle(10, 10, d)

  -- Left-center.
  d = pow(base, 2)
  circle(20, 20, d)

  -- Right-center.
  d = pow(base, 3)
  circle(40, 40, d)

  -- Bottom-right.
  d = pow(base, 4)
  circle(80, 80, d)

  describe('A series of circles that grow exponentially from top left to bottom right.')
end
```

## Syntax

```lua
pow(n, e)
```

## Parameters

| Parameter |                                                                    |
| -         | --                                                                 |
| n         | Number: base of the exponential expression.                        |
| e         | Number: power by which to raise the base.                          |

## Returns

Number: n^e.

## Related

* [exp()](exp.md)
* [ceil()](ceil.md)
* [abs()](abs.md)
* [constrain()](constrain.md)
* [dist()](dist.md)



---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
