# rotate()
 
Rotates the coordinate system.

By default, the positive x-axis points to the right and the positive y-axis points downward. The `rotate()` function changes this orientation by rotating the coordinate system about the origin. Everything drawn after `rotate()` is called will appear to be rotated.

The first parameter, `angle`, is the amount to rotate. For example, calling `rotate(1)` rotates the coordinate system clockwise 1 radian which is nearly 57˚. `rotate()` interprets angle values using the current angleMode().

By default, transformations accumulate. For example, calling `rotate(1)` twice has the same effect as calling `rotate(2)` once. The push() and pop() functions can be used to isolate transformations within distinct drawing groups.

Note: Transformations are reset at the beginning of the draw loop. Calling `rotate(1)` inside the draw() function won't cause shapes to spin.

## Examples

![rotate example 1](assets/rotate1.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle("rotate example")
  describe(
    "A white rectangle on a gray background. The rectangle's long axis runs from top-left to bottom-right."
  )
end

function draw()
  background(200)

  -- Rotate the coordinate system 1/8 turn.
  rotate(QUARTER_PI)

  -- Draw a rectangle at coordinates (50, 0).
  rect(50, 0, 40, 20)
end
```

![rotate example 2](assets/rotate2.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle('rotate() example')
  describe(
    "A white rectangle on a gray background. The rectangle's long axis runs from top-left to bottom-right."
  )
end

function draw() 
  background(200)

  -- Rotate the coordinate system 1/16 turn.
  rotate(QUARTER_PI / 2)

  -- Rotate the coordinate system another 1/16 turn.
  rotate(QUARTER_PI / 2)

  -- Draw a rectangle at coordinates (50, 0).
  rect(50, 0, 40, 20)
end
```

![rotate example 3](assets/rotate3.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle('rotate() example')
  -- Use degrees.
  angleMode(DEGREES)

  describe(
    "A white rectangle on a gray background. The rectangle's long axis runs from top-left to bottom-right."
  )
end

function draw() 
  background(200)

  -- Rotate the coordinate system 1/8 turn.
  rotate(45)

  -- Draw a rectangle at coordinates (50, 0).
  rect(50, 0, 40, 20)
end
```

![rotate example 4](assets/rotate4.gif)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle('rotate() example')
  describe(
    'A white rectangle on a gray background. The rectangle rotates slowly about the top-left corner. It disappears and reappears periodically.'
  )
end

function draw() 
  background(200)

  -- Rotate the coordinate system a little more each frame.
  local angle = frameCount * 0.01
  rotate(angle)

  -- Draw a rectangle at coordinates (50, 0).
  rect(50, 0, 40, 20)
end
```

## Related

* [applyMatrix()](applyMatrix.md)
* [resetMatrix()](resetMatrix.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
