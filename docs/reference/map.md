# map()
 
Re-maps a number from one range to another.

For example, calling `map(2, 0, 10, 0, 100)` returns 20. The first three arguments set the original value to 2 and the original range from 0 to 10. The last two arguments set the target range from 0 to 100. 20's position in the target range [0, 100] is proportional to 2's position in the original range [0, 10].

The sixth parameter, `withinBounds`, is optional. By default, `map()` can return values outside of the target range. For example, `map(11, 0, 10, 0, 100)` returns 110. Passing `true` as the sixth parameter constrains the remapped value to the target range. For example, `map(11, 0, 10, 0, 100, true)` returns 100.

## Examples

![map example 1](assets/map1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  describe('Two horizontal lines. The top line grows horizontally as the mouse moves to the right. The bottom line also grows horizontally but is scaled to stay on the left half of the canvas.')
end

function draw()
  background(200)

  -- Draw the top line.
  line(0, 25, mouseX, 25)

  -- Remap mouseX from [0, 100] to [0, 50].
  local x = map(mouseX, 0, 100, 0, 50)

  -- Draw the bottom line.
  line(0, 75, x, 75)
end
```

![map example 2](assets/map2.webp)

```lua
require("L5")

function setup()
  size(100,100)

  describe('A circle changes color from black to white as the mouse moves from left to right.')
end

function draw() 
  background(200)

  -- Remap mouseX from [0, 100] to [0, 255]
  local c = map(mouseX, 0, 100, 0, 255)

  -- Style the circle.
  fill(c)

  -- Draw the circle.
  circle(50, 50, 20)
end
```

## Syntax

```lua
map(value, start1, stop1, start2, stop2, [withinBounds])
```

## Parameters

| Parameter    |                                                         |
| -            | --                                                      |
| value        | Number: the value to be remapped.                       |
| start1       | Number: lower bound of the value's current range.       |
| stop1        | Number: upper bound of the value's current range.       |
| start2       | Number: lower bound of the value's target range.        |
| stop2        | Number: upper bound of the value's target range.        |
| withinBounds | Boolean: constrain the value to the newly mapped range. |

## Returns

Number: remapped number.

## Related

* [constrain()](constrain.md)
* [abs()](abs.md)
* [round()](round.md)
* [dist()](dist.md)



---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
