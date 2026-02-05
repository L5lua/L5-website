# mouseX()
 
A `Number` system variable that tracks the mouse's horizontal position.

`mouseX` keeps track of the mouse's position relative to the top-left corner of the canvas. For example, if the mouse is 50 pixels from the left edge of the canvas, then `mouseX` will be 50.

## Examples

![mouseX example 1](assets/mouseX1.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  describe("A vertical black line moves left and right following the mouse's x-position.")
end

function draw()
  background(200)

  -- Draw a vertical line that follows the mouse's x-coordinate.
  line(mouseX, 0, mouseX, 100)
end
```

![mouseX example 2](assets/mouseX2.gif)

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
mouseX
```

## Returns

Number: Current x-coordinate of mouse.

## Related

* [mouseButton](mouseButton.md)
* [mouseY](mouseY.md)
* [movedX](movedX.md)
* [movedY](movedY.md)
* [pmouseX](pmouseX.md)
* [pmouseY](pmouseY.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
