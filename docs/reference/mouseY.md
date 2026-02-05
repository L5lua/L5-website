# mouseY()

A `Number` system variable that tracks the mouse's vertical position.

`mouseY` keeps track of the mouse's position relative to the top-left corner of the canvas. For example, if the mouse is 50 pixels from the top edge of the canvas, then `mouseY` will be 50.

## Examples

![mouseY example 1](assets/mouseY1.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  describe("A horizontal black line moves up and down following the mouse's y-position.")
end

function draw()
  background(200)

  -- Draw a horizontal line that follows the mouse's y-coordinate.
  line(0, mouseY, 100, mouseY)
end
```

![mouseY example 2](assets/mouseX2.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  describe("A gray square. The mouse's x- and y-coordinates are displayed as the user moves the mouse.")
end

function draw()
  background(200)
  fill(0)

  -- Style the text.
  textAlign(CENTER)
  textSize(16)

  -- Display the mouse's coordinates.
  text('x: '..mouseX..' y:'..mouseY, 50, 50)
end
```

## Syntax

```lua
mouseY
```

## Returns

Number: current y-coordinate of mouse position.

## Related

* [mouseButton](mouseButton.md)
* [mouseY](mouseY.md)
* [movedX](movedX.md)
* [movedY](movedY.md)
* [pmouseX](pmouseX.md)
* [pmouseY](pmouseY.md)



---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
