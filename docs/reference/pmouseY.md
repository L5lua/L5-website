# pmouseY()

A `Number` system variable that tracks the mouse's previous vertical position.

`pmouseY` keeps track of the mouse's position relative to the top-left corner of the canvas. Its value is mouseY from the previous frame. For example, if the mouse was 50 pixels from the top edge of the canvas during the last frame, then `pmouseY` will be 50.

## Examples

![pmouseY example 1](assets/pmouseX1.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  -- Slow the frame rate.
  frameRate(10)

  describe('A line follows the mouse as it moves. The line grows longer with faster movements.')
end

function draw()
  background(200)

  line(pmouseX, pmouseY, mouseX, mouseY)
end
```

## Syntax

```lua
pmouseY
```

## Returns

Number: y-coordinate of mouse from previous frame.

## Related

* [pmouseX](pmouseX.md)
* [mouseButton](mouseButton.md)
* [movedX](movedX.md)
* [movedY](movedY.md)
* [mouseX](mouseX.md)
* [mouseY](mouseY.md)



---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
