# tan()
 
Calculates the tangent of an angle.

`tan()` is useful for many geometric tasks in creative coding. The values returned range from -Infinity to Infinity and repeat periodically as the input angle increases. `tan()` calculates the tan of an angle, using radians by default, or according to angleMode() setting (RADIANS or DEGREES).

## Examples

![tan example 1](assets/tan1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  describe('A series of identical curves drawn with black dots. Each curve starts from the top of the canvas, continues down at a slight angle, flattens out at the middle of the canvas, then continues to the bottom.')
end

function draw()
  -- Calculate the coordinates.
  local x = frameCount
  local y = 5 * tan(x * 0.1) + 50

  -- Draw the point.
  point(x, y)
end
```

## Syntax

```lua
tan(angle)
```

## Parameters

| Parameter |                                                                                                       |
| -         | --                                                                                                    |
| angle     | Number: the angle, in radians by default, or according to angleMode() setting (RADIANS or DEGREES) |

## Returns

Number: tangent of the angle

## Related

* [acos()](acos.md)
* [angleMode()](angleMode.md)
* [asin()](asin.md)
* [atan()](atan.md)



---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
