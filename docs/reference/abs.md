# abs()
 
Calculates the absolute value of a number.

A number's absolute value is its distance from zero on the number line. -5 and 5 are both five units away from zero, so calling `abs(-5)` and `abs(5)` both return 5. The absolute value of a number is always positive.

## Examples

![abs example 1](assets/abs1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  describe('A gray square with a vertical black line that divides it in half. A white rectangle gets taller when the user moves the mouse away from the line.')
end

function draw()
  background(200)

  -- Divide the canvas.
  line(50, 0, 50, 100)

  -- Calculate the mouse's distance from the middle.
  local h = abs(mouseX - 50)

  -- Draw a rectangle based on the mouse's distance
  -- from the middle.
  rect(0, 100 - h, 100, h)
end
```

## Syntax

```lua
abs(n)
```

## Parameters

| Parameter |                              |
| -         | --                           |
| n         | Number: number to compute.   |

## Returns

Number: absolute value of given number

## Related

* [ceil()](ceil.md)
* [constrain()](constrain.md)
* [dist()](dist.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
