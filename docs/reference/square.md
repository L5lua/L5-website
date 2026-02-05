# square()

Draws a square.

A square is a four-sided shape defined by the `x`, `y`, and `s` parameters. `x` and `y` set the location of its top-left corner. `s` sets its width and height. Every angle in the square measures 90˚ and all its sides are the same length. See rectMode() for other ways to define squares.

The version of square() with four parameters creates a rounded square. The fourth parameter sets the radius for all four corners.

## Examples

![basic square](assets/square.webp)

```lua
  size(100, 100)

  background(200)

  square(30, 20, 55)

  describe('A white square with a black outline on a gray canvas.')
end
```


![square with rounded edges](assets/square-rounded.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Give all corners a radius of 20.
  square(30, 20, 55, 20)

  describe('A white square with a black outline and round edges on a gray canvas.')
end
```

## Syntax

```lua
square(x, y, s)
square(x, y, s, r)
```

## Parameters

| Parameter |                                                                  |
| -         | --------------------------------------------------               |
| x         | Number: x-coordinate of the square.                              |
| y         | Number: y-coordinate of the square .                             |
| s         | Number: side size of the square.                                 |
| r         | Number: optional radii of the corners.                           |

## Related

* [rect()](rect.md)
* [rectMode](rectMode.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
