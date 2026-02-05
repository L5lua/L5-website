# applyMatrix()
 
Applies a transformation matrix to the coordinate system.

Transformations such as translate(), rotate(), and scale() use matrix-vector multiplication behind the scenes. A table of numbers, called a matrix, encodes each transformation. The values in the matrix then multiply each point on the canvas, which is represented by a vector.

`applyMatrix()` allows for many transformations to be applied at once attempts to replicate the behavior of the p5.js implementation.

There are two ways to call `applyMatrix()` in two dimensions.

In 2D mode, the parameters `a`, `b`, `c`, `d`, `e`, and `f`, correspond to elements in the following transformation matrix:

![The transformation matrix used when applyMatrix is called in 2D mode.](assets/transformation-matrix.png)

The numbers can be passed individually, as in
`applyMatrix(2, 0, 0, 0, 2, 0)`. They can also be passed in an array, as in `applyMatrix({2, 0, 0, 0, 2, 0})`.

By default, transformations accumulate. The push() and pop() functions can be used to isolate transformations within distinct drawing groups.

Note: Transformations are reset at the beginning of the draw loop. Calling `applyMatrix()` inside the draw() function won't cause shapes to transform continuously.

## Examples

![applyMatrix example 1](assets/applyMatrix1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  describe('A white circle on a gray background.')
end

function draw()
  background(200)

  -- Translate the origin to the center.
  applyMatrix(1, 0, 0, 1, 50, 50)

  -- Draw the circle at coordinates (0, 0).
  circle(0, 0, 40)
end
```

![applyMatrix example 2](assets/applyMatrix2.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle("applyMatrix(0 example")
  describe('A white circle on a gray background.')
end

function draw()
  background(200)

  -- Translate the origin to the center.
  local m = {1, 0, 0, 1, 50, 50}
  applyMatrix(m)

  -- Draw the circle at coordinates (0, 0).
  circle(0, 0, 40)
end
```

![applyMatrix example 3](assets/applyMatrix3.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle('applyMatrix example')
  describe('A white quadrilateral on a gray background.')
end

function draw() 
  background(200)

  -- Calculate the shear factor.
  local angle = QUARTER_PI
  local ca = cos(angle)
  local sa = sin(angle)
  applyMatrix(ca, sa, -sa, ca, 0, 0)

  rect(50, 0, 40, 20)
end
```

![applyMatrix example 4](assets/applyMatrix4.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle('applyMatrix() example')
  describe('Two white squares on a gray background. The larger square appears at the top-center. The smaller square appears at the top-left.')
end

function draw() 
  background(200)

  -- Calculate the shear factor.
  local angle = QUARTER_PI
  local shearFactor = 1 / tan(HALF_PI - angle)

  -- Shear the coordinate system along the x-axis.
  applyMatrix(1, 0, shearFactor, 1, 0, 0)

  -- Draw the square.
  square(0, 0, 50)
end
```

![applyMatrix example 5](assets/applyMatrix5.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle('applyMatrix example')

  describe('A white quadrilateral on a gray background.')
end

function draw() 
  background(200)

  -- Calculate the shear factor.
  local angle = QUARTER_PI
  local shearFactor = 1 / tan(HALF_PI - angle)

  -- Shear the coordinate system along the x-axis.
  applyMatrix(1, 0, shearFactor, 1, 0, 0)

  -- Draw the square.
  square(0, 0, 50)
end
```

## Syntax

```lua
applyMatrix(arr)
```

```lua
applyMatrix(a, b, c, d, e, f)
```

## Parameters

| Parameter   |                                                                                                          |
| -           | --                                                                                                       |
| table array | Table array: an array containing the elements of the transformation matrix. Its length should be 6 (2D). |
| a           | Number: an element of the transformation matrix.                                                         |
| b           | Number: an element of the transformation matrix.                                                         |
| c           | Number: an element of the transformation matrix.                                                         |
| d           | Number: an element of the transformation matrix.                                                         |
| e           | Number: an element of the transformation matrix.                                                         |
| f           | Number: an element of the transformation matrix.                                                         |
| g           | Number: an element of the transformation matrix.                                                         |

## Related

* [resetMatrix()](resetMatrix.md)
* [rotate()](rotate.md)



---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
