# norm()

Maps a number from one range to a value between 0 and 1.

For example, `norm(2, 0, 10)` returns 0.2. 2's position in the original range [0, 10] is proportional to 0.2's position in the range [0, 1]. This is the same as calling `map(2, 0, 10, 0, 1)`.

Numbers outside of the original range are not constrained between 0 and 1. Out-of-range values are often intentional and useful.

## Examples

![norm example 1](assets/norm1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  -- Use RGB color with values from 0 to 1.
  colorMode(RGB, 1)

  describe('A square changes color from black to red as the mouse moves from left to right.')
end

function draw()
  -- Calculate the redValue.
  local redValue = norm(mouseX, 0, 100)

  -- Paint the background.
  background(redValue, 0, 0)
end
```

## Syntax

```lua
norm(value, start, stop)
```

## Parameters

| Parameter |                                                                    |
| -         | --                                                                 |
| value     | Number: incoming value to be normalized.                           |
| start     | Number: lower bound of the value's current range.                  |
| stop      | Number: upper bound of the value's current range.                  |

## Returns

Number: normalized number.

## Related

* [map()](map.md)
* [abs()](abs.md)
* [constrain()](constrain.md)
* [dist()](dist.md)



---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
