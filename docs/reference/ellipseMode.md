# ellipseMode()

Changes where ellipses, circles, and arcs are drawn.

By default, the first two parameters of `ellipse()`, `circle()`, and `arc()` are the x- and y-coordinates of the shape's center. The next parameters set the shape's width and height. This is the same as calling `ellipseMode(CENTER)`.

`ellipseMode(RADIUS)` also uses the first two parameters to set the x- and y-coordinates of the shape's center. The next parameters are half of the shapes's width and height. Calling `ellipse(0, 0, 10, 15)` draws a shape with a width of 20 and height of 30.

`ellipseMode(CORNER)` uses the first two parameters as the upper-left corner of the shape. The next parameters are its width and height.

`ellipseMode(CORNERS)` uses the first two parameters as the location of one corner of the ellipse's bounding box. The next parameters are the location of the opposite corner.

The argument passed to `ellipseMode()` must be written in ALL CAPS because the constants `CENTER`, `RADIUS`, `CORNER`, and `CORNERS` are defined this way. Lua is a case-sensitive language.

## Examples

![ellipseMode example 1](assets/ellipseMode1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- White ellipse.
  ellipseMode(RADIUS)
  fill(255)
  ellipse(50, 50, 30, 30)

  -- Gray ellipse.
  ellipseMode(CENTER)
  fill(100)
  ellipse(50, 50, 30, 30)

  describe('A white circle with a gray circle at its center. Both circles have black outlines.')
end
```

![ellipseMode example 2](assets/ellipseMode2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- White ellipse.
  ellipseMode(CORNER)
  fill(255)
  ellipse(25, 25, 50, 50)

  -- Gray ellipse.
  ellipseMode(CORNERS)
  fill(100)
  ellipse(25, 25, 50, 50)

  describe('A white circle with a gray circle at its top-left corner. Both circles have black outlines.')
end
```

## Syntax

```lua
ellipseMode(mode)
```

## Parameters

| Parameter |                                                     |
| -         | --------------------------------------------------  |
| mode      | Constant: either CENTER, RADIUS, CORNER or CORNERS |

## Related

* [ellipse()](ellipse.md)
* [noSmooth()](noSmooth.md)
* [rectMode()](rectMode.md)
* [smooth()](smooth.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
