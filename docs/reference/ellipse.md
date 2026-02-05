# ellipse()

Draws an ellipse (oval).

An ellipse is a round shape defined by the `x`, `y`, `w`, and `h` parameters. `x` and `y` set the location of its center. `w` and `h` set its width and height. See ellipseMode() for other ways to set its position.

If no height is set, the value of width is used for both the width and height. If a negative height or width is specified, the absolute value is taken.

## Examples

![ellipse example](assets/ellipse.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  ellipse(50, 50, 80, 80)

  describe('A white circle on a gray canvas.')
end
```

## Syntax

```lua
ellipse(x, y, w, [h])
```

## Parameters

| Parameter |                                                    |
| -          | -------------------------------------------------- |
| x          | Number: x-coordinate of the center of the ellipse. |
| y          | Number: y-coordinate of the center of the ellipse. |
| w          | Number: width of the ellipse.                      |
| h          | Number: height of the ellipse.                     |

## Related

* [circle()](circle.md)
* [ellipseMode()](ellipseMode.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
