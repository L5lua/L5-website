# rect()

Draws a rectangle to the screen. A rectangle is a four-sided shape with every angle at ninety degrees. By default, the first two parameters set the location of the upper-left corner, the third sets the width, and the fourth sets the height. The way these parameters are interpreted, however, may be changed with the rectMode() function.

To draw a rounded rectangle, add a fifth parameter, which is used as the radius value for all four corners.

## Examples

![basic 1 rectangle](assets/rect1.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle("rect example")
  background(200)

  rect(30, 20, 55, 55)

  describe('A white square with black outline on a gray canvas.')
end
```

![rectangle 2 example](assets/rect2.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle("rect example")
  background(200)

  rect(30, 20, 55, 40)

  describe('A white rectangle with black outline on a gray canvas.')
end
```

![rectangle 3 example](assets/rect3.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle("rect example")
  background(200)

  -- Give all corners a radius of 20.
  rect(30, 20, 55, 50, 20)

  describe('A white rectangle with a black outline and round edges on a gray canvas.')
end
```

## Syntax

```lua
rect(a, b, c, d)
rect(a, b, c, d, r)
```

## Parameters

| Parameter |                                                                  |
| -         | --------------------------------------------------               |
| a         | Number: x-coordinate of the rectangle by default.               |
| b         | Number: y-coordinate of the rectangle by default.               |
| c         | Number: width of the rectangle by default.                      |
| d         | Number: height of the rectangle by default.                     |
| r         | Number: radii of the corners.                                   |

## Related

* [rectMode](rectMode.md)
* [quad()](quad.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
