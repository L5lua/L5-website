# circle()

Draws a circle to the screen. By default, the first two parameters set the location of the center, and the third sets the shape's width and height. The origin may be changed with the ellipseMode() function.

## Examples

![circle 1 example](assets/circle1.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  windowTitle("circle example")
  background(200)
  circle(50, 50, 25)

  describe('A white circle with black outline in the middle of a gray canvas.')
end
```

## Syntax

```lua
circle(x, y, w)
```

## Parameters

| Parameter |                                                    |
| -          | -------------------------------------------------- |
| x          | Number: x-coordinate of the center of the ellipse. |
| y          | Number: y-coordinate of the center of the ellipse. |
| w          | Number: width and height of the ellipse.           |

## Related

* [ellipse()](ellipse.md)
* [ellipseMode()](ellipseMode.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
