# strokeWeight()

Sets the width of the stroke used for lines, points, and the border around shapes. All widths are set in units of pixels.

Using point() with strokeWeight(1) or smaller may draw nothing to the screen, depending on the graphics settings of the computer. Workarounds include drawing the point using either circle() or square().

## Examples

![strokeWeight example](assets/strokeWeight.webp)

```lua
require("L5")

function setup()
  size(400, 400)
  strokeWeight(4)  -- Default
  line(80, 80, 320, 80)
  strokeWeight(16)  -- Thicker
  line(80, 160, 320, 160)
  strokeWeight(40)  -- Beastly
  line(80, 280, 320, 280)
  describe('3 lines of increasing thickness')
end
```

## Syntax

```lua
strokeWeight(weight)
```

## Parameters

| Parameter |                                                     |
| -         | --------------------------------------------------  |
| weight    | Number: The weight (in pixels) of the stroke        |

## Related

* [stroke()](stroke.md)
* [strokeJoin()](strokeJoin.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
