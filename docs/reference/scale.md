# scale()
 
Scales the coordinate system.

By default, shapes are drawn at their original scale. A rectangle that's 50 pixels wide appears to take up half the width of a 100 pixel-wide canvas. The `scale()` function can shrink or stretch the coordinate system so that shapes appear at different sizes. There are two ways to call `scale()` with parameters that set the scale factor(s).

The first way to call `scale()` uses numbers to set the amount of scaling. The first parameter, `s`, sets the amount to scale each axis. For example, calling `scale(2)` stretches the x-, y-, and z-axes by a factor of 2. The next parameter, `y` is optional. It sets the amount to scale the y-axis. For example, calling `scale(2, 0.5)` stretches the x-axis by a factor of 2, and shrinks the y-axis by a factor of 0.5.

By default, transformations accumulate. For example, calling `scale(1)` twice has the same effect as calling `scale(2)` once. The push() and pop() functions
can be used to isolate transformations within distinct drawing groups.

Note: Transformations are reset at the beginning of the draw loop. Calling `scale(2)` inside the draw() function won't cause shapes to grow continuously.

## Examples

![scale example 1](assets/scale1.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle('scale() example')
  describe(
    'Two white squares on a gray background. The larger square appears at the top-center. The smaller square appears at the top-left.'
  )
end

function draw()
  background(200)

  -- Draw a square at (30, 20).
  square(30, 20, 40)

  -- Scale the coordinate system by a factor of 0.5.
  scale(0.5)

  -- Draw a square at (30, 20).
  -- It appears at (15, 10) after scaling.
  square(30, 20, 40)
end
```

![scale example 2](assets/scale2.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle('scale() example')
  describe('A rectangle and a square drawn in white on a gray background.')
end

function draw() 
  background(200)
  windowTitle('scale() example')
  -- Draw a square at (30, 20).
  square(30, 20, 40);

  -- Scale the coordinate system by factors of
  -- 0.5 along the x-axis and
  -- 1.3 along the y-axis.
  scale(0.5, 1.3)

  -- Draw a square at (30, 20).
  -- It appears as a rectangle at (15, 26) after scaling.
  square(30, 20, 40)
end
```

## Syntax

```lua
scale(s, [y])
```

## Parameters

| Parameter | |
| - | -- |
| s | Number: amount to scale along the positive x-axis. |
| y | Number: amount to scale along the positive y-axis. Defaults to `s`. |

## Related

* [translate()](translate.md)
* [rotate()](rotate.md)
* [push()](push.md)
* [pop()](pop.md)
* [resetMatrix()](resetMatrix.md)
* [applyMatrix()](applyMatrix.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
