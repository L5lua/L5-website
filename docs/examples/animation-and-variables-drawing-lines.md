# Drawing Lines

Click and drag the mouse to draw a line.

This example demonstrates the use of several built-in variables. [mouseX](/reference/mouseX.md) and [mouseY](/reference/mouseY.md) store the current mouse position, while the previous mouse position is represented by [pmouseX](/reference/pmouseX.md) and [pmouseY](/reference/pmouseY.md). 

This example also shows the use of [colorMode()](/reference/colorMode.md) with [HSB](/reference/HSB.md) (hue-saturation-brightness), so that the first variable sets the hue.

![A black screen has rainbow colored squiggly lines draw in animation](/assets/examples/drawing-lines.gif)

```lua
require("L5")

function setup()
  -- Set the title
  windowTitle('Drawing Lines')

  -- Create the canvas
  size(710, 400)

  -- Set background to black
  background(0)

  -- Set width of the lines
  strokeWeight(10)

  -- Set color mode to hue-saturation-brightness (HSB)
  colorMode(HSB)

  -- Set screen reader accessible description
  describe('A blank canvas where the user draws by dragging the mouse')
end

function mouseDragged()
  -- Set the color based on the mouse position, and draw a line
  -- from the previous position to the current position
  local lineHue = mouseX - mouseY
  stroke(lineHue, 90, 90)
  line(pmouseX, pmouseY, mouseX, mouseY)
end
```

## Related Examples

* [Doodle Draw](doodle-draw.md)
* [Animation with Events](animation-and-variables-animation-with-events.md)
* [Conditions](animation-and-variables-conditions.md)

Drawing Lines: Revised by [Darren Kessner](https://github.com/dkessner). Edited and maintained by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people). Adapted to L5 2025. Licensed under CC BY-NC-SA 4.0.

