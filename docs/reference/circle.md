# circle()

Draws a circle to the screen. By default, the first two parameters set the location of the center, and the third sets the shape's width and height. The origin may be changed with the ellipseMode() function.

## Examples

![circle example](assets/circle.webp)

```lua
function setup() 
  size(400, 400);
  circle(224, 184, 220);

  describe('A white circle on a gray canvas.')
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
