# fract()
 
Calculates the fractional part of a number.

A number's fractional part includes its decimal values. For example, `fract(12.34)` returns 0.34.

## Examples

![fract example 1](assets/fract1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Style the text.
  textAlign(CENTER)
  textSize(16)
  fill(0)

  -- Original number.
  local n = 56.78
  text(n, 50, 33)

  -- Fractional part.
  local f = fract(n)
  text(f, 50, 67)

  describe('The number 56.78 written above the number 0.78.')
end
```

## Syntax

```lua
fract(n)
```

## Parameters

| Parameter |                                                        |
| -         | --                                                     |
| n         | Number: number whose fractional part will be computed. |

## Returns

Number: fractional part of n.

## Related

* [abs()](abs.md)
* [ceil()](ceil.md)
* [constrain()](constrain.md)
* [dist()](dist.md)



---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
