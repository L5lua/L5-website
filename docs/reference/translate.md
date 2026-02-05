# translate()
 
Translates the coordinate system.

By default, the origin `(0, 0)` is at the sketch's top-left corner in 2D. The `translate()` function shifts the origin to a different position. Everything drawn after `translate()` is called will appear to be shifted. 

The first way to call `translate()` uses numbers to set the amount of translation. The two parameters, `x` and `y`, set the amount to translate along the positive x- and y-axes. For example, calling `translate(20, 30)` translates the origin 20 pixels along the x-axis and 30 pixels along the y-axis. 

By default, transformations accumulate. For example, calling `translate(10, 0)` twice has the same effect as calling `translate(20, 0)` once. The push() and pop() functions can be used to isolate transformations within distinct drawing groups.

Note: Transformations are reset at the beginning of the draw loop. Calling `translate(10, 0)` inside the draw() function won't cause shapes to move continuously.

## Examples

![translate example 1](assets/translate1.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle('translate() example')
  describe('A white circle on a gray background.')
end

function draw()
  background(200)

  -- Translate the origin to the center.
  translate(50, 50)

  -- Draw a circle at coordinates (0, 0).
  circle(0, 0, 40)
end
```

![translate example 2](assets/translate2.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle("translate() example")
  describe(
    'Two circles drawn on a gray background. The blue circle on the right overlaps the red circle at the center.'
  )
end

function draw() 
  background(200)

  -- Translate the origin to the center.
  translate(50, 50)

  -- Draw the red circle.
  fill('red')
  circle(0, 0, 40)

  -- Translate the origin to the right.
  translate(25, 0)

  -- Draw the blue circle.
  fill('blue')
  circle(0, 0, 40)
end
```

![translate example 3](assets/translate3.gif)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle("translate() example")
  describe('A white circle moves slowly from left to right on a gray background.')
end

function draw() 
  background(200)

  -- Calculate the x-coordinate.
  local x = frameCount * 0.2

  -- Translate the origin.
  translate(x, 50)

  -- Draw a circle at coordinates (0, 0).
  circle(0, 0, 40)
end
```

## Syntax

```lua
translate(x, y)
```

## Parameters

| Parameter | |
| - | -- |
| x | Number: amount to translate along the positive x-axis. |
| y | Number: amount to translate along the positive y-axis. |

## Related

* [rotate()](rotate.md)
* [scale()](scale.md)
* [push()](push.md)
* [pop()](pop.md)
* [applyMatrix()](applyMatrix.md)
* [resetMatrix()](resetMatrix.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
